##def printTable(tableData,colWidths):
##    colWidths = [0] * len(data)
##    for data in tableData:
##        for item in data:
##            longestString = max(item,key = len)
##            count = 0
##            while count <= len(colWidths):
##                colWidths.insert(longestString,count)
##                count += 1
##
##    colWidth.sort()
##    rightJustify = colWidth[-1]
##    
##
##tableData = [['apples', 'oranges', 'cherries', 'banana'],
## ['Alice', 'Bob', 'Carol', 'David'],
## ['dogs', 'cats', 'moose', 'goose']]
##
##printTable(tableData,6)
            
def printLongestString(tableData):
    for data in tableData:
        for item in data:
            longestString = len(max(data,key = len))
        count = 0
        stringLengths = [0] * (len(tableData)-1)
        stringLengths.insert(count, longestString)
        count += 1

    print(stringLengths)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

printLongestString(tableData)
