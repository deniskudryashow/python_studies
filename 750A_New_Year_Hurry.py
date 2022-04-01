n , k = map(int, input().split())
time_for_contest = 240 - k
cnt = 0
problem_time = 0
for i in range(1,n+1):
    problem_time = problem_time + 5*i
    if problem_time > time_for_contest:
        break
        print(cnt)
    else:
        cnt += 1
print(cnt)
