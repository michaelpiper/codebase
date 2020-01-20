import math

def rollDice(A):
    count  =[0] * 7
    for i in A:
        count[i] +=1
        min_r = math.inf
    for i in range(1,7):
        rotate = sum(count) - count[i] + count[7-i]
        if rotate < min_r:
            min_r = rotate
    return min_r
A = [1,6,2,3]
result = rollDice(A)
print (result)
    