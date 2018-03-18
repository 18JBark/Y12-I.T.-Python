print('Lower-Case only')

V = 0.00015

r = input('Gender: M or F? ')
if r == ('m'):
    r = 0.68
elif r == 'f':
    r = 0.55
else:
    print('M or F!')
    exit(0)

W = input('Kilograms(Kg) or pounds(Lbs)? ')
if W == 'kg':
    W = input('Your mass? ')
    W = W*1000
if W == 'lbs':
    W = input('Your mass? ')
    W = int(W)
    W = W*453.592

t = input('How long ago did you commence drinking(hours)? ')


A = int(input('Number of drinks consumed? '))
A = A*10

A = float(A)
r = float(r)
W = float(W)
V = float(V)
t = float(t)

BAC = float(A/(r*W)*100-(V*t))
print("BAC is", BAC)

drive = input('Learner(L), Probationary(P) or Full(FL)? ')

if drive == 'l' or 'p':
    if BAC > 0:
        print('You will have your licence cancelled for three months and will be required to install an alcohol interlock for at least six months once you are relicensed ')

if drive == 'fl':
    if BAC >= 0.05 and BAC <= 0.07:
        print('You will be fined and recieve 10 demerit points')

    if BAC > 0.07:
        print('You will have your licence cancelled and will be required to install an alcohol interlock for at least six months once you are relicensed.')