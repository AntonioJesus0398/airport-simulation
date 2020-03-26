from random_vars import gen_bernoulli, gen_exp, gen_normal, gen_uniform, random


REPAIR_PROBABILITY = 0.1


def plane_arrival(time):
    return time + gen_exp(1/20)

def plane_landing(id, time):
    # print(f"{time}: Plane {id} is landing")
    return time +  gen_normal(mean=10, var=5)

def plane_takeoff(id, time):
    # print(f"{time}: Plane {id} is taking off")
    return time + gen_normal(mean=10, var=5)

def plane_repair(id, time):
    # print(f"{time}: Plane {id} is repairing")
    return time + gen_exp(1/15)

def plane_needs_repair():
    return random() < REPAIR_PROBABILITY

def plane_refuel(id, time):
    # print(f"{time}: Plane {id} is refueling")
    return time + gen_exp(1/30)

def plane_unload_load(id, time):
    # print(f"{time}: Plane {id} is unloading & loading passengers")
    return time + gen_exp(1/30)

def plane_needs_load_unload():
    u1 = random()
    u2 = random()
    if u2 < u1:
        return True
    return False

def serve_plane(id=0, time=0):
    """ Computes the time the plane remains on the landing track """

    time = plane_landing(id, time)

    time = plane_refuel(id, time)

    if plane_needs_load_unload():
        time = plane_unload_load(id, time)

    if plane_needs_repair():
        time = plane_repair(id, time)

    time = plane_takeoff(id, time)

    return time


INF = (1 << 64) - 1

def find_min(A):
    m = 0
    for i in range(len(A)):
        m = i if min(A[i], A[m]) == A[i] else m
    return m, A[m]


def simulate_airport(T=60*24*7):
    # Initilizing
    t = 0   # time global variable
    Na = 0  # number of arrivals

    # System state: [n, id1, id2, id3, id4, id5]
    #  n: number of planes in the system, idi: id of plane served on track i
    SS = [0 for _ in range(5)]
    n = 0

    ct = [INF for _ in range(5)]    # Completion times for services. Starts in position 1
    et = [0 for _ in range(5)]

    T0 = plane_arrival(time=t)    # First arrival
    ta = T0

    total = 0

    while t < T:

        if ta == min([ta] + ct):
            if ta > T:
                break
            t = ta
            Na += 1
            print(f"{t}: Plane {Na} is arriving")

            ta = plane_arrival(time=t)
            if n <= 4:
                for i, e in enumerate(SS):
                    if e == 0:
                        SS[i] = Na
                        total += t - et[i]
                        ct[i] = serve_plane(Na, t)
                        break
            n += 1

        else:
            m, ctm = find_min(ct)
            if ctm > t:
                break
            t = ctm

            print(f"{t}: Plane {SS[m]} is taking off")

            if n <= 5:
                SS[m] = 0
                ct[m] = INF
                et[i] = t
            else:
                M = max(SS)
                SS[m] = M + 1
                ct[m] = serve_plane(SS[m], t)

            n -= 1

    for i, e in enumerate(SS):
        if not e:
            total += T - et[i]
    return total
