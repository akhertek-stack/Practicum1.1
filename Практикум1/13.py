cm = float(input())
total_inches = cm / 2.54
total_feet = total_inches / 12
total_yards = total_feet / 3
total_miles = total_yards / 1760
print(f"Ярды: {total_yards:.2f}")
print(f"Мили: {total_miles:.2f}")
print(f"Футы: {total_feet:.2f}")
print(f"Дюймы: {total_inches:.2f}")