starting_numbers = [int(n) for n in "0,3,1,6,7,5".split(",")]
number_dict = {n: turn for turn, n in enumerate(starting_numbers, start=1)}
last_spoken = starting_numbers[-1]
turn = len(starting_numbers)
while turn < 30000000:
    if last_spoken in number_dict:
        now_spoken = turn - number_dict[last_spoken]
    else:
        now_spoken = 0
    number_dict[last_spoken] = turn
    last_spoken = now_spoken
    turn += 1

print(last_spoken)
