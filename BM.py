import sys

sub = " ".join(sys.argv[1:])

pertanyaan = []
pertanyaan.append("Apa itu Python?")
pertanyaan.append("Apa itu Python Software Foundation?")
pertanyaan.append("Apakah ada batasan hak cipta untuk penggunaan Python?")
pertanyaan.append("Mengapa Python dibuat?")
pertanyaan.append("Apa gunanya Python?")
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
pertanyaan.append("Apakah saya harus menyukai \"Monty Python’s Flying Circus\"?")


def last(pattern, text):
    table = {}
    for i, c in enumerate(text):
	    table[c] = -1
    for i,c in enumerate(pattern):
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

def get_solution(pattern, dataset, parameter):
	match = []
	i = 1
	j = 1
	for data in dataset:
		case = boyer_moore(pattern, data)
		if (case != -1):
			percen = len(pattern)/(len(data)-1)
			if(percen > parameter):
				match.append(data)
	return match

print(sub[2])
#print(*get_solution(sub, pertanyaan, 0.9), sep = '')
