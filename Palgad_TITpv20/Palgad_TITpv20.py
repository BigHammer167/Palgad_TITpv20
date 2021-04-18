palk=[1060,50,340,1200,1060,50,1600,1060]
inimesed=["A","B","C","D","E","A","D",'F']


def palgad(p,i):
##    print(palk)
##    print(inimesed)
    n=len(inimesed)
    print("Добавить человека и зарплату - add")
    print("Удалить человека и зарплату - del")
    print('Максимальная зарплата и кто её получает - max')
    print('Минимальная зарплата и кто её получает - min')
    print('Сортировка зарплат по возрастанию - sort')
    print('Сортировка зарплат по убыванию - sort1')
    print("Кто получает одинаковые зарплаты? - odin")
    print('Поиск зарплаты по имени человека - nimi')
    print("У кого зарплата больше/меньше заданной? - bmz")
    print("Top3 (3 самых богатых и 3 самых бедных) - top")
    print("Вывод заданного количества самых высоких зарплат - top_max")
    print("Средняя зарплата - k")
    print("Нетто-зарплата - netto")
    print("Сортировка по имени - sort_n")
    print("Удаление данных тех, чья зарплата ниже средней - del_k")
    
    

    print()
    valik=input("Ваш выбор? => ")
    
    ## Добавить человека и зарплату
    if valik=="add":                                        
        i=adding(palk,inimesed)
        print("Обновлённые списки: ")
        print(inimesed)
        print(palk)
        print("Добавлен элемент", inimesed[-1])
        print("С зарплатой", str(palk[-1])+'€')

    ## Удалить человека и зарплату
    elif valik=="del":                                       
        p,i=delete(palk,inimesed,n)
        print(palk,inimesed)
        if n==0:
            print("Пустой список")
        else:
            n = len(inimesed)
            for i in range(n):
                print(inimesed[i],"получает", str(palk[i])+'€')

    ## Максимальная зарплата и кто её получает
    elif valik=="max":
        max_palk,kellel,nr=maksimum(palk,inimesed)
        print("Максимальную зарплату", str(max_palk)+'€', "получает",str(nr)+'-й человек из списка -',kellel)

    ## Минимальная зарплата и кто её получает
    elif valik=="min":
        min_palk,kellel,nr=minimum(palk,inimesed)
        print("Минимальную зарплату", str(min_palk)+'€', "получает",str(nr)+'-й человек из списка -',kellel)

    ## Сортировка зарплат по возрастанию
    elif valik=="sort":
        p,ini=sorteerimine(palk,inimesed,n)
        for i in range(n):
            print(ini[i],"получает", str(p[i])+'€')

    ## Сортировка зарплат по убыванию
    elif valik=="sort1":
        p,ini=sorteerimine(palk,inimesed,n)
        p.reverse()
        ini.reverse()
        for i in range(n):
            print(ini[i],"получает", str(p[i])+'€')

    ## Кто получает одинаковые зарплаты?
    elif valik == 'odin':
        print("Одинаковые зарплаты получают")
        odinakovyje_zarplaty(palk, inimesed,n)    ## вызов соответствующей функции пользователя

    ## Поиск зарплаты по имени человека
    elif valik=="nimi":
        ots_nimi,ots_palk,nr=nimi(palk,inimesed,n)
        if len(ots_nimi) == 0:
            print("Данные этого человека отсутствуют")
        else:
            for i in range(len(ots_nimi)):
                print(str(nr[i])+'-й человек в списке с именем -',ots_nimi[i],"получает", str(ots_palk[i])+'€')

    ## У кого зарплата больше/меньше заданной?
    elif valik=='bmz':
        pal, ini, valik = bolshe_menshe_zadannoi(palk, inimesed,n)
        print("Получают", valik)
        if len(pal) == 0:
            print("Таких данных нет")
        else:
            for i in range(len(pal)):
                print(pal[i],'получает',ini[i])

    ## Top3 (3 самых богатых и 3 самых бедных)
    elif valik == 'top':
        bog, bog_p, bed, bed_p = top3(palk,inimesed,n)
        print("3 самых богатых")
        for i in range(3):
            print(bog[i],'получает',str(bog_p[i])+'€')
        print()
        print("3 самых бедных")
        for i in range(3):
            print(bed[i],'получает',str(bed_p[i])+'€')
            
    ## Вывод заданного количества самых высоких зарплат
    elif valik=="top_max":
        topbogat(palk,inimesed,n)

    ## Средняя зарплата
    elif valik=="k":
        kesk_palk=round(keskmine(palk,n),2)
        print("Средняя зарплата",str(kesk_palk)+'€')

    ## Нетто-зарплата
    elif valik == 'netto':
        netto = netto_palk(palk,n)
        for i in range(n):
            print(inimesed[i],"получает нетто-зарплату", str(netto[i])+'€')

    ## Сортировка по имени
    elif valik == 'sort_n':
        p,i=nimi_sort(palk,inimesed,n)
        for i in range(n):
            print(inimesed[i],"получает", str(palk[i])+'€')

    ## Удаление данных тех, чья зарплата ниже средней
    elif valik == 'del_k':
        p,i=alla_keskmist_kustuta(palk,inimesed,n)
        print("Новые списки: удалены данные, где зарплата ниже средней")
        for i in range(len(p)):
            print(inimesed[i],"получает", str(palk[i])+'€')
        
    ## Во всех остальных случаях
    else:
        print("Вы сделали неправильный выбор")



