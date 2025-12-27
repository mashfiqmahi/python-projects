import os

PLACE_HOLDER = "[name]"

# Create output folder if it doesn't exist
os.makedirs("./Output/ReadyToSend", exist_ok=True)

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACE_HOLDER, stripped_name)

        with open(
            f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",
            mode="w"
        ) as completed_letter:
            completed_letter.write(new_letter)
