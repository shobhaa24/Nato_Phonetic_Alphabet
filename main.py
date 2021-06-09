import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# for (index, row) in df.iterrows():
#     if row.letter == "A":
#         print(row.code)

#TODO 1. Create a dictionary in this format:
words = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
answer = input("Enter your name").upper()
list_phonetic = [words[alphabet] for alphabet in answer]
print(list_phonetic)
