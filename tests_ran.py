import pytest
from practice import randomarraygenerator,main


# test for missing parameters
def testmissparameter():
    with pytest.raises(TypeError):
        randomarraygenerator() #no parameter passed


#test for extra parameters
def testextraparameter():
    with pytest.raises(TypeError):
        randomarraygenerator(0,8,90) #3 parameters present


#test for incorrect parameter type
def testincorrectpar():
    with pytest.raises(TypeError):
        randomarraygenerator("hundred")


#test for zero length parameter
def testzerolength():
    with pytest.raises(ValueError):
        randomarraygenerator(0)


#test for checking the return type of function
def testrandom():
    x=randomarraygenerator(10)
    assert isinstance(x,list)


#test for checking whether list lenght matches the expected length parameter
def testlengthcheck():
    x=randomarraygenerator(10)
    assert len(x)==10
    x=randomarraygenerator(50)
    assert len(x)==50


#test to check the elements in the array is within the range of 0 to 50
def testnumrange():
    result=randomarraygenerator(100)
    assert all(0<=i<=50 for i in result),"elements should be in the range of 0 to 50"


#test to check whether the frequency of elements are matching with actual count
def testfreqcheck():
    result=randomarraygenerator(100)
    frequency=main(result)
    assert all(result.count(num)==frequency[num] for num in result)