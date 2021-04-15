palk=[1200,2500,750,395,1200]
inimesed=["A","B","C","B","E"]
def palgad(p,i):
    print(palk)
    print(inimesed)
    print("Keskmine - k, Minimum - min, Maksimum -max, Otsing -nimi, Sorteerimine -sort")
    print("Delete - del")# Список того, что можно сделать
    print("Top - top_max")
    print("Odinakovie_zarplati - odinak")
    valik=input("Valik-...")
    if valik=="k": 
        kesk_palk=round(keskmine(palk),2)
        print("Keskmine palk on ",kesk_palk)
    elif valik=="min": 
        min_palk,kellel=minimum(palk,inimesed)
        print("Minimaalne palk ", min_palk, " saab kätte ",kellel)
    elif valik=="max":
        max_palk,kellel=maksimum(palk,inimesed)
        print("Maksimaalne palk ", max_palk, " saab kätte ",kellel)
    elif valik=="nimi":
##        pk=nimi(palk,inimesed)
##        print(pk)
        ots_nimi,ots_palk=nimi(palk,inimesed)
        for i in range(len(ots_nimi)):
            print(ots_nimi[i]," saab kätte   ", ots_palk[i])
    elif valik=="sort": 
        p,i=sorteerimine(palk,inimesed)
        for i in range(len(inimesed)):
            print(inimesed[i]," saab kätte   ", palk[i])
    elif valik=="del":
        p,i=delete(palk,inimesed)
        print(palk,inimesed)
        if len(inimesed)==0:
            print("Tüli list")
        else:
            for i in range(len(inimesed)):
                print(inimesed[i]," saab kätte   ", palk[i])
    elif valik=="add":
        i=adding(palk,inimesed)
        print(palk,inimesed)

    elif valik=="top_max":
        p, i=topbogat(palk,inimesed)
    elif valik=="odinak":
        odinakovie_zarplati(palk,inimesed)
        

def topbogat(palk,inimesed):#Выводит на экран значение топа
    top,inimes=sorteerimine(palk,inimesed)
    maks=len(palk)
    k= int(input("Выберите значение топ (максимально "+str(maks)+")"))

    palk.reverse()
    inimesed.reverse()

    for i in range(0,k,1):
        print(palk[i])
        print(inimesed[i])
    return palk, inimesed
 

def adding(palk,inimesed):#Добавляет еще несколько человек и зарплат(кол-во говорит пользователь)
    add=input("Кого добавить??? ")
    inimesed.append(add)
    add_zp=int(input("Какая зарплата???"))
    palk.append(add_zp)
    return palk,inimesed

def delete(palk, inimesed):#Удаляет человека и его зарплату
    x=input("name or number")
    if x=="number":
        i=int(input("Chose number"))
        palk.pop(i-1)
        inimesed.pop(i-1)
    elif x=="name":
        i=0
        keda=input("Write the name =>")
        n=len(inimesed)
        while i<n:
            if keda==inimesed[i]:
                inimesed.pop(i)
                palk.pop(i)
                n=len(inimesed)
            else:
                i+=1
            
    
    return palk, inimesed
            
        
def sorteerimine(palk,inimesed):#Упорядочивает зарплаты в порядке возрастания и убывания вместе с именами
    abi_p=0
    abi_i=""
    n=len(inimesed)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if palk[i]>palk[j]:
                abi_p=palk[i]
                palk[i]=palk[j]
                palk[j]=abi_p
                abi_i=inimesed[i]
                inimesed[i]=inimesed[j]
                inimesed[j]=abi_i
    return palk,inimesed


def nimi(palk,inimesed):#Показывает зарплату человека, которого вы написали
    ots_nimi=[]
    ots_palk=[]
    palk_keda=0
    keda=input("Sisesta nimi... ")
    n=len(inimesed)
    for j in range(n):
        if inimesed[j]==keda:
##            palk_keda=palk[j]
##            break
            ots_nimi.append(inimesed[j])
            ots_palk.append(palk[j])
        else: pass
            #palk_keda='ei ole'
    return ots_nimi, ots_palk

def maksimum(palk,inimesed):#Показывает самую большую зарплату и кто ее получает
    max_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p>max_palk:
            max_palk=p
            i=palk.index(max_palk)
            kellel=inimesed[i]
    return max_palk, kellel   

def minimum(palk,inimesed):#Кто получает самую маленькую зарплату и какую именно 
    min_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p<min_palk:
            min_palk=p
            i=palk.index(min_palk)
            kellel=inimesed[i]
    return min_palk, kellel   
    
def keskmine(palk):
    summa=0
    n=len(palk)
    for p in palk:
        summa+=p
    k=summa/n
    return k


   
def odinakovie_zarplati(palk,inimesed):#Узнаёт, кто получает одинаковую зарплату
    odinak=[]
    for i in range(len(palk)):
        p=palk[i]
        for j in range(len(palk)):
            if palk [i]==palk[j] and i!=j:
                odinak.append(inimesed[j])
    print("Võrdsed palgad saavad",odinak[1],"ja",odinak[0])


while True:
    palgad(palk,inimesed)
