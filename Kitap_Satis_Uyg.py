  
import random
import string
class Books:

    global allBookInfo
    allBookInfo=[]  

    def bookReg(**bookInfos): 
        bookInfo ={} 

        for key, value in bookInfos.items():
            bookInfo[key] = value
      
        allBookInfo.append(bookInfo)
        #print(allBookInfo)
        #print("----------------")

    def showBooks():
        tmpDict={}
        
        for i in range(len(allBookInfo)):
            tmpDict=allBookInfo[i]
            for key, value in tmpDict.items():
                bookNames = value
                print(str(i+1)+". "+bookNames) 
                break
            
    def getInfoSelectedBook(selectedBookNum):
        return(allBookInfo[(int(selectedBookNum))-1])


    def getSelectedBookName(selectedBookNum):
        for key, value in  (allBookInfo[(int(selectedBookNum))-1]).items():
                selectedBookName = value
                break
        return selectedBookName
    
    def getSelectedBookPrice(selectedBookNum):
        for key, value in  (allBookInfo[(int(selectedBookNum))-1]).items():
                if key=="Fiyat":
                    return value
                    break
   
    def getInfoOrderedBook(bookName):
        tmpDict={}
        
        for i in range(len(allBookInfo)):
            tmpDict=allBookInfo[i]
            for key, value in tmpDict.items():
               if key=="Adı" and value==bookName:
                   print(tmpDict)
                   print("")
    


        
class Customer:
     
    global ordersList
    global detailedOrdersList
    global orderCategoryList
    global orderAuthorList
    global orderPublisherList
    ordersList=[]
    detailedOrdersList=[]
    orderCategoryList=[]
    orderPublisherList=[]
    orderAuthorList=[]

    

    global freeRomanPrices
    global freeSiirPrices
    global freeKorkuPrices
    global freeCocukPrices
    freeRomanPrices=[]
    freeSiirPrices=[]
    freeKorkuPrices=[]
    freeCocukPrices=[]


    campaigns=["Aynı kategoriden 3 al 2 öde","Farklı kategorilerden 4 al 3 öde","Aynı yayınevinden 2 kitapta totalde %5.3 indirim","Aynı yayınevinden 2+ kitapta totalde %7 indirim","Aynı yazara ait 2. kitapta %30 indirim"]
   
    def createOrderWithDetail(myDicts):
        detailedOrdersList.append(myDicts)

    def Campaign1():
        global romanPrices
        global siirPrices
        global korkuPrices
        global cocukPrices
        romanPrices=[]
        siirPrices=[]
        korkuPrices=[]
        cocukPrices=[]

        tmpDict={}
        tmpDict2={}
        
        for i in range(len(detailedOrdersList)):
            tmpDict=detailedOrdersList[i]
            #print(detailedOrdersList) -------
            for key, value in tmpDict.items():
                if key=="Tür":
                    orderCategoryList.append(value)
                    #print(orderCategoryList) -------
                elif key=="Yayınevi":
                    orderPublisherList.append(value)
                elif key=="Yazar":
                    orderAuthorList.append(value)

        for i in range(len(detailedOrdersList)):
            tmpDict2=detailedOrdersList[i]
            for key, value in tmpDict2.items():
                if key=="Tür" and value=="Roman":
                    romanPrices.append(tmpDict2["Fiyat"])
                    #print(romanPrices) -------
                elif key=="Tür" and value=="Şiir":
                    siirPrices.append(tmpDict2["Fiyat"])
                elif key=="Tür" and value=="Korku":
                    korkuPrices.append(tmpDict2["Fiyat"])
                elif key=="Tür" and value=="Çocuk":
                    cocukPrices.append(tmpDict2["Fiyat"])
                

        countRoman=orderCategoryList.count("Roman")
        countSiir=orderCategoryList.count("Şiir")
        countKorku=orderCategoryList.count("Korku")
        countCocuk=orderCategoryList.count("Çocuk")

        #print(countRoman)
        if countRoman%3: #9
            howManyFreeC=countRoman/3 #3
            print(romanPrices.sort())
            for i in range(int(howManyFreeC)):
                freeRomanPrices.append(romanPrices[i])
                del(romanPrices[i])

        #print(freeRomanPrices)
        #print(sum(freeRomanPrices))

        
        return(sum(freeRomanPrices))
    

    def createOrder(**orderInfos):
        orderInfo={}
       
        for key, value in orderInfos.items():
            orderInfo[key] = value

        ordersList.append(orderInfo)   
        print("Ürün başarıyla sepetinize eklendi.")


    def showOrders(): 
        for i in range(len(ordersList)):
            print(str(i+1)+". "+str(ordersList[i])) 
        print(" ")

    def getInfoOrder(orderDetailNum):
        tmpDict={}
        book3=Books
        
        for i in range(len(ordersList)):
            tmpDict=ordersList[i]
            for key, value in tmpDict.items():
                if key=="SepetNo" and value==orderDetailNum:
                    bookName=tmpDict["SepeteEklenenKitap"]
                    book3.getInfoOrderedBook(bookName)
                    
    def getTotalPrice():
        tmpDict={}
        total=0
       
        for i in range(len(ordersList)):
            tmpDict=ordersList[i]
            for key, value in tmpDict.items():
                if key=="Fiyat":
                    total=value+total
        return total

            

               

               



    def orderPnrGenerate():
        source = string.ascii_letters + string.digits
        orderPnr = ''.join((random.choice(source) for i in range(8)))
        return orderPnr



