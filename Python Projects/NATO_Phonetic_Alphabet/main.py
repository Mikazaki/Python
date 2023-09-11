import pandas

NATO = pandas.read_csv("nato_phonetic_alphabet.csv")

NATO_dict = {row.letter: row.code for (index, row) in NATO.iterrows()}


def gen():
    name = input("Enter Name: ")
    try:
        NATO_name = [NATO_dict[letter.upper()] for letter in name]

    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        gen()

    else:
        print(NATO_name)


gen()
