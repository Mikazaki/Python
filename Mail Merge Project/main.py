


with open("./Input/Letters/starting_letter.txt", mode='r') as file:
    lines = file.readlines()
    first = lines[0].strip()

    with open("./Input/Names/invited_names.txt", mode='r') as names:
        for name in names:
            name = name.strip()
            new = f"Dear {name},\n"
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="a") as letter:
                letter.write(new)
                letter.writelines(lines[1:])
