#%% 1-MISOL
"""print("Eslatma -> sonlarfaqat 2 honali va qoldiq soni 1/1000 ko'rinishida yozilsin misol 99.123 !!!")
son = float(input("Sonni kiriting: "))
jami = 1
if(0<=son<10):
    if(len(str(son))==3):
        son*=10
        a = int(son)%10
        for i in range(1,a+1):
            jami*=i
        print(jami)
    elif(len(str(son))==4):
        son*=100
        a = int(son)%100
        for i in range(1,a+1):
            jami*=i
        print(jami)
    elif(len(str(son))==5):
        son*=1000
        a = int(son)%1000
        for i in range(1,a+1):
            jami*=i
        print(jami)   
elif(10<=son<100):
    if(len(str(son))==4):
        son*=10
        a = int(son)%10
        for i in range(1,a+1):
            jami*=i
        print(jami)
    elif(len(str(son))==5):
        son*=100
        a = int(son)%100
        for i in range(1,a+1):
            jami*=i
        print(jami)
    elif(len(str(son))==6):
        son*=1000
        a = int(son)%1000
        for i in range(1,a+1):
            jami*=i
        print(jami)

#%%2-MISOL
lst1 = [input("Malumot kiriting : ")]
print(lst1[0])
lst2 = lst1[0]
print(lst2[0])

if(lst2[2]=='1'and lst2[3]!='2' and lst2[3]!='1' and lst2[3]!='0' ):
    print("Yanvar")
elif(lst2[2]=='2'):
    print("Fevral")
elif(lst2[2]=='3'):
    print("Mart")
elif(lst2[2]=='4'):
    print("Aprel")   
elif(lst2[2]=='5'):
    print("May")   
elif(lst2[2]=='6'):
    print("Iyun")   
elif(lst2[2]=='7'):
    print("Iyul")
elif(lst2[2]=='8'):
    print("Avgust")
elif(lst2[2]=='9'):
    print("Sentyabr")
elif(lst2[2]=='1' and lst2[3] == '0' or lst2[3]=='1' and lst2[4] == '0'):
    print("Oktyabr")
elif(lst2[2]=='1' and lst2[3] == '1' or lst2[3]=='1' and lst2[4] == '1'):
    print("Noyabr")
elif(lst2[2]=='1' and lst2[3] == '2' or lst2[3]=='1' and lst2[4] == '2'):
    print("Dekabr")
else:
    print("Bunaqa oy yo'q")
if('1'<=lst2[0]<='7'):
    print("Oyning 1- haftasi")
if('7'<=lst2[0]<='9' and '0'<=lst2[1]<='4'):
    print("Oyning 2-haftasi")
if('5'<=lst2[1]<='9' and '0'<=lst2[1]<='1' or lst2[0]==2):
    print("Oyning 3-haftasi")
if('2'<=lst2[0]<='8' ):
    print("Oyning 4-haftasi")
    

#%% 3-MISOL

dct_birlik = {0:'',1:"bir",2:"ikki",3:"uch",4:"to'rt",5:"besh",6:"olti",7:"yetti",8:"sakkiz",9:"to'qqiz"}
dct_onlik = {0:'',10:"o'n",20:"yigirma",30:"yigirma",40:"qirq",50:"ellik",60:"yigirma",70:"yetmish",80:"sakson",90:"to'qson"}
#dct_yuzlik = {100:"bir yuz",200:"ikki yuz",300:"uch yuz",400:"to'rt yuz",500:"besh yuz",600:"olti yuz",700:"yetti yuz",800:"sakkiz yuz",900:"to'qqiz yuz"}
while (True):
    try:
        son = int(input("Son kiriting: "))
        if(len(str(son))>3):
            print("Faqat IKKI xonaligacha bo'lgan son kiriting!")
            continue
        break
    except ValueError:
        print("Faqat int son kiriting!")

onlik = 0
birlik = 0

if(int(len(str(son))) == 2):
    onlik = son//10%10*10
    birlik = son%10
    print(dct_onlik[onlik].capitalize(),dct_birlik[birlik])
elif(son == 0):
    print("No'l")
elif(int(len(str(son))) == 1):
    birlik = son%10
    print(dct_birlik[birlik].capitalize())

"""
#%% 5-MISOL

