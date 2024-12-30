import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
nato_word_list = [data_dict[i] for i in word]
print(nato_word_list)

