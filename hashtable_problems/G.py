n = int(input())
numbers = set(range(1, n+1))
while True:
    guess = input()
    if guess == "HELP":
        break
    guess = set(map(int, guess.split()))
    answer = input()
    if answer == "YES":
        numbers = numbers & guess
    else:
        numbers = numbers - guess
print(numbers)