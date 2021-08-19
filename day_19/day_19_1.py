from itertools import product

with open("day_19/day_19_input.txt") as f:
    lines = f.read().splitlines()
    split_point = lines.index("")
    rules = dict((key.strip(), value.strip(" \"")) for key, value in
                 (rule.split(":") for rule in lines[:split_point]))
    messages = lines[split_point + 1:]


def find_valid_messages(rule_text):
    valid_messages = []
    if rule_text in ("a", "b"):
        valid_messages.append(rule_text)

    elif "|" in rule_text:
        for subtext in rule_text.split(" | "):
            valid_messages.extend(find_valid_messages(subtext))

    else:
        valid_messages.extend(["".join(element) for element in product(
            *[find_valid_messages(rules[sub_rule]) for sub_rule in rule_text.split()])])
    return valid_messages


print(len(set(find_valid_messages("0")).intersection(set(messages))))
