[n, m] = list(map(int, input().split() ))
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
 
index1=0
index2=0
result=[]
while index1<n or index2<m:
    if index2>=m:
        result.append(str(nums1[index1]))
        index1+=1
    elif index1>=n:
        result.append(str(nums2[index2]))
        index2+=1
    elif nums2[index2] <= nums1[index1]:
        result.append(str(nums2[index2]))
        index2+=1
    elif nums2[index2] > nums1[index1]:
        result.append(str(nums1[index1]))
        index1+=1
 
print(" ".join(result))  
