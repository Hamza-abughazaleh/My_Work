import random

# Two useful variables for creating Cards.
RANKS = (2,3,4,5,6,7,8,9,10,11,12,13,14)
RANKS= [x for pair in zip(RANKS,RANKS,RANKS,RANKS) for x in pair]
random.shuffle(RANKS)
RANKS1 = RANKS[:26]
RANKS2 = RANKS[26:]
print (RANKS1)
print (RANKS2)
size=len(RANKS1)
size2=len(RANKS2)
clueReport=[]
count=0
while clueReport != "CODE CRACKED":
    count+=1
    pops=[]
    if RANKS1[0]==RANKS2[0]:
        if len(RANKS1)<= 4 :
            RANKS2.extend(RANKS1)
        elif len(RANKS2) <= 4:
            RANKS1.extend(RANKS2)
        else:
            for x in range(3):
                pops.append(RANKS1.pop())
                pops.append(RANKS2.pop())
            if RANKS1[0]>RANKS2[0]:
                pops=[RANKS1.pop(0),RANKS2.pop(0)]
                RANKS1.extend(pops)
            else:
                pops=[RANKS1.pop(0),RANKS2.pop(0)]
                RANKS2.extend(pops)
    if RANKS1[0]>RANKS2[0]:
        pops=[RANKS1.pop(0),RANKS2.pop(0)]
        RANKS1.extend(pops)
    else:
        pops=[RANKS1.pop(0),RANKS2.pop(0)]
        RANKS2.extend(pops)
    if len(RANKS1) ==0 or len(RANKS2) == 0:
        clueReport="CODE CRACKED"
    print(RANKS1)
    print(RANKS2)
    print("\n")
print(count)
