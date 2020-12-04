with open("day_4/day_4_input.txt") as f:
    passports = tuple(passport.split() for passport in f.read().split("\n\n"))

required = {"iyr", "eyr", "byr", "pid", "hgt", "ecl", "hcl"}
print(sum({field.split(":")[0] for field in p} - {"cid"} == required for p in passports))
