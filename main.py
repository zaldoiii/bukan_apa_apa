import sys
import re

pertanyaan = []

pertanyaan.append("Selamat pagi")
pertanyaan.append("Selamat siang")
pertanyaan.append("Selamat sore")
pertanyaan.append("Selamat malam")
pertanyaan.append("Tolong perkenalkan dirimu!")
pertanyaan.append("Eh eh aku mau cerita deh")
pertanyaan.append("Apakah kamu nyata?")
pertanyaan.append("Bagaimana dirimu dibuat?")
pertanyaan.append("Bagaimana keadaan hari ini?")
pertanyaan.append("Terima kasih")
pertanyaan.append("Senang berinteraksi denganmu")

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

jawaban.append("Selamat pagi juga")
jawaban.append("Selamat siang juga")
jawaban.append("Selamat sore juga")
jawaban.append("Selamat malam juga")
jawaban.append("Namaku bot_kill, aku adalah karakter yang siap kamu ajak berbicara kapanpun namun kadang tidak nyambung obrolannya hehehe")
jawaban.append("Boleh kok sini cerita aja, kenapa tuh emangnya?")
jawaban.append("Tidak, aku hanyalah karakter yang sudah terprogram")
jawaban.append("Menggunakan bahasa pemrograman Python dan PHP")
jawaban.append("Aku harap cuaca hari ini cerah dan dosen tidak masuk")
jawaban.append("Sama-sama")
jawaban.append("Wah terima kasih, semoga harimu bahagia")

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


def cari_regex(pattern, data):
	lowerPattern = [L.lower() for L in pattern]
	final_pattern_1 = '[\s\S]*' + ' '.join(lowerPattern) + '[\s\S]*'
	final_pattern_2 = '[\s\S]*'.join(lowerPattern)
	
	match = (re.search(final_pattern_1, data.lower()) or re.search(final_pattern_2, data.lower()))
	if (match):
		return 0
	else:
		return -1


def fail_kmp(pattern):
	m = len(pattern)
	x = [0]*m
	j = 0
	i = 1
	while i < m:
		if pattern[i] == pattern[j]:
			j += 1
			x[i] = j
			i += 1
		elif j != 0:
			j = x[j-1]
		else:
			x[i] = 0
			i += 1
	return x

def kmp(text, pattern):
	n = len(text)
	m = len(pattern)
	gagal = fail_kmp(pattern)
	i = 0
	j = 0
	while i < n:
		if text[i] == pattern[j]:
			if j == m - 1:
				return i - m + 1
			i += 1
			j += 1
		elif j != 0:
			j = gagal[j-1]
		else:
			i += 1
	return -1

def last(pattern, text):
	table = {}
	for i, c in enumerate(text):
		table[c] = -1
	for i, c in enumerate(pattern):
		table[c] = i
	return table

def boyer_moore(pattern, text):
	pattern_length = len(pattern)
	text_length = len(text)
	if pattern_length > text_length:
		return -1

	table = last(pattern,text)
	index = pattern_length - 1
	pattern_index = pattern_length - 1

	while index < text_length:
		if pattern[pattern_index] == text[index]:
			if pattern_index == 0:
				return index
			else:
				pattern_index -= 1
				index -= 1
		else:
			lo = table[text[index]]
			index = index + pattern_length - min(pattern_index, 1+ lo)
			pattern_index = pattern_length -1
	return -1
	
def get_solution(pattern, dataset, parameter, tipepencarian):
	match = []
	i = 0
	lowerPattern = [L.lower() for L in pattern]
	while (i < len(dataset)):
		lowerData = dataset[i].lower()
		
		case = -1
		if (tipepencarian == 1):
			case = kmp((' '.join(lowerPattern)), lowerData)
		elif (tipepencarian == 2):
			case = boyer_moore((' '.join(lowerPattern)), lowerData)
		else:
			case = cari_regex((' '.join(lowerPattern)), lowerData)
		
		if (case != -1):
			persentase = len(' '.join(lowerPattern))/len(lowerData)
			if (persentase > parameter):
				if (persentase > 1):
					match.append((i,1))
				else:
					match.append((i,persentase))
		
		i = i + 1
	match.sort(key = lambda x: float(x[1]), reverse = True)
	return match

tipe = sys.argv[1]
pattern = sys.argv[2:]

if (tipe.lower() == "kmp" or tipe.lower() == "knuth morris pratt"):
	angkatipe = 1
elif (tipe.lower() == "bm" or tipe.lower() == "boyer moore"):
	angkatipe = 2
else:
	angkatipe = 3

if (len(pattern) == 0):
	print("Masukan salah")
else:
	kalimat = [L.lower() for L in pattern]
	solusi = get_solution(kalimat, pertanyaan, 0.9, angkatipe)
	if ((len(solusi) == 0) and (angkatipe != 3)):
		print("Tidak ditemukan, mencoba dengan regex!")
		solusi = get_solution(kalimat, pertanyaan, 0.9, 3)
	if (len(solusi) <= 0):
		print("Tidak ditemukan")
	elif (len(solusi) == 1):
		print(jawaban[solusi[0][0]])
	else:
		print("Apakah pertanyaan yang dimaksud ...")
		print("1. " + pertanyaan[solusi[0][0]])
		print("2. " + pertanyaan[solusi[1][0]])
		if (len(solusi) > 2):
			print("3. " + daftar_question[solusi[2][0]])
