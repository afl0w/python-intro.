# removes all elements from the second set
# that are there in the first one too. 
# 0's should be removed from the list. 
s1 = {'O', 'W', 'O', 'I'}
s2 = {'M', 'G', 'D', 'O', 'Y'}   

s3= s1 - s2 
print(s3)

s4 = s2 - s1
print(s4)

