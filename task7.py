squares = [i**2 for i in range(1, 11)]

print(squares)


even_numbers = [x for x in range(0,21) if x %2 == 0 ]

print(even_numbers)


words_list = ["falco","apple","leo","cup","orang"]

f = [words_list[0] for words_list in words_list]

print(f)

num_val = {
    1 : 1,
    2 : 4,
    3 : 3,
    4 : 16,
    5 : 25,
    
}

print(num_val)


wor_val = ["barcelona","argintina","cars","genshin"] 

word_lenghts = {word : len(word) for word in wor_val}

print(word_lenghts)