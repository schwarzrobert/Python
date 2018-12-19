from random import shuffle


liste = "amazing really excited amazing gorgeous vibrant blazing fast stunning \
        bold stunning biggest & fastest tremendous greatest & best".upper().split()


msg = "test 1"
print("asdf")
print(msg)


for strophe in range(3):
    for n in range(2):  
        for i in range(4):
            print("Thalia ich liebe dich ",end='')
            print("Marie natürlich auch")
            print()
       
        print(liste.pop() + " SPAM, " + liste.pop()+ " SPAM ")

    text1 = liste.pop()
    text2 = liste.pop()
    print("{} SPAM, {} SPAM".format(text1,text2))
    print()




#Reisfeldberechnung
summe =0
for feld in range(64):
    reiskorn =2**feld     #2 hoch
    summe = summe + reiskorn
    print("Feld {}. = {:,} Reiskörner und damit insgesamt  {:,} Reiskörner"\
    .format(feld+1,reiskorn,summe))

gewicht = summe *0.02 /1000 /1000
print("Wenn nun ein Reiskorn 0.2 Gramm benötigt")
print("Tonnen: {:18,.0f}".format(gewicht))