Parametres = input("Input Three Numbers(Add comma after each number) : ")
list = (Parametres.split(','))

a = int(list[0])
b = int(list[1])
c = int(list[2])

def TrueOrFalse(a, b, c):
    counter = 0
    if a == b:
        counter += 1
    if b == c:
        counter += 1
    if c == a:
        counter += 1
    
    if counter > 0:
        return True
    else:
        return False

D = TrueOrFalse(a, b, c)
print(D)
