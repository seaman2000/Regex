import re

demon_names = re.split(r'\s*,\s*', input())

pattern_for_name = r'[^0-9\+\-\*\/.]'
pattern_for_damage = r'[+-]?\d+(?:\.\d+)?'
pattern_for_divide_or_multiply = r'[*]|[/]'

demon_dict = {}

for name in demon_names:
    result = re.findall(pattern_for_name, name)
    demon_health = 0

    for char in result:
        demon_health += ord(char)

    extracted_damage = re.findall(pattern_for_damage, name)
    extracted_damage = [float(damage) for damage in extracted_damage]
    dividers_or_multipliers = re.findall(pattern_for_divide_or_multiply, name)
    damage_sum = sum(extracted_damage)

    for operator in dividers_or_multipliers:
        if operator == "*":
            damage_sum *= 2
        elif operator == "/":
            damage_sum /= 2
    demon_dict[name] = demon_health, damage_sum

for demon, (health, dmg) in sorted(demon_dict.items()):
    print(f"{demon} - {health} health, {dmg:.2f} damage")




