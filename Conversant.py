import statistics

def parse():
    a=input("Please enter a data center letter: ")
    a=a.lower()
    dc="dc="+a
    numList=[]
    timeList=[]
    file=open("data.Montoya.txt","r")
    lines=file.readlines()
    file.close()
    for line in lines:
        wordList=line.lower().split()
        number=wordList[2]
        time=wordList[1]
        if (dc in wordList):
            numList.append(number)
            timeList.append(time)
            #print("DC=A",wordList)
    numList=[float(i) for i in numList]
    avg=statistics.mean(numList)
    #numList.sort()
    #print (timeList)
    #print (numList)
    res2=statistics.median(numList)
    outliers=outlier(numList,timeList,avg)
    print("Average= ",avg)
    print ("Median= ", res2)
    '''print (outliers)'''    
    return

def mean(aList):
    return float(sum(aList)) / max(len(aList), 1)
    
def outlier(numList,timeList,avg):
   outliers={}
   for each in numList:
        t=timeList[numList.index(each)]
        if (each < avg/3):
            outliers[t]=each
            print("OUTLIER(-): " , "Time" ,t,"|","Data", each)
            '''figure this out'''
        if(each > avg*3):
            outliers[t]= each
            print("OUTLIER(+): " , "Time" ,t, "|", "Data", each)
   return outliers
