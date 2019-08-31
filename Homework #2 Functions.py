def OldTownRoad(a):
    a = "Old Town Road"
    return a
def Genre(b):
    b = "Country Song"
    return b
def YearRealeased(c):
    c = "Year Realeased : 2019"
    return c

Question = input("A = Name, B = Genre or C = Year Realeased: ")
a, b, c = "0", "0", "0"
if Question == ("A"):
    A = OldTownRoad(a)
    print(A)
if Question == ("B"):
    B = Genre(b)
    print(B)
if Question == ("C"):
    C = YearRealeased(c)
    print(C)