##############################################################
def adding(palk,inimesed):
    add=input("Кого добавить? (введите имя) => ")
    inimesed.append(add)
    add_zp=int(input("Какая у него зарплата? => "))
    palk.append(add_zp)
    return palk,inimesed
#############################################################
def delete(palk, inimesed,n):
    x=input("Удаляем по номеру или по имени? (nr/nm) => ")
    if x=="nr":
        nr=int(input("Введи номер (максимум "+str(len(palk))+ ') => '))
        if nr > n:
            print("Такого номера нет в списке!")
        else:
            palk.pop(nr-1)
            inimesed.pop(nr-1)
    elif x=="nm":
        keda=input("Введите имя => ")
        if inimesed.count(keda)==0:
            print("Данные такого человека отсутствуют!")
        else:
            i=0
            while i < n:
                if keda==inimesed[i]:
                    inimesed.pop(i)
                    palk.pop(i)
                    n=len(inimesed)
                else:
                    i+=1
    return palk, inimesed
#############################################################
def maksimum(palk,inimesed):
    max_palk=palk[0]       
    kellel=inimesed[0]      
    for p in palk:          
        if p > max_palk:      
            max_palk=p       
            nr=palk.index(max_palk)   
            kellel=inimesed[nr]      
    return max_palk, kellel,nr+1  
#############################################################
def minimum(palk,inimesed):
    min_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p < min_palk:
            min_palk=p
            nr=palk.index(min_palk)
            kellel=inimesed[nr]
    return min_palk, kellel,nr+1  
#############################################################
def sorteerimine(palk,inimesed,n):
    abi_p = 0
    abi_i = ""
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
#############################################################
def odinakovyje_zarplaty(palk, inimesed,n):
    odin_p =[palk[i] for i in range(n) if palk.count(palk[i])>1]   
    odin_p_i =[inimesed[i] for i in range(n) if palk.count(palk[i])>1] 
    odin_p_s, odin_p_i_s = sorteerimine(odin_p,odin_p_i,len(odin_p))   
    for i in range(len(odin_p_s)):
        print(odin_p_i_s[i],'получает',str(odin_p_s[i])+'€',) 
#############################################################
def nimi(palk,inimesed,n):
    ots_nimi=[]   ## otsitav nimi - искомое имя
    ots_palk=[]
    nr=[]
    palk_keda=0
    keda=input("Введи имя => ")
    for j in range(n):
        if inimesed[j]==keda:
            palk_keda=palk[j]
            ots_nimi.append(inimesed[j])
            ots_palk.append(palk_keda)
            nr.append(j+1)
        else:pass
    return ots_nimi,ots_palk,nr
############################################################
def bolshe_menshe_zadannoi(palk, inimesed,n):
    valik = input("Введите знак и зарплату (например: <1500) => ")
    ini = []; pal = [];zadano = float(valik[1:len(valik)])
    if valik[0] == '<':
        for i in range(n):
            if palk[i] < zadano:
                pal.append(palk[i])
                ini.append(inimesed[i])    
    elif valik[0] == '>':
        for i in range(n):
            if palk[i] > zadano:
                pal.append(palk[i])
                ini.append(inimesed[i])
    return pal, ini, valik           
############################################################
def top3(palk, inimesed,n):
    bog_i = []; bog_p = []
    bed_i = []; bed_p = []
    p,ini=sorteerimine(palk,inimesed,n)
    for i in range(3):
        bed_i.append(ini[i])
        bed_p.append(p[i])
        bog_i.append(ini[n-1-i])
        bog_p.append(p[n-1-i])
    return bog_i, bog_p, bed_i, bed_p
###########################################################
def topbogat(palk,inimesed,n):
    top,inimes=sorteerimine(palk,inimesed,n)
    k = int(input("Сколько самых высоких зарплат вывести: максимум " +str(len(palk))+ ' => ' ))
    if k > len(palk):
        print("Вы ввели неверное значение!")
    else:
        palk.reverse()
        inimesed.reverse()
        for i in range(0,k,1):
            print(palk[i], 'получает',inimesed[i])
###########################################################
def keskmine(palk,n):
    summa=0
    for p in palk:
        summa+=p
    kesk=summa/n
    return kesk
##########################################################
def netto_palk(palk,n):
    netto = []
    for i in range(n):
        if palk[i] <= 1200:       
            mv = 500             
            if palk[i] < mv:     
                mv = palk[i]     
        elif 1201 <= palk[i] <= 2099:
            mv = 500 - 0.55556 * (palk[i]-1200)  
        else:
            mv = 0               
        netto.append(round(mv + (palk[i] - mv) * 0.8,2))
    return netto
##########################################################
def nimi_sort(palk,inimesed,n):
    abi_p = 0
    abi_i = ""
    for i in range(0,n-1):
        for j in range(i+1,n):
            if inimesed[i]>inimesed[j]:
                abi_i=inimesed[i]
                inimesed[i]=inimesed[j]
                inimesed[j]=abi_i
                abi_p=palk[i]
                palk[i]=palk[j]
                palk[j]=abi_p
    return palk,inimesed
##########################################################
def alla_keskmist_kustuta(palk,inimesed,n):
    uus_palk = []; uus_inimesed = []
    kesk = keskmine(palk,n)
    for p in palk:
        if p > kesk:
            nr = palk.index(p)
            uus_palk.append(p)
            uus_inimesed.append(inimesed[nr])
    palk.clear();inimesed.clear()
    for i in range(len(uus_palk)):
        palk.append(uus_palk[i])
        inimesed.append(uus_inimesed[i])
    return uus_palk, uus_inimesed
##########################################################

while True:
    palgad(palk,inimesed)
    print()
