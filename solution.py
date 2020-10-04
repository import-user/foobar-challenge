def solution(n):
    s = ""
    for i in range(2,30000):
        for j in range(2, int(math.sqrt(i)+1)):
            if i%j == 0:
                break
        else:
            s += str(i)
        if len(s) > 100000:
            break
    return s[n:n+5]
