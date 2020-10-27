msg = "Hello World"
print(msg)

testArray = ['strOne', 'strTwo', 'strThree']
print(testArray)

testObj = {'strFour', 'strFive', 'strSix'}
print(testObj)

def loopTest(container):
    for string in container:
        print(letterCounter(string))
        
def letterCounter(string):
    letterCount = len(string)
    print(letterCount)

loopTest(testArray)

loopTest(testObj)