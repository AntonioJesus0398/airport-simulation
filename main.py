from src.airport import simulate_airport
import src.random_vars

HOUR = 60
DAY = 24 * HOUR
WEEK = 7 * DAY


if __name__ == "__main__":
    mean = 0
    for _ in range(10000):
        totals = simulate_airport(T=WEEK)
        mean += sum(totals)
    mean = mean / (10000 * 5)

    days = mean/60//24
    hours = (mean - days*24*60) // 60
    minutes = (mean - days*24*60 - hours*60 )//1
    print(f"Mean: {mean/60} hours")
    print(f"{days} days, {hours} hours, {minutes} minutes")