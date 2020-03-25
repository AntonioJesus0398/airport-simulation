from random_vars import gen_bernoulli, gen_exp, gen_normal, gen_uniform, random


REPAIR_PROBABILITY = 0.1


def plane_arrival(id, time):
    print(f"{time}: Plane {id} is arriving")
    return gen_exp(20)

def plane_landing(id, time):
    print(f"{time}: Plane {id} is landing")
    return gen_normal(mean=10, var=5)

def plane_takeoff(id, time):
    print(f"{time}: Plane {id} is taking off")
    return gen_normal(mean=10, var=5)

def plane_repair(id, time):
    print(f"{time}: Plane {id} is repairing")
    return gen_exp(15)

def plane_needs_repair():
    return random() < REPAIR_PROBABILITY

def plane_refuel(id, time):
    print(f"{time}: Plane {id} is refueling")
    return gen_exp(30)

def plane_unload_load(id, time):
    print(f"{time}: Plane {id} is unloading & loading passengers")
    return gen_exp(30)

def plane_needs_load_unload():
    u1 = random()
    u2 = random()
    if u2 < u1:
        return True
    return False

def serve_plane(id, time):
    """ Computes the time the plane remains on the landing track """

    time += plane_landing(id, time)

    time += plane_refuel(id, time)

    if plane_needs_load_unload():
        time += plane_unload_load(id, time)

    if plane_needs_repair():
        time += plane_repair(id, time)

    time += plane_takeoff(id, time)

    return time
