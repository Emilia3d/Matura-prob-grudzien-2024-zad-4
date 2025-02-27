
wiersze=open('prostokaty.txt','r').readlines()

prostokaty=[]
for wiersz in wiersze:
    wiersz=list(map(int, wiersz.split(' ')))
    prostokaty.append(wiersz)

#print(prostokaty)

#4.1
lista_4_1=[]

for h,s in prostokaty:
    lista_4_1.append(h*s)

print(min(lista_4_1),max(lista_4_1))

#4.2
akt_dl, maks_dl,akt_pocz, maks_pocz=1,1,0,0

for i in range(len(prostokaty) - 1):
    #h1 =prostokaty [i][0]
    #h2=prostokaty[i+1][0]
    #s1 =prostokaty [i][1]
    #s2=prostokaty[i+1][1]
    h1, s1=prostokaty[i]
    h2, s2 = prostokaty[i+1]

    if h2<=h1 and s2<=s1:
        akt_dl+=1
        if akt_dl>maks_dl:
            maks_dl=akt_dl
            maks_pocz=akt_pocz
    else:
        akt_dl=1
        akt_pocz=i

print(maks_dl,prostokaty[maks_pocz+maks_dl])
#4.3
wysokosci = []
for h, s in prostokaty:
    if h not in wysokosci:
        wysokosci.append(h)
print(wysokosci)

szerokosci = [[] for _ in range(len(wysokosci))] #utworzenie pustych list dla szerokosci

for i in range(len(wysokosci)): #wypełnienie list szerokościami dla danej wysokosci
    h1 = wysokosci[i]
    for h, s in prostokaty:
        if h == h1:
            szerokosci[i].append(s)

for i in range(len(szerokosci)):
    szerokosci[i].sort(reverse=True)
    print (szerokosci[i])
    
#suma szer dla 2,3 i 5 pierwszych prostokatow (posortowalismy od najwiekszego)
suma2s=0
for i in range(len(szerokosci)):
    if len(szerokosci[i]) >= 2:
        if szerokosci[i][0]+szerokosci[i][1]>suma2s:
            suma2s=szerokosci[i][0]+szerokosci[i][1]
print(suma2s)

suma3s=0
for i in range(len(szerokosci)):
    if len(szerokosci[i]) >= 3:
        if szerokosci[i][0]+szerokosci[i][1]+szerokosci[i][2]>suma3s:
            suma3s=szerokosci[i][0]+szerokosci[i][1]+szerokosci[i][2]
print(suma3s)

suma5s=0
for i in range(len(szerokosci)):
    if len(szerokosci[i]) >= 5:
        if szerokosci[i][0]+szerokosci[i][1]+szerokosci[i][2]+szerokosci[i][3]+szerokosci[i][4]>suma5s:
            suma5s=szerokosci[i][0]+szerokosci[i][1]+szerokosci[i][2]+szerokosci[i][3]+szerokosci[i][4]
print(suma5s)
