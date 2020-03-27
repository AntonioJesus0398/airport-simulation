from src.airport import simulate_airport
from argparse import ArgumentParser

HOUR = 60
DAY = 24 * HOUR
WEEK = 7 * DAY
MONTH = 30 * DAY
YEAR = 365 * DAY

time_args = {
    "h": HOUR,
    "d": DAY,
    "w": WEEK,
    "m": MONTH,
    "y": YEAR
}


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--nosim', type=int, default=10000)
    parser.add_argument('--time', type=str, default="w")
    parser.add_argument('--arrival', type=float, default=1/20)
    parser.add_argument('--landing', type=int, nargs="+", default=[10, 5])
    parser.add_argument('--takeoff', type=int, nargs="+", default=[10, 5])
    parser.add_argument('--refuel', type=float, default=1/30)
    parser.add_argument('--repair', type=float, default=1/15)
    parser.add_argument('--load', type=float, default=1/30)
    parser.add_argument('--repairprob', type=float, default=0.1)

    args = parser.parse_args()
    nosim = int(args.nosim)
    arrival = float(args.arrival)
    landing = tuple(args.landing)
    takeoff = tuple(args.takeoff)
    refuel = float(args.refuel)
    repair = float(args.repair)
    load = float(args.load)
    repairprob = float(args.repairprob)
    time = time_args[args.time]

    mean = 0
    for _ in range(nosim):
        totals = simulate_airport(T=time, arrival_rate=arrival, landing_rate=landing, load_rate=load, takeoff_rate=takeoff, refuel_rate=refuel, repair_rate=repair, repair_prob=repairprob)
        mean += sum(totals)
    mean = mean / (10000 * 5)

    days = mean/60//24
    hours = (mean - days*24*60) // 60
    minutes = (mean - days*24*60 - hours*60 )//1
    print(f"After {nosim} simulations:")
    print(f"Mean: {mean/60} hours")
    print(f"{days} days, {hours} hours, {minutes} minutes")