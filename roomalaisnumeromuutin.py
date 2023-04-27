from itertools import islice
import collections
def consume(iterator, n):
    #pöllitty lol
    #https://stackoverflow.com/questions/17837316/how-do-i-skip-a-few-iterations-in-a-for-loop

    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def rm(rl):
    num=0

    yhd=["CD","IX","IV","XL","XC","CM",]
    yhdl=[900,9,4,40,90,400]

    r=["I","V","X","L","C","M","D"]
    l=[1,5,10,50,100,500,1000]
    numbers = iter(range(0,len(rl)))
    oikea=True

    #testi
    for t in range(len(rl)):
        if rl[t:t+4]=="IIII" or rl[t:t+4]=="VVVV" or rl[t:t+4]=="XXXX" or rl[t:t+4]=="LLLL" or rl[t:t+4]=="CCCC" or rl[t:t+4]=="MMMM" or rl[t:t+4]=="DDDD":
            print("tämä ei ole sallittu:",rl[t:t+4])
            oikea=False
            break

    if oikea==True:

        #laskenta
        for i in numbers:

            #print("i on",i)
            if rl[i:i+2] in yhd:
                #print("yhd")
                for y in range(0,len(yhd)):
                    if rl[i:i+2]==yhd[y]:
                        print(yhd[y],"on",yhdl[y])
                        num+=yhdl[y]
                        consume(numbers,1)
                    else:
                        continue

            elif rl[i] in r:
                #print("yks")
                for n in range(0,len(r)):
                    if rl[i]==r[n]:
                        print(rl[i],"on",l[n])
                        num+=l[n]
        print(rl,"lukuna on",num)
    else:
        print("luku on väärin")

rm("DCMXLIV")

#1444
#I 1
#V 5
#X 10
#L 50
#C 100
#M 500
#D 1000

# CD 900
# IX 9 
# IV 4 
# XL 40 
# XC 90 
# CM 400
