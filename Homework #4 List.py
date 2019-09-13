MyUniqueList = []
MyLeftOvers = []

while True:
    a = input("Something Unique : ")

    def IfUnique(a):
        if a in MyUniqueList:
            MyLeftOvers.append(a)
            return False
        else:
            MyUniqueList.append(a)
            return True

    b = IfUnique(a)
    
    if b == True:
        print ("True : ",MyUniqueList)
    
    else:
        print("False : ", MyLeftOvers)
    

    
    