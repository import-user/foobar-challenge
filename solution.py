def solution(l):
    ones,twos,threes = [],[],[]
    for x in l:
        if x%3 == 1: ones.append(x)
        elif x%3 == 2: twos.append(x)
        else: threes.append(x)
    ones.sort(reverse=True)
    twos.sort(reverse=True)
    
    n1,n2 = len(ones),len(twos)
    if n1 == n2: threes = l
    elif n1 > n2:
        if n2 == 0: n1 = 3*int(n1/3)
        else:
            if (n1-n2)%2 == 1: n1 = n1-1
            else: n2 = n2-1
        threes.extend(ones[:n1])
        threes.extend(twos[:n2])
    else:
        if n1 == 0: n2 = 3*int(n2/3)
        else:
            if (n2-n1)%2 == 1: n2 = n2-1
            else: n1 = n1-1
        threes.extend(ones[:n1])
        threes.extend(twos[:n2])
    threes.sort(reverse=True)
    return "".join([str(x) for x in threes]) if len(threes) else 0
