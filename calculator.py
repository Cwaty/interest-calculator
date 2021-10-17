print("Sherwood")

paranumber = int(input("Para miktarı girin."))
paraanswer = float(paranumber)

faiznumber = int(input("Faiz oranı girin."))
faizanswer = float(faiznumber)

yılnumber = int(input("Faiz yılı girin."))
yılanswer = float(yılnumber)

answer = paraanswer*(faizanswer/100)*yılanswer

print("İşleme girilen faiz sayısı:", faizanswer)
print("İşleme girilen yıl sayısı:", yılanswer)
print("İşleme girilen para sayısı:" , paraanswer)
print("Faiz parası:",answer)
