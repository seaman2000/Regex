import re

demon_names = input().split(', ')

pattern_for_name = r'[^0-9\+\-\*\/.]'
pattern_for_damage = r'[+\-]*\d[\.\d]*'
pattern_for_divide_or_multiply = r'[*]|[/]'
demon_dict = {}

for name in demon_names:
    result = re.findall(pattern_for_name, name)
    demon_health = 0
    demon_dict[]
    for char in result:
        demon_health += ord(char)

    extracted_damage = re.findall(pattern_for_damage, name)
    extracted_damage = [int(damage) for damage in extracted_damage]
    dividers_or_multipliers = re.findall(pattern_for_divide_or_multiply, name)
    damage_sum = sum(extracted_damage)

    for operator in dividers_or_multipliers:
        if operator == "*":
            damage_sum *= 2
        elif operator == "/":
            damage_sum /= 2
    damage_sum, 
for demon in sorted(demon_names):

    print(f"{demon} - {health points} health, {damage points} damage")




