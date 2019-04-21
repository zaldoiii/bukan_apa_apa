import sys


s = sys.argv[1:] 


pattern = ".*"
for i in range(1,len(sys.argv)):
    pattern = pattern + sys.argv[i] + "." + "*" 

#import library regex
import re


pertanyaan = []
pertanyaan.append("Siapa nama koordinator dosen mata kuliah strategi algoritma 2018/2019?")
pertanyaan.append("Siapa nama koordas strategi algoritma?")
pertanyaan.append("Berapa jumlah SKS minimal untuk lulus S1 di ITB?")
pertanyaan.append("Apa kepanjangan SKSD?")
pertanyaan.append("Tanggal berapa diadakan pemilu tahun ini?")
pertanyaan.append("Sudah berapa kali diadakan pemilu presiden?")
pertanyaan.append("Pemilu diadakan berapa kali setahun?")
pertanyaan.append("Siapa saja pembuat anda?")
pertanyaan.append("Apa saja stack yang dipakai untuk membuat anda?")
pertanyaan.append("Apa nama ibukota Indonesia?")
pertanyaan.append("Nama ibukota Indonesia sebelum disebut Jakarta adalah?")
pertanyaan.append("Siapa pembuat algoritma KMP?")
pertanyaan.append("Siapa pemain catur nomor satu dunia sekarang?")
pertanyaan.append("Apa nama blackhole yang berada di tengah galaksi bimasakti?")
pertanyaan.append("Siapa nama pemain karakter wanita yang direbutkan oleh kedua pria dalam lagu \"adu rayu\"?")
pertanyaan.append("Berapa jumlah presiden Indonesia?")
pertanyaan.append("Tahun berapa Indonesia merdeka?")
pertanyaan.append("Berapa tahun Indonesia dijajah Jepang?")
pertanyaan.append("Dimana Soekarno memproklamasikan kemerdekaan Indonesia?")
pertanyaan.append("Dimana kantin terdekat Labtek 5?")
pertanyaan.append("Apa itu bahasa pemrograman Python?")
pertanyaan.append("Apa itu Python Software Foundation?")
pertanyaan.append("Apakah ada batasan hak cipta untuk penggunaan Python?")
pertanyaan.append("Mengapa bahasa pemrograman Python dibuat?")
pertanyaan.append("Apa gunanya bahasa pemrograman Python?")
pertanyaan.append("Bagaimana cara mendapatkan salinan sumber Python?")
pertanyaan.append("Bagaimana saya mendapatkan dokumentasi tentang Python?")
pertanyaan.append("Apakah ada tutorial Python?")
pertanyaan.append("Apakah ada newsgroup atau mailing list yang dikhususkan untuk Python?")
pertanyaan.append("Bagaimana cara saya mendapatkan versi beta Python?")
pertanyaan.append("Bagaimana cara mengirim laporan bug untuk Python?")
pertanyaan.append("Apakah ada artikel yang dipublikasikan tentang Python yang dapat saya rujuk?")
pertanyaan.append("Apakah ada buku tentang Python?")
pertanyaan.append("Di mana www.python.org berada?")
pertanyaan.append("Mengapa disebut Python?")
pertanyaan.append("Apakah saya harus menyukai \"Monty Python\’s Flying Circus\"?")


