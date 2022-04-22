n = int(input())
numbers = set(range(1, n+1))
rest = numbers
while True:
    guess = input()
    if guess == "HELP":
        break
    guess = set(map(int, guess.split()))
    if len(guess&rest) > int((len(rest)/2)):
        print("YES")
        rest &= guess
    else:
        print("NO")
        rest -= guess
print(*sorted(rest))
    
