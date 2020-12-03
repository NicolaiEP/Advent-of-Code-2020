with open("day_2/day_2_input.txt") as f:
    policies = tuple(line.split() for line in f.read().splitlines())

valid_passwords = []
for policy in policies:
    first, second = [int(i) - 1 for i in policy[0].split("-")]
    letter = policy[1][0]
    if (policy[2][first] == letter) != (policy[2][second] == letter):
        valid_passwords.append(policy[2])
print(len(valid_passwords))
