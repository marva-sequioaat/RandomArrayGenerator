""""this file contain function to find the frequency of elements present in a array of size 100 containing random elements between 0 and 50"""
import random
def randomarraygenerator(length:int):
    """this function generate an array with random element between 0 and 50 of size length"""
    i=0
    arr=[]
    if length==0:
        raise ValueError("The 'length' parameter must be greater than zero.")
    while i<length:
        x=random.randint(0,50)
        arr.append(x)
        i+=1
      
    return arr

def main(array1):
    """This is the main function which count the frequency of  each element in a array"""  
    temp={}
    for i in array1:
        if i not in temp.keys():
            temp[i]=1
        else:
            temp[i]+=1
    print(temp)
    return temp
if __name__=="__main__":
    array1=randomarraygenerator(100)
    main(array1)
    






