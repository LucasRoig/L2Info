import operator
import itertools
def glouton_rec(n, a, b, c):
    """ a<b<c"""
    r = 0
    if n == 0 :
        return 0
    elif n < a :
        r = -1;
    elif n >=  c:
        r = glouton_rec(n-c, a, b, c)
    elif n >= b :
        r = glouton_rec(n-b, a, b, c)
    else :
        r = glouton_rec(n-a, a, b,c)
    if r != -1:
        r += 1
    return r

def glouton_iter(n,a,b,c):
    """a<b<c"""
    res = 0
    while (n != 0):
        if n<a :
            res = -1
            break
        if n>= c :
            res += 1
            n -= c
        elif n>=b:
            res += 1
            n -= b
        else :
            res += 1
            n -= a
    return res

def glouton_iter2(n,a,b,c):
    res = n // c
    n = (n % c)
    res += n // b
    n = (n % b)
    res += n // a
    n = (n % a)
    if n != 0 :
        res = -1
    return res

def toutes_sommes_n_pieces_iter(n,a,b,c):
    comb = []
    for i in range(0,n+1):
        for j in range(0, n+1):
            for k in range(0, n+1):
                if (i + j + k) == n :
                    li = a*i + b*j + c*k
                    comb.append(li)
    return comb

            
def toutes_sommes_n_pieces(n, a, b, c):
    res = []
    if n == 1 :
        return [a,b,c]
    else :
        prec = toutes_sommes_n_pieces(n-1,a,b,c)
        res.extend(list(map(operator.add,itertools.repeat(a,len(prec)),prec)))
        res.extend(list(map(operator.add,itertools.repeat(b,len(prec)),prec)))
        res.extend(list(map(operator.add,itertools.repeat(c,len(prec)),prec)))
    return set(res)

for i in range(50) :
    if not glouton_rec(i,1,3,9) == glouton_iter2(i,1,3,9):
        print(glouton_rec(i,1,3,9))
        print(glouton_iter2(i,1,3,9))
        print("erreur")
        
print([i for i in toutes_sommes_n_pieces_iter(4,1,3,4) if toutes_sommes_n_pieces_iter(4,1,3,4).count(i) == 2])


