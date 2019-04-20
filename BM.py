import sys

sub = " ".join(sys.argv[1:])

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
	f = open(dataset, "r")
	match = []
	i = 1
	j = 1
	for data in f:
		case = boyer_moore(pattern, data)
		if (case != -1):
			percen = len(pattern)/(len(data)-1)
			if(percen > parameter):
				match.append(data)
	return match

print(*get_solution(sub, "Question.txt", 0.9), sep = '')
