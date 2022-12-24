'''
    All the math tools needed are included here
'''

def isTrue(x): 
    '''
        judge whether x is equal to 1
    '''
    return x == 1

def if_(i, y, z):
    '''
        choose between y and z: choose y when i is 1, otherwise, choose z 
    '''
    return y if isTrue(i) else z

def and_(i, j): 
    '''
        and gate(i, j)
    '''
    return if_(i, j, 0)

def AND(i, j): 
    '''
        AND gate(i,j) (operating and gates on all elements)
    '''
    return [and_(ia, ja) for ia, ja in zip(i,j)] 

def not_(i):
    '''
        not gate
    ''' 
    return if_(i, 0, 1)

def NOT(i):
    '''
        NOT gate (operating not gate on all elements)
    ''' 
    return [not_(x) for x in i]

def xor(i, j):
    '''
        xor gate
    ''' 
    return if_(i, not_(j), j)

def XOR(i, j): 
    '''
        operating xor on all elements
    '''
    return [xor(ia, ja) for ia, ja in zip(i, j)]

def xorxor(i, j, l): 
    '''
        tripple xor gate
    '''
    return xor(i, xor(j, l))

def XORXOR(i, j, l): 
    '''
        operating tripple xor on all elements
    '''
    return [xorxor(ia, ja, la) for ia, ja, la, in zip(i, j, l)]

# def maj(i,j,k): 
#     return max([i,j,], key=[i,j,k].count)

def rotr(x, n): 
    '''
        right circular shift
    '''
    return x[-n:] + x[:-n]

def shr(x, n): 
    '''
        right shift (zero padding)
    '''
    return n * [0] + x[:-n]

def _add(i,j,k):
    '''
        add for a single bit
    '''
    tmp = [i,j,k].count(1)
    if tmp == 0:
        return 0,0
    elif tmp == 1:
        return 1,0
    elif tmp == 2:
        return 0,1
    else:
        return 1,1

def add(i,j):
    '''
        operating binary add
    '''
    if len(i) > len(j):
        length = len(i)
        padding = [0] * (len(i)-len(j))
        j = padding + j
    else:
        length = len(j)
        padding = [0] * (len(j)- len(i))
        i = padding + i

    res = [0]*length
    tmp = [0]*(length + 1)

    for k in range(length):
        res[length - k - 1],tmp[length - k - 2] = _add(i[length - k - 1],j[length - k - 1],tmp[length - k - 1])
    return res
    

if __name__ == '__main__':
    res = add([1,0,1,0,0,1,1],[0,1,0,0,1,1,0])
    breakpoint()
    print('finished!')