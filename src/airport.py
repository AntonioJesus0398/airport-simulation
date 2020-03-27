from src.random_vars import gen_bernoulli, gen_exp, gen_normal, gen_uniform, random


def plane_arrival(time, rate):
    return time + gen_exp(rate)

def plane_landing(time, rate):
    return time +  gen_normal(mean=rate[0], var=rate[1])

def plane_takeoff(time, rate):
    return time + gen_normal(mean=rate[0], var=rate[1])

def plane_repair(time, rate):
    return time + gen_exp(rate)

def plane_needs_repair(repair_prob):
    return random() < repair_prob

def plane_refuel(time, rate):
    return time + gen_exp(rate)

def plane_unload_load(time, rate):
    return time + gen_exp(rate)

def plane_needs_load_unload():
    u1 = random()
    u2 = random()
    if u2 < u1:
        return True
    return False

def serve_plane(time, landing_rate, refuel_rate, repair_rate, load_rate, takeoff_rate, repair_prob):
    """ Computes the time the plane remains on the landing track """

    time = plane_landing(time, landing_rate)

    time = plane_refuel(time, refuel_rate)

    if plane_needs_load_unload():
        time = plane_unload_load(time, load_rate)

    if plane_needs_repair(repair_prob):
        time = plane_repair(time, repair_rate)

    time = plane_takeoff(time, takeoff_rate)

    return time


INF = (1 << 64) - 1

def find_min(A):
    m = 0
    for i in range(len(A)):
        m = i if min(A[i], A[m]) == A[i] else m
    return m, A[m]

# T: time range
def simulate_airport(T, arrival_rate=1/20, landing_rate=(10, 5), load_rate=1/30, repair_rate=1/15, refuel_rate=1/30, takeoff_rate=(10, 5), repair_prob=0.1):
    # Initilizing
    t = 0   # time global variable
    Na = 0  # number of arrivals

    SS = [0 for _ in range(5)]  # cystem state: [id1, id2, id3, id4, id5], idi: id of plane served on track i
    n = 0   # n: number of planes in the system

    ct = [INF for _ in range(5)]    # completion times for services. Starts in position 1
    et = [0 for _ in range(5)]  # time after which the runway was empty
    totals = [0 for _ in range(5)]  # total time the runway No i has been empty

    T0 = plane_arrival(t, arrival_rate)    # first arrival
    ta = T0

    while t < T:
        # next event is an arrival
        if ta == min([ta] + ct):

            # if it's after the deadline we discard it
            if ta > T:
                break

            t = ta
            Na += 1
            #print(f"{t}: Plane {Na} is arriving")

            # compute next arrival
            ta = plane_arrival(t, arrival_rate)

            # if there is an empty runway:
            if n <= 4:
                for i, e in enumerate(SS):
                    if e == 0:
                        SS[i] = Na
                        totals[i] += t - et[i]
                        ct[i] = serve_plane(t, landing_rate, refuel_rate, repair_rate, load_rate, takeoff_rate, repair_prob)
                        break
            n += 1

        # an airplane takes off
        else:
            m, ctm = find_min(ct)

            # if takes off after the deadline we discard it
            if ctm > T:
                break

            t = ctm
            #print(f"{t}: Plane {SS[m]} is taking off")

            # a runway is now empty
            if n <= 5:
                SS[m] = 0
                ct[m] = INF
                et[m] = t

            # the firt plane of the queue takes place on the runway
            else:
                M = max(SS)
                SS[m] = M + 1
                ct[m] = serve_plane(t, landing_rate, refuel_rate, repair_rate, load_rate, takeoff_rate, repair_prob)

            n -= 1

    # update totals
    for i, e in enumerate(SS):
        if not e:
            totals[i] += T - et[i]

    return totals
