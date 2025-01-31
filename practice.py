import random
def randomarraygenerator(length:int):
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
    