import sqlite3
import time

boglanish = sqlite3.connect("Filmlar.db")

kursr = boglanish.cursor()

def malumot_kirit():
    kursr.execute("CREATE TABLE IF NOT EXISTS kinolar(Nomi text,Yili text,Davlati text, Vaqti text,Bosh Roli text,Turi text,Olchami text)")
    boglanish.commit()
    
malumot_kirit()
user = input("Useringizni kiriting: ")
password = input("Parolingizni kiriting: ")
if(user == "admin" and password != "1234"):
    print("Password hato !!!")
elif(user != "admin" and password == "1234"):
    print("User hato !!!")
elif(user == "admin" and password == "1234"):
    print("Togri")
    def maxsulotQosh():
        nomi = input("Kino nomi: ")
        yili = input("Yilini kiriting: ")
        davlati = input("Davlati: ")
        vaqti = input("Davomiyligi: ")
        bosh_roli = input("Kim o'ynagan:")
        turi = input("Qanaqa janrda: ")
        olchami = input("Necha MB: ")
        kursr.execute("INSERT INTO kinolar VALUES(?,?,?,?,?,?,?)",(nomi,yili,davlati,vaqti,bosh_roli,turi,olchami))
        boglanish.commit()
        print("Malumot kiritilmoqda .......")
        time.sleep(3)
        print("Malumot kiritildi !!!")
    
    
    def malumotOlibkel():
        kursr.execute("SELECT * FROM kinolar")
        malumot = kursr.fetchall()
        print("\nBazada bor malumotlar !!!\n\n")
        for i in malumot:
            print(i)
    
    def malumotOlibkel1():
        kursr.execute("SELECT * FROM kinolar WHERE nomi = ?",(input("Nomi: "),))
        malumot = kursr.fetchall()
        print("Malumot kelmoqda.....")
        for i in malumot:
            print(i)
    def malumotYangila():
        kursr.execute("UPDATE kinolar SET olchami=? WHERE nomi=?",(input("olchamini kirit: "),input("Qaysi kinoni olchamini ozgartiray: "),))
        boglanish.commit()
    def malumotOchir():
        kursr.execute("DELETE FROM kinolar WHERE nomi=?",(input("Kino nomini yozing: "),))
        boglanish.commit()

    def malumot_All_Ochir():
        while(True):
            print("Siz bu kamandani bajarib bazadagi hamma malumotlarni o'chirib yuborasiz !!!")
            ochiraymi = input("O'chiraymi [ha/yoq]:")
            if ochiraymi == 'ha':
                break
            elif ochiraymi == 'yoq':
                break
            else:
                print("Notogri buyruq!\n")
            if(ochiraymi == "ha"):
                kursr.execute("DELETE FROM kinolar")
                boglanish.commit()
                print("O'chirilmoqda.....\n")
                time.sleep(2)
                print("Bazadan barcha malumot o'chirildi!\n")
            elif(ochiraymi == "yoq"):
                print("")
    while True:
        print("""
1.Malumot qo'shing
2.Malumotlarni ko'rsating
3.Kino nomi bo'yicha izlang
4.Malumot olchamini o'zgartiring
5.Kinoni  o'chiring
6.Hamma Malumotlarni o'chirish
7.Menyudan chiqish""")
        kirit = input("Son tanlang: ")
    
        if kirit == '1':
            maxsulotQosh()
        elif kirit == '2':
            malumotOlibkel()
        elif kirit == '3':
            malumotOlibkel1()
        elif kirit == '4':
            malumotYangila()
        elif kirit == '5':
            malumotOchir()
        elif kirit == '6':
            malumot_All_Ochir()
        elif kirit == '7':
            break
        else:
            print("noto'g'ri camanda")


            

boglanish.close()














    

