import random

def madliber():
    print("Welcome to Mary and Molly's MADLIBER Story!\n")

    # Collecting user inputs
    noun1 = input("Enter a noun (person, place, thing, idea): ")
    adjective1 = input("Enter an adjective (describes or defines a noun; adorable, bored, calm, busy): ")
    verb1 = input("Enter a verb (expresses action; run, swim, play, steal : ")
    adverb1 = input("Enter an adverb (modifies a verb or adverb; loudly, rudely, foolishly): ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")
    noun3 = input("Enter one more noun: ")
    body_part = input("Enter a body part: ")
    color = input("Enter a color: ")
    color2 = input("Enter a different color: ")
    adjective3 = input("Enter another adjective:")
    animal = input("Enter a type on animal: ")
    phrase = input("Enter a phrase (something you say): ")

    # Generating a random number to select a story
    story_number = random.randint(1, 3)

    # Selecting a story based on the random number
    
    if story_number == 1:
        story = "\fOnce upon a time, Mary and Molly woke up in a {adjective1} {noun1}, they decided they wanted to go to a {adjective2} {noun2} that was deep inside the {color} forest. " \
                "On the way there, Molly tripped and hurt her {body_part}, so Mary bandadged her up till it was nice and {color2}. " \
                "They met a {noun2} who loved to {verb1} {adverb1} and dream about {verb2} the {noun3}, so the girls told him {phrase}! " \
                "They never made it to the forest, but they had a {adjective3} good time! THE END! " \
    
    elif story_number == 2:
        story = "\fIn a {adjective1} land, there were two brave girls who always {verb1} {adverb1}. " \
                "One day, they discovered a {adjective2} {noun1} and decided to {verb2} it with all their might. " \
                "Before they knew what was happening, the {noun1} and turned into a {color} {noun2}! " \
                "Worried about their {adjective3} {color2}, {body_part} the two girls jumped on their {animal} and yelled out '{phrase}!' as they rode away.THE END! "
    
    else:  
        story = "\fGrandma Shauna woke up one morning and remembered she had to move the {adjective1} cows! " \
                " She got on her {adjective2} {animal} and rode out across the {color} field." \
                "The cows weren't listening so she called Mary and Molly and told them '{phrase}'! " \
                "Mary and Molly came to help with their {noun1}.  " \
                "During their journey, a {noun2} would often {verb1} {adverb1} and they would marvel at the beauty of a {noun2}. " \
                "After they got the cows in, they remembered the {noun1} and realized the true meaning of {verb2} and found inner peace. THE END! " \

    # Displaying the completed MADLIBER story
    print("\fMary and Molly's Adventure MADLIBER Story:\n")
    print(story)

# Run the MADLIBR function
madliber()
