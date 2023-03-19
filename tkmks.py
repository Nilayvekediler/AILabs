import random
myList = [1,2,3,4,5]
myPoint=0
computerPoint=0
gameInfo=str(1)
computerChoice=0

def match2():
    global myChoice
    if myChoice=="1":
        print("Taş")
    elif myChoice=="2":
        print("Kağıt")
    elif myChoice=="3":
        print("Makas")
    elif myChoice=="4":
        print("Kertenkele")
    elif myChoice=="5":
        print("Spock")

def match3():
    global computerChoice
    if computerChoice==1:
        print("Taş")
    elif computerChoice==2:
        print("Kağıt")
    elif computerChoice==3:
        print("Makas")
    elif computerChoice==4:
        print("Kertenkele")
    elif computerChoice==5:
        print("Spock")

def skor():
    global myPoint
    global computerPoint
    print("Senin Puanın: "+str(myPoint)+"  Bilgisayarın Puanı: "+str(computerPoint))

def isMaxSkor():
    global myPoint
    global computerPoint
    if (myPoint==10 or computerPoint ==10):
        print("OYUN BİTTİ")
        if(myPoint==10):
             print("***TEBRİKLER KAZANDINIZ***")
        else:
             print("KAYBETTİNİZ...")
        return 1


def gameFun(myCh,comCh):
    global myPoint
    global computerPoint
   
    if myCh == str(comCh):
        print("Bu el berabere.")
        skor()
    elif myChoice ==str(1) and (computerChoice==3 or computerChoice ==4):
        if computerChoice==3:
            print("Taş makası kırdı.")
        else:
            print("Taş kertenkeleyi ezdi.")
        print("Bu eli kazandın.") 
        myPoint=myPoint+1
        skor()
    elif myChoice ==str(1) and (computerChoice==2 or computerChoice ==5):
        if computerChoice==2:
            print("Kağıt taşı kapladı.")
        else:
            print("Spock taşı buharlaştırdı.")
        print("Bu eli kaybettin") 
        computerPoint+=1
        skor()
    elif myChoice ==str(2) and (computerChoice==1 or computerChoice ==5):
        if computerChoice==1:
            print("Kağıt taşı kapladı.")
        else:
            print("Kağıt spock'u çürüttü.")
        print("Bu eli kazandın.") 
        myPoint=myPoint+1
        skor()
    elif myChoice ==str(2) and (computerChoice==3 or computerChoice ==4):
        if computerChoice==3:
            print("Makas kağıdı kesti.")
        else:
            print("Kertenkele kağıdı yedi")
        print("Bu eli kaybettin") 
        computerPoint+=1
        skor()
    elif myChoice ==str(3) and (computerChoice==2 or computerChoice ==4):
        if computerChoice==2:
            print("Makas kağıdı kesti.")
        else:
            print("Makas kertenkeleyi kesti.")
        print("Bu eli kazandın.") 
        myPoint=myPoint+1
        skor()
    elif myChoice ==str(3) and (computerChoice==1 or computerChoice ==5):
        if computerChoice==1:
            print("Taş makası kırdı.")
        else:
            print("Spock makası kırdı.")
        print("Bu eli kaybettin") 
        computerPoint+=1
        skor()
    elif myChoice ==str(4) and (computerChoice==2 or computerChoice ==5):
        if computerChoice==2:
            print("Kertenkele kağıdı yedi")
        else:
            print("Kertenkele Spock'u zehirledi.")
        print("Bu eli kazandın.") 
        myPoint=myPoint+1
        skor()
    elif myChoice ==str(4) and (computerChoice==1 or computerChoice ==3):
        if computerChoice==1:
            print("Taş kertenkeleyi ezdi.")
        else:
            print("Makas kertenkeleyi ezdi.")
        print("Bu eli kaybettin") 
        computerPoint+=1
        skor()
    elif myChoice ==str(5) and (computerChoice==1 or computerChoice ==3):
        if computerChoice==1:
            print("Spock taşı buharlaştırdı.")
        else:
            print("Spock makası kırdı.")
        print("Bu eli kazandın.") 
        myPoint=myPoint+1
        skor()
    elif myChoice ==str(5) and (computerChoice==2 or computerChoice ==4):
        if computerChoice==2:
            print("Kağıt Spock'u çürüttü.")
        else:
            print("Kertenkele Spock'u zehirledi.")
        print("Bu eli kaybettin") 
        computerPoint+=1
        skor()
    

print("Taş-Kağıt-Makas-Kertenkele-Spock Oyunu'na hoş geldiniz!")

while gameInfo==str(1):

    gameInfo = input("Oyun kurallarını görmek için 0'a, Oyuna başlamak için 1'e, Çıkış Yapmak için 2'ye basınız: ")

    if gameInfo==str(0):
        print("Taş-Kağıt-Makas-Kertenkele-Spock Oyun Kuralları:\n*Taş için 1, Kağıt için 2, Makas için 3, Kertenkele için 4, Spock için 5'e basınız.\n*Oyun rakiplerden birinin 10 puan almasıyla sonlanacaktır.\n*Beraberlikte iki tarafa da puan verilmez.\n*Her adımda kazananana 1 puan verilir.\n")
       
        okSpace = input("Ana menüye dönmek için space tuşuna basınız: ")
        if okSpace.isspace()==1:
            gameInfo=str(1)
        else:
            print("Beklenen dışı girdi.")
    elif gameInfo==str(1):
        while isMaxSkor()!=1:
            myChoice = input("Seçiminiz: ") 
            if int(myChoice) in range(1,6):
                match2()
                computerChoice = random.choice(myList)
                print("Bilgisayarın Seçimi: "+str(computerChoice))
                match3()
                print(" ")
                gameFun(myChoice,computerChoice)
                print("------------------------------------------")
            else:
                 print("Beklenen dışı girdi.\n")
    elif gameInfo==str(2):
        gameInfo=str(0)
    else:
         print("Beklenen dışı girdi.")
    