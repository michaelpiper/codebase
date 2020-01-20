
def findMoviesDuration(d,arr=[],time=30):
    prev=0
    # arr.sort()
    end=len(arr)-1
    max_val=0
    d-=time
    while prev < end:
        if arr[prev]+arr[end]<=d :
            if  max_val < arr[prev]+arr[end] :
                max_val = arr[prev]+arr[end]
                i = prev
                j = end
            prev+=1
        else :
            end-=1
    if end and prev :
        return (arr[i],arr[j])
    else :
        return False
d=250
movies_duration=[90,85,75,60,120,150]
result = findMoviesDuration(d,movies_duration)
print(result)
if result:
    print (result[0]+result[1])
else :
    print ('none found')