jawaban = []
jawaban.append("Rinaldi Munir")
jawaban.append("Kevin Andrian Liwinata")
jawaban.append("144 SKS")
jawaban.append("Sistem Komunikasi Satelit Domestik")
jawaban.append("17 April 2019")
jawaban.append("4 Kali")
jawaban.append("5 tahun sekali")
jawaban.append("Kevin, Zaldi, dan Dandi")
jawaban.append("<tuliskan stack yang dipakai>")
jawaban.append("DKI Jakarta")
jawaban.append("Jayakarta")
jawaban.append("Knuth-Morris-Prat")
jawaban.append("Magnus Carlsen")
jawaban.append("Blackhole M87")
jawaban.append("velove vexia")
jawaban.append("Tujuh orang")
jawaban.append("1945")
jawaban.append("3 setengah tahun")
jawaban.append("Jl. Pegangsaan Timur No.56")
jawaban.append("Kantin Borju")
jawaban.append("Python adalah bahasa pemrograman yang interaktif dan berorientasi objek. Python menggabungkan modul, exception, dynamic typing, dynamic data types, dan kelas. Python menggabungkan kekuatan luar biasa dengan sintaksis yang sangat jelas. Ini memiliki antarmuka ke banyak system call dan library, serta berbagai window system, dan dapat diperluas dalam C atau C ++. Ini juga dapat digunakan sebagai bahasa ekstensi untuk aplikasi yang membutuhkan antarmuka yang dapat deprogram.")
jawaban.append("Python Software Foundation adalah organisasi nirlaba independen yang memegang hak cipta pada Python versi 2.1 dan yang terbaru. Misi PSF adalah untuk memajukan teknologi open source yang terkait dengan bahasa pemrograman Python dan untuk mempublikasikan penggunaan Python. Halaman beranda PSF ada di https://www.python.org/psf/.")
jawaban.append("Anda dapat melakukan apa pun yang Anda inginkan dengan sumbernya, selama Anda menampilkan hak cipta itu dalam dokumentasi apa pun tentang Python yang Anda hasilkan.")
jawaban.append("Karena pada saat itu dibutuhkan bahasa yang pada umumnya bersifat extensible.")
jawaban.append("Python adalah general-purpose programming language tingkat tinggi yang dapat diterapkan ke banyak kelas masalah yang berbeda. Bahasa ini dilengkapi dengan pustaka standar besar yang mencakup bidang-bidang seperti pemrosesan string, protokol Internet , rekayasa perangkat lunak , dan antarmuka sistem operasi.")
jawaban.append("Distribusi sumber Python terbaru selalu tersedia dari python.org, di https://www.python.org/downloads/. Sumber pengembangan terbaru dapat diperoleh di https://github.com/python/cpython/.")
jawaban.append("Dokumentasi standar untuk versi Python saat ini tersedia di https://docs.python.org/3/. PDF, teks biasa, dan versi HTML yang dapat diunduh juga tersedia di https://docs.python.org/3/download.html.")
jawaban.append("Ada banyak tutorial dan buku yang tersedia. Dokumentasi standar termasuk Tutorial Python.")
jawaban.append("Ada newsgroup, comp.lang.python, dan milis, python-list. Newsgroup dan milis saling berhubungan satu sama lain.")
jawaban.append("Rilis alfa dan beta tersedia dari https://www.python.org/downloads/. Semua rilis diumumkan di comp.lang.python dan comp.lang.python.announce newsgroup dan di beranda Python di https://www.python.org/.")
jawaban.append("Untuk melaporkan bug, silakan gunakan instalasi Roundup di https://bugs.python.org/.")
jawaban.append("Mungkin lebih baik untuk mengutip buku favorit Anda tentang Python.")
jawaban.append("Ya, ada banyak, dan lebih banyak lagi yang diterbitkan. Lihat wiki python.org di https://wiki.python.org/moin/PythonBooks.")
jawaban.append("Infrastruktur proyek Python terletak di seluruh dunia dan dikelola oleh Tim Infrastruktur Python.")
jawaban.append("Ketika mulai menerapkan Python, Guido van Rossum juga membaca skrip yang diterbitkan dari \"Monty Python\'s Flying Circus\", sebuah serial komedi BBC dari tahun 1970-an. Van Rossum berpikir dia membutuhkan nama yang pendek, unik, dan sedikit misterius, jadi dia memutuskan untuk memanggil bahasa Python.")
jawaban.append("Tidak, tapi itu membantu.")


for i in range(0,len(pertanyaan)-1):
    pat = pattern.lower()
    t = pertanyaan[i].lower()
    x = re.findall(pat,t)
    if(x):
        print(jawaban[i])
