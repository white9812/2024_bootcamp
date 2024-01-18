univ="inha university"
counts_alphabet={letter:word.count(letter) for letter in univ}
print(counts_alphabet)

counts_alphabet=dict()
for letter in univ:
    counts_alphabet[letter]=univ.count(letter)
print(counts_alphabet)