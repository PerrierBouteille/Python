mod=str(input("Modèle: "))

prcs=['prcs1_1','prcs1_2','prcs2_1']
prcs_short=[['prcs1_1','59'],['prcs1_2','74'],['prcs2_1','28']]
prcs_bloc=[['prcs1_1','prcs1_2'],['prcs2_1','prcs2_2']]
prcs_prio=[['prcs1_1','medium'],['prcs1_2','lower'],['prcs2_1','hight']]

if(mod.lower() == "fifo"):
    print('FIFO \n----------')
    for i in prcs:
        print(i)
if(mod.lower() == "sjf"):
    print('SFJ \n----------')
    prcs_short.sort(key = lambda x: x[1])
    for i in prcs_short:
        print(i[0])
if(mod.lower() == "round robin"):
    print('Round Robin \n----------')
    for i in prcs_bloc:
        print(i[0])
    for j in prcs_bloc:
        print(j[1])
if(mod.lower() == "prio"):
    x=0
    print('Priority \n----------')
    while prcs_prio != []:
        if(x==len(prcs_prio)):
            x=0
        if(prcs_prio[x][1] == 'hight'):
            print(prcs_prio[x][0])
            prcs_prio.pop(x)
            if(prcs_prio==[]): break
        if(prcs_prio[x][1] == 'medium'):
            print(prcs_prio[x][0])
            prcs_prio.pop(x)
            if(prcs_prio==[]): break
        if(prcs_prio[x][1] == 'lower'):
            print(prcs_prio[x][0])
            prcs_prio.pop(x)
            if(prcs_prio==[]): break
        x+=1




