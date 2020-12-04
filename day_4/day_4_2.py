import re

with open("day_4/day_4_input.txt") as f:
    passports = [tuple(passport.split()) for passport in f.read().split("\n\n")]


def data_validate(passport):
    passport = {k: v for k, v in (field.split(":") for field in passport)}
    valid_byr = 1920 <= int(passport["byr"]) <= 2002
    valid_iyr = 2010 <= int(passport["iyr"]) <= 2020
    valid_eyr = 2020 <= int(passport["eyr"]) <= 2030

    hgt = passport["hgt"]
    if 5 == len(hgt) and hgt[-2:] == "cm":
        valid_hgt = 150 <= int(hgt[:3]) <= 193
    elif 4 == len(hgt) and hgt[-2:] == "in":
        valid_hgt = 59 <= int(hgt[:2]) <= 76
    else:
        valid_hgt = False

    valid_hcl = re.fullmatch(r"#[0-9a-f]{6}", passport["hcl"]) is not None
    valid_ecl = passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    valid_pid = len(passport["pid"]) == 9 and passport["pid"].isdigit()

    return all((valid_byr, valid_iyr, valid_eyr, valid_hgt, valid_hcl, valid_ecl, valid_pid))


required = {"iyr", "eyr", "byr", "pid", "hgt", "ecl", "hcl"}
valid_by_requirements = {p for p in passports if {field.split(":")[0] for field in p} - {"cid"} == required}
print(sum(data_validate(p) for p in valid_by_requirements))
