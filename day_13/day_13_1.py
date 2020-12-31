from math import ceil
with open("day_13/day_13_input.txt") as f:
    timestamp = int(f.readline())
    buses = [int(bus) for bus in f.readline().split(",") if bus != "x"]

bus_id = min(buses, key=lambda x: x * (timestamp // x + 1))
wait_time = bus_id * ceil(timestamp / bus_id) - timestamp
print(bus_id * wait_time)
