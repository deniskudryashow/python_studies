with open ("input.txt", 'r', encoding = 'utf=8') as f:
    lines = f.read().splitlines()
    words = set()
    for i in range(len(lines)):
        # if not (97 <= ord(lines[i][-1]) <= 122 or 65 <= ord(lines[i][-1]) <= 90):
        #     lines[i] = lines[i][0:-1]
            words.update(lines[i].split())
    print(len(words))