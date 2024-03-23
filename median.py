
numberList = [2, 3, 5, 7, 8]

count = len(numberList)

numberList.sort()

if count % 2 == 0:
    median1 = numberList[count//2]
    median2 = numberList[count//2 - 1]
    median = (median1 + median2)/2
else:
    median = numberList[count//2]

print("Median", median)
