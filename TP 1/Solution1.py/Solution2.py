total_seconds = 9875
hour = total_seconds // 3600 
minute = (total_seconds % 3600) // 60
second = total_seconds % 60

print(f"{hour} H - {minute} m - {second} s")