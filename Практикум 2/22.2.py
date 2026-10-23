import math

n, k, m = map(int, input().split())
total_rides = n * 2
sessions = math.ceil(total_rides / k)
total_time = sessions * m
print(total_time)