 #? Write a Python program to count the number 4 in a given list.
def ls(numbers):
    count=0
    for i in numbers:
        if i==4:
            count+=1    
    return count
print(ls([1,4,6,4,7,4,4,5,7,8,9,4,8,9,5,44,2,4,5,6]))

 