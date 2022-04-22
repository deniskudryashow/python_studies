n = int(input())
hours = str((n // 3600) % 24)
minutes = str((n // 60) % 60)
seconds = str(n % 60)
if len(minutes) < 2:
    minutes = "0" + minutes
if len(seconds) < 2:
    seconds = "0" + seconds
print(hours + ":" + minutes + ":" + seconds)

