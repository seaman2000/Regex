import re

number_of_messages = int(input())
first_decrypt_pattern = r'[star]'
between = r'[^@\-\!:>]*?'
second_decrypt_pattern = fr"@\b([A-Za-z]+){between}:(\d+){between}!(A|D)!{between}->(\d+)"
attacked_planets = sorted([])
destroyed_planets = sorted([])

for _ in range(number_of_messages):
    line = input()
    result = re.findall(first_decrypt_pattern, line, re.IGNORECASE)
    subtract_num = len(result)
    first_decrypt_part = ''.join([chr(ord(char) - subtract_num) for char in line])
    second_decrypt_part = re.search(second_decrypt_pattern, first_decrypt_part)
    if second_decrypt_part:
        name, population, attack_type, soldier_count = second_decrypt_part.groups()

print(f"Attacked planets: {len(attacked_planets)}\n")
if attacked_planets:
    for planet in attacked_planets:
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if destroyed_planets:
    for planet in destroyed_planets:
        print(f"-> {planet}")