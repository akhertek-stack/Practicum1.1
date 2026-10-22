seconds = int(input())
hours = seconds // 3600
min = (seconds % 3600) // 60
sec = seconds % 60
print(f"{hours}:{min}:{sec}")