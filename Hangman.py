import time
from random import choice

# oyuncuya oyunu anlatıyor
print ("Ekrana rastgele bir kelime ve bir ipucu gelecek. Bu ipucuna göre kelimeyi bulmaya çalış.")
# ardından uygulama 1.5 saniye bekliyor
time.sleep(1.5)

# kelime havuzu yaratıyoruz
listeCanliDort = ["kedi","kuzu","deve","lama","inek","kurt","fare","dana","çita","eşek","pire","kene","kuğu"]
listeCanliBes = ["horoz","tavuk","köpek","aslan","balık","çakal","hindi","domuz","sinek","tilki","yılan","zebra","akrep","karga","koyun","kumru","sığır","yunus","goril"]
listeCanliAlti = ["balina","bülbül","kuzgun","tavşan","sincap","yarasa","timsah","kartal","sırtlan","leopar","kaplan","akbaba","civciv","ceylan","iguana","porsuk","sansar","panter","zürafa","yengeç","tırtıl"]
listeIsimDort = ["arda","berk","bora","cenk","emir","emre","eray","mert","mete","onur","tuna","ulaş","umut","anıl","ayaz","enes","enis","eren","kaan","oğuz","ozan","ömer","sarp","arzu","aslı","azra","emel","duru","ecem","ışıl","öykü","sena"]
listeIsimBes = ["murat","alper","kemal","ahmet","barış","celal","erden","ergün","fatih","giray","ilker","kadir","tekin","miraç","olcay","osman","bartu","nihan","yeşim","beyza","bahar","cansu","sinem","selen","şeyma","şeyda","asude","hülya","begüm"]
listeIsimAlti = ["mahmut","rıdvan","necdet","serkan","tarkan","burhan","bülent","kudret","süheyl","behzat","atakan","furkan","berkin","poyraz","ferhat","dinçer","tuncay","refika","mehtap","candan","şermin","şevval","meltem","feride","ilayda","açelya"]
listeNesneDort = ["masa","ayna","vazo","kase","maşa","sıra","örtü","örgü","askı","priz","kapı","iğne","odun","halı","bank","çapa","çeki"]
listeNesneBes = ["balon","dışkı","hamak","kablo","leğen","çanta","tahta","radyo","çekiç","kağıt","sehpa","dolap","kalem","kaşık","kemik","bıçak","tablo","rende","kilit","ayraç","makas","lamba","ampul"]
listeNesneAlti = ["terlik","bardak","cımbız","gözlük","koltuk","balyoz","demlik","yorgan","yastık","sandık","sürahi","küllük","klavye","yazıcı","defter"]

# bu kelime havuzlarını bir araya getiriyoruz
listeCanlilar = listeCanliDort + listeCanliBes + listeCanliAlti
listeIsimler = listeIsimDort + listeIsimBes + listeIsimAlti
listeNesneler = listeNesneDort + listeNesneBes + listeNesneAlti
listeGenel = listeCanliDort + listeCanliBes + listeCanliAlti + listeIsimDort + listeIsimBes + listeIsimAlti + listeNesneDort + listeNesneBes + listeNesneAlti

# hangi kelimenin seçileceği belirleniyor
word = choice(listeGenel)
#kelimenin hangi grupta olduğuna bağlı olarak ipucu veriliyor
if word in listeCanlilar:
    print("İpucu: Bu bir canlı.")
elif word in listeIsimler:
    print("İpucu: Bu bir isim.")
elif word in listeNesneler:
    print("İpucu: Bu bir nesne.")

# string olan bir variable yaratıyoruz
guesses = ''

# kaç hakkın olacağı belirleniyor
turns = len(word) + 3

# kalan hak 0'dan fazla mı
while turns > 0:
    # 0 ile başlayan bir counter yaratıyoruz
    failed = 0

    # yazılan her bir karakter için
    for char in word:
        # karakterin, kişinin tahminiyle aynı olup olmadığına bakıyoruz
        if char in guesses:
            # eğer doğru tahminse, o karakteri yazdırıyoruz
            print(char, end=""),
        else:
            # eğer yanlış tahminse aynen devam ediyor
            print("_", end=""),
            # ve failed sayısını artırıyoruz
            failed += 1

    # eğer failed==0 ise kazandın
    if failed == 0:
        print(" Tebrikler, kazandın!")
        # exit the script
        break
    # kişinin bir karakter yazmasını istiyoruz
    guess = input(" Bir karakter yazın:")

    # kişinin yalnızca bir karakter yazmış olduğunu garanti altına alıyoruz if-else ile
    if len(guess) > 1:
        print("Lütfen yalnızca 1 karakter yazınız.")
    else:
        guesses += guess
        # eğer girilen karakter kelimede yoksa
        if guess not in word:
            turns -= 1
            print("Kelimede böyle bir karakter yok!")
            # kaç hakkın kaldığı
            print(turns, "hakkınız daha var.")
            # eğer 0 hak kalmışsa
            if turns == 0:
                print("Üzgünüm, kaybettin.")