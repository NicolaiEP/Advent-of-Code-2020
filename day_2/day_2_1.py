with open("day_2/day_2_input.txt") as f:
    policies = tuple(line.split() for line in f.read().splitlines())

valid_passwords = []
for policy in policies:
    lowest, highest = [int(i) for i in policy[0].split("-")]
    letter = policy[1][0]
    if lowest <= policy[2].count(letter) <= highest:
        valid_passwords.append(policy[2])
print(len(valid_passwords))
