with open ("input.txt", 'r', encoding = 'utf=8') as f:
    lines = f.read().split()
    cnt = {}
    for word in lines:
        cnt[word] = cnt.get(word,0) + 1
    print(max(sorted(cnt), key = cnt.get))