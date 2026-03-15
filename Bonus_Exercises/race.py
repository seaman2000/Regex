import re

pattern_for_name = r"[A-Za-z]"
pattern_for_numbers = r"\d"

participants = input().split(', ')
line = input()
run_distance_and_name = {}

while line != "end of race":
    found_name = re.findall(pattern_for_name, line)
    found_name = ''.join(found_name)

    if found_name in participants:
        distance = re.findall(pattern_for_numbers, line)
        if distance:
            distance = [int(meters) for meters in distance]
            if found_name in run_distance_and_name.keys():
                run_distance_and_name[found_name] += sum(distance)
            else:
                run_distance_and_name[found_name] = sum(distance)

    line = input()

run_distance_and_name = sorted(run_distance_and_name)
for name in run_distance_and_name:
    print(f"first place: {name}")

