n = int(input())
numbers = set(range(1, n+1))
while True:
    guess = input()
    if guess == "HELP":
        break
    guess = set(map(int, guess.split()))
    answer = input()
    if answer == "YES":
        numbers &= guess
    else:
        numbers -= guess
print(*sorted(list(numbers)))