class Index: 

    role=1
    print("***********Nilay'ın Kitap Dükkanına Hoş Geldiniz!***********")
    role = input("Admin girişi için 0'a, Müşteri girişi için 1'e basınız: \n")

    book1=Books
    book1.bookReg(Adı="Frankenstein",Tür="Korku",Yayınevi="MKPublic",Yazar="Marry Shelly",SayfaSayısı=50,Fiyat=100)
    book1.bookReg(Adı="Heidi",Tür="Çocuk",Yayınevi="Childrens Classic",Yazar="Johanna",SayfaSayısı=352,Fiyat=50)
    book1.bookReg(Adı="IBelieveInAllah",Tür="Çocuk",Yayınevi="Muslim",Yazar="Johanna",SayfaSayısı=30,Fiyat=80) 
    book1.bookReg(Adı="Yabancı",Tür="Roman",Yayınevi="Can",Yazar="Albert Camus",SayfaSayısı=112,Fiyat=40) 
    book1.bookReg(Adı="Suç ve Ceza",Tür="Roman",Yayınevi="Türkiye İş Bankası",Yazar="Dostoyevski",SayfaSayısı=100,Fiyat=30) 
    book1.bookReg(Adı="Çilekler ve Tuz",Tür="Roman",Yayınevi="Nilcp",Yazar="Nilay İnel",SayfaSayısı=180,Fiyat=20) 



    while role==str(0):

            print("Admin Modülüne Hoş Geldiniz.")
            bookNum = input("Eklemek istediğiniz kitap bilgisi adedini giriniz: \n")
            for x in range(int(bookNum)):
                name = input("Adı: ")
                category = input("Tür: ")
                publisher = input("Yayınevi: ")
                author = input("Yazar: ")
                pages = input("Sayfa Sayısı: ")
                price = input("Fiyat: ")
                print("")

                book1=Books
                book1.bookReg(Adı=name,Tür=category,Yayınevi=publisher,Yazar=author,SayfaSayısı=pages,Fiyat=price)
            
            role=input("Admin menüsüne dönmek için 0'a, müşteri menüsüne geçmek için 1'e, çıkış yapmak için 2'ye basınız.")
        

        

        

  
    if role==str(1):
        selectedBookNum = "0"
        print("Müşteri Modülüne Hoş Geldiniz.")
        nick=input("Kullanıcı adınızı giriniz: ")
        exit= input("Kitaplar aşağıdaki gibidir. Detaylı bilgi edinmek istediğiniz kitabın numarasını girip enter tuşuna basınız. Çıkmak için 'exit' yazıp enter tuşuna basınız.\n")
        while exit!="exit":
            book2=Books
            book2.showBooks()

            selectedBookNum = input("\nKitap Numarası: ")
            if selectedBookNum=="exit":
                break
            print()
            print(book2.getInfoSelectedBook(selectedBookNum))
            print()

            orderedBook= input("Bu eşsiz kitaba sahip olmak istiyorsanız, kitabı sepete eklemek için x'e basınız: ")
            if orderedBook=="x" or orderedBook=="X":
                customer=Customer
                customer.createOrder(Müşteri=nick,SepeteEklenenKitap=book2.getSelectedBookName(selectedBookNum),Fiyat=book2.getSelectedBookPrice(selectedBookNum),SepetNo=customer.orderPnrGenerate())
                customer.createOrderWithDetail(book2.getInfoSelectedBook(selectedBookNum))
            
            
            goOrder= input("\nSepetinize gitmek istiyorsanız 's' tuşuna basınız: ")
            if goOrder=="s" or goOrder=="S":
                con=0
                while con==0:
                    exit="exit"
                    print("Sepetim: ")
                    customer=Customer
                    customer.showOrders()
                    print("Ödenecek İndirimsiz Toplam Miktar: "+str(customer.getTotalPrice())+" TL.")
                    print("Uygulanan kampanya:"+str(customer.campaigns[3]))
                    print("İndirim Tutarı:"+str(customer.Campaign1()))
                    pay=(customer.getTotalPrice())-(customer.Campaign1())
                    print("Ödenecek Tutar:"+str(pay)) 
                    orderDetailNum= input("Detaylı bilgi edinmek istediğiniz sepet numarasını girip enter tuşuna basınız: ")
                    customer2=Customer
                    customer2.getInfoOrder(orderDetailNum)
                    zero=input("Alışverişe devam etmek için 0'a basınız: ")
                    if zero=="0":
                        exit=""
                        con=1

    else:
        if role==str(2):
             exit()
        else:
            print("\nBeklenen dışı veri girdiniz.")


      



  
          
