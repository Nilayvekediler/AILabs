import numpy as np
birim=input("Birim matris'in boyut bilgisini giriniz: ")
birimM=np.identity(int(birim))
print(birimM)
print()

i=input("Rastgele oluşturulacak matrisin satır sayısını (i) giriniz: ")
j=input("Rastgele oluşturulacak matrisin sütun sayısını (j) giriniz: ")

randomM=np.random.randint(10, size=(int(i),int(j)))  #np.array([[1, 2, 3], [4, 5,6]])
print(randomM)
transposeM=randomM.transpose()
print("\nBu matrisin transpose'u: ")
print(transposeM)
if(np.array_equal(randomM, transposeM)):
    print("\nOluşturulan random matris simetriktir.")
elif(np.array_equal(-randomM, transposeM)):
    print("\nOluşturulan random matris asimetriktir.")

if(i==j):
    traceM=np.trace(randomM)
    print("\nOluşturulan random matrisin trace'i: "+str(traceM))
else:
    print("\nMatrisin trace'i yalnızca nxn değerli kare matrislerde hesaplanabilir.")

i2=input("\nRastgele oluşturulacak 2. matrisin satır sayısını (i) giriniz: ")
j2=input("Rastgele oluşturulacak 2. matrisin sütun sayısını (j) giriniz: ")

randomM2=np.random.randint(10, size=(int(i2),int(j2)))  
print(randomM2)
print("\nMatris 1: ")
print(randomM)
print("Matris 2: ")
print(randomM2)
if(i==i2 and j==j2):
    totalM=np.add(randomM,randomM2)
    subM=np.subtract(randomM,randomM2)
    print("\nRastgele oluşturulmuş 2 matrisin toplamı: ")
    print(totalM)
    print("\nRastgele oluşturulmuş 2 matrisin 1.den 2.nin çıkarılması: ")
    print(subM)
else:
    print("\nMatrisler aynı tipli olmadığından toplama ve çıkarma işlemi yapılamaz.")

if(j==i2):
    mulM=np.matmul(randomM,randomM2)
    transposeM2=mulM.transpose()
    print("\nRastgele oluşturulmuş 1.matris ile 2.matrisin çarpımı: ")
    print(mulM)
    print("\nMatrislerin çarpımının devriği: ")
    print(transposeM2)
else:
    print("\n1. matrisin kolon sayısıyla 2. matrisin satır sayısı eşit olmadığından çarpma işlemi yapılamaz.")

