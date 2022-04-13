with open ('C:/Users/danku/dz/dz_hashtables/input.txt') as f:
    lines = f.readlines()
    words = set()
    for i in range(len(lines)):
        words = words | set(lines[i].split())
    print(len(words))
    
