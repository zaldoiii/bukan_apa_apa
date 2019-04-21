import sys


s = sys.argv[1:] 


pattern = ".*"
for i in range(1,len(sys.argv)):
    pattern = pattern + sys.argv[i] + "." + "*" 

#import library regex
import re


l = []
l.append("Siapa nama koordinator dosen mata kuliah strategi algoritma 2018/2019?")
l.append("Siapa nama koordas strategi algoritma?")
l.append("Berapa jumlah SKS minimal untuk lulus S1 di ITB?")
l.append("Apa kepanjangan SKSD?")
l.append("Tanggal berapa diadakan pemilu tahun ini?")
l.append("Sudah berapa kali diadakan pemilu presiden?")
l.append("Pemilu diadakan berapa kali setahun?")
l.append("Siapa saja pembuat anda?")
l.append("Apa saja stack yang dipakai untuk membuat anda?")
l.append("Apa nama ibukota Indonesia?")
l.append("Nama ibukota Indonesia sebelum disebut Jakarta adalah?")
l.append("Siapa pembuat algoritma KMP?")
l.append("Siapa pemain catur nomor satu dunia sekarang?")
l.append("Apa nama blackhole yang berada di tengah galaksi bimasakti?")
l.append("Siapa nama pemain karakter wanita yang direbutkan oleh kedua pria dalam lagu Adu Rayu?")
l.append("Berapa jumlah presiden Indonesia?")
l.append("Tahun berapa Indonesia merdeka?")
l.append("Berapa tahun Indonesia dijajah Jepang?")
l.append("Dimana Soekarno memproklamasikan kemerdekaan Indonesia?")
l.append("Dimana kantin terdekat Labtek 5?")
l.append("Halo")
l.append("Siapa nama kamu?")
l.append("Kapan kamu lahir?")
l.append("Bagaimana kabar kamu?")
l.append("Dimana kamu tinggal?")
l.append("Hai")
l.append("Dengan bahasa apa kamu dibuat?")
l.append("Apa itu bahasa Python?")
l.append("Siapa pencipta bahasa Python?")
l.append("Kenapa bahasa Python dinamakan Python?")


l1 = []
l1.append("Rinaldi Munir")
l1.append("Kevin Andrian Liwinata")
l1.append("144 SKS")
l1.append("Sistem Komunikasi Satelit Domestik")
l1.append("4/17/2019")
l1.append("4 Kali")
l1.append("5 tahun sekali")
l1.append("Andrian, Anissa, dan Fajar")
l1.append("<apa ni maksudnya aing gapaham>")
l1.append("DKI Jakarta")
l1.append("Jayakarta")
l1.append("Knuth-Morris-Prat")
l1.append("Magnus Carlsen")
l1.append("Blackhole M87")
l1.append("Velove Vexia")
l1.append("Tujuh orang")
l1.append("1945")
l1.append("3 setengah tahun")
l1.append("Jl. Pegangsaan Timur No.56")
l1.append("Kantin Borju")
l1.append("Halo juga")
l1.append("Aku bot yang bernama AFA")
l1.append("Aku lahir pada 22 April 2019")
l1.append("Kabarku baik :)")
l1.append("Aku tinggal di Bandung")
l1.append("Hai juga")
l1.append("Aku dibuat menggunakan bahasa Python.")
l1.append("Python adalah bahasa pemrograman interpretatif multiguna dengan filosofi perancangan yang berfokus pada tingkat keterbacaan kode.")
l1.append("Guido van Rossum")
l1.append("Nama Python dipilih karena kecintaan pembuatnya pada acara televisi Monty Python's Flying Circus.")


for i in range(0,len(l)-1):
    pat = pattern.lower()
    t = l[i].lower()
    x = re.findall(pat,t)
    if(x):
        print(l1[i])
