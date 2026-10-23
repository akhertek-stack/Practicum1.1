n, k, m = map(int, input().split())
path1 = abs(k - m)
path2 = n - path1
min_path = min(path1, path2)
print(min_path - 1)