def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # Drop the lowest set bit of x
    return result

def bit(x):
    result = ''
    if (x == 0):
        result = '0'
    while x:
        if (x & 1):
            result = '1' + result
        else:
            result = '0' + result
        x >>= 1
    return result

n = int(input())
#for i in range (1,n+1):
#    print (((10**i-1)//9)**2)


x = bit(n)
print ('bit = ', x)
x = parity(n)
print ('parity = ', x)
