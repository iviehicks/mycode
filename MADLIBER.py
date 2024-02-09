import random

def madliber():
    print("Welcome to Mary and Molly/'s Adventure MADLIBER!\n")

    # Collecting user inputs
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    adverb1 = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")
    noun3 = input("Enter one more noun: ")

    # Generating a random number to select a story
    story_number = random.randint(1, 3)

    # Selecting a story based on the random number
    if story_number == 1:
        story = f"\nOnce upon a time, in a {adjective1} {noun1}, there lived a {adjective2} {noun2}. " \
                f"The {noun2} loved to {verb1} {adverb1} and dream about {verb2} the {noun3}."
    elif story_number == 2:
        story = f"\nIn a {adjective1} land, there was a brave {noun1} who always {verb1} {adverb1}. " \
                f"One day, the {noun1} discovered a {adjective2} {noun2} and decided to {verb2} it with all their might."
    else:
        story = f"\nA {adjective1} {noun1} once embarked on a {adjective2} journey. " \
                f"During the journey, the {noun1} would often {verb1} {adverb1} and marvel at the beauty of a {noun2}. " \
                f"At the end of the journey, the {noun1} realized the true meaning of {verb2} and found inner peace."

    # Displaying the completed MADLIBER story
    print("\nMary and Molly/'s Adventure MADLIBER Story:\n")
    print(story)

# Run the MADLIBS function
madliber()
