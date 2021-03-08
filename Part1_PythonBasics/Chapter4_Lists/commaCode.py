def delimit(someList):
    for item in range(len(someList)-1):
        print( someList[item] + ', ' , end = '')
    print('and ' + someList[-1] + '.') 

spam = ['apples', 'bananas', 'tofu', 'cats']
delimit(spam)
