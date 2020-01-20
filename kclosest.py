import math
def sortPoints(InputList):
    # Selection Sort
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
        # Compare the current element with next one	
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
    return InputList
def kNearest(points, input,k=3):
    [m,n] = input
    result=[]
    tem=[]
    variable={}
    for i in points:
        [p,q] = i  
        sqrt=math.sqrt(((m-p)*(m-p))+((n-q)*(n-q)))
        tem.append(sqrt)
        variable[sqrt]=i
    sortPoints(tem)
    for j in tem:
        if len(result)>k-1:
            break
        result.append(variable[j])
    return result

input = [0,0]
post_offices = [[-16,5],[-1,2],[4,3],[10,-2],[0,3],[-5,-9]]
result= kNearest(post_offices,input)
print (result)