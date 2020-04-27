##
def twoSum1(nums, target):
    mydict = {}
    indexlist = []
    for (i,v) in enumerate(nums):
        compliment = target - v
        if compliment not in mydict:
            mydict[v] = i
        else:
            indexlist.extend([i,mydict[compliment]])
    return(indexlist)



nums=[1,2,3,4,6,7,5]
target=8
twoSum1(nums,target)

##
