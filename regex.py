import sys

pattern = sys.argv[1:]

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
pertanyaan.append("Siapa nama pemain karakter wanita yang direbutkan oleh kedua pria dalam lagu Adu Rayu?")
pertanyaan.append("Berapa jumlah presiden Indonesia?")
pertanyaan.append("Tahun berapa Indonesia merdeka?")
pertanyaan.append("Berapa tahun Indonesia dijajah Jepang?")
pertanyaan.append("Dimana Soekarno memproklamasikan kemerdekaan Indonesia?")
pertanyaan.append("Dimana kantin terdekat Labtek 5?")
pertanyaan.append("Apa itu bahasa pemrograman Python?")
pertanyaan.append("Apa itu Python Software Foundation?")
pertanyaan.append("Apakah ada batasan hak cipta untuk penggunaan Python?")
pertanyaan.append("Mengapa bahasa pemrograman Python dibuat?")
pertanyaan.append("Apa kelebihan bahasa pemrograman Python?")
pertanyaan.append("Bagaimana cara mendapatkan salinan sumber Python?")
pertanyaan.append("Bagaimana saya mendapatkan dokumentasi tentang Python?")
pertanyaan.append("Apakah ada tutorial Python?")
pertanyaan.append("Apakah ada newsgroup atau mailing list yang dikhususkan untuk Python?")
pertanyaan.append("Bagaimana cara mengirim laporan bug untuk Python?")
pertanyaan.append("Apakah ada artikel yang dipublikasikan tentang Python yang dapat saya pelajari?")
pertanyaan.append("Apakah ada buku tentang Python?")
pertanyaan.append("Di mana www.python.org berada?")
pertanyaan.append("Bagaimana asal usul nama Python?")

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
jawaban.append("Python adalah bahasa pemrograman yang interaktif dan berorientasi objek dengan sintaksis yang sangat jelas.")
jawaban.append("Python Software Foundation adalah organisasi yang memegang hak cipta pada Python versi 2.1 dan yang terbaru.")
jawaban.append("Tidak ada, selama Anda menampilkan hak cipta itu dalam dokumentasi apa pun tentang Python yang Anda hasilkan.")
jawaban.append("Karena pada saat itu dibutuhkan bahasa yang pada umumnya bersifat extensible.")
jawaban.append("Python adalah general-purpose programming language tingkat tinggi yang bisa diterapkan ke banyak kelas masalah yang berbeda.")
jawaban.append("Distribusi sumber Python terbaru selalu tersedia dari python.org, di https://www.python.org/downloads/")
jawaban.append("Dokumentasi standar untuk versi Python saat ini tersedia di https://docs.python.org/3/.")
jawaban.append("Ada banyak tutorial dan buku yang tersedia. Dokumentasi standar termasuk Tutorial Python.")
jawaban.append("Ada newsgroup di comp.lang.python, dan milis di python-list.")
jawaban.append("Untuk melaporkan bug, silakan gunakan instalasi Roundup di https://bugs.python.org/.")
jawaban.append("Mungkin lebih baik untuk mengutip buku favorit Anda tentang Python.")
jawaban.append("Banyak, lihat wiki python.org di https://wiki.python.org/moin/PythonBooks.")
jawaban.append("Infrastruktur proyek Python terletak di seluruh dunia dan dikelola oleh Tim Infrastruktur Python.")
jawaban.append("Guido van Rossum membaca skrip yang diterbitkan dari \"Monty Python\'s Flying Circus\"dan memutuskan untuk menyebutnya Python.")

import re

def cari_regex(pattern, Q, A):
	matched = []
	lowerPattern = [L.lower() for L in pattern]
	final_pattern_1 = '[\s\S]*' + ' '.join(lowerPattern) + '[\s\S]*'
	final_pattern_2 = '[\s\S]*'.join(lowerPattern)

	if (len(pattern) <= 2):
		print("Kata kunci terlalu sedikit")

	else:
		for i in range(0, len(Q)):
			match = (re.search(final_pattern_1, Q[i].lower()) or re.search(final_pattern_2, Q[i].lower()))
			if (match):
				print(A[i])

cari_regex(pattern, pertanyaan, jawaban)
