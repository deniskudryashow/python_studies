with open ("input.txt", 'r', encoding = 'utf=8') as f:
    lines = f.read().split()
    cnt = {}
    for word in lines:
        cnt[word] = cnt.get(word,0) + 1
    res = dict((v, k) for k, v in cnt.items())
    for i in range(1,len(res)+1):
        print(sorted(res.items())[-i][1])