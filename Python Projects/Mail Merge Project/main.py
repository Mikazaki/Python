#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


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
