#!/usr/bin/env python3

"""This is my version of MADLIBS that I called MADLIBER, I designed it for my daughters that are 7 and 10 years old.  I wanted to make something that is interactive and educational for them -but most of all good for a laugh! It is not the most advanced Python script, but I learned alot while figuring it out and I was able to incorporate things like crayons and ascii art to make it more visually appealing.  Enjoy!"""

import random
import crayons


def madliber():
    print("  (\__/)      (\__/)")
    print("  (='.'=)     (='.'=)")
    print(" ('')_('')   ('')_('')")

    print("Welcome to Mary and Molly's MADLIBER Story! I need you to answer some questions to help me make a story. \n")

    # Asking the reader for inputs to develop the stories
    noun1 = input(f'{crayons.red ("Enter a noun (person, place, thing, idea): ")}' )
    adjective1 = input(f'{crayons.magenta ("Enter an adjective (describes or defines a noun; cute, calm, busy, ugly, stinky): ")}' )
    verb1 = input(f'{crayons.green ("Enter a verb (expresses action; run, swim, play, steal): ")}'  )
    adverb1 = input(f'{crayons.yellow ("Enter an adverb (modifies a verb or adverb; loudly, rudely, foolishly): ")}'  )
    adjective2 = input(f'{crayons.blue ("Enter another adjective: ")}'  )
    noun2 = input(f'{crayons.cyan ("Enter another noun: ")}'  )
    verb2 = input(f'{crayons.red ("Enter another verb: ")}'  )
    noun3 = input(f'{crayons.yellow ("Enter one more noun: ")}'  )
    body_part = input(f'{crayons.magenta ("Enter a body part: ")}'  )
    color = input(f'{crayons.green ("Enter a color: ")}'  )
    color2 = input(f'{crayons.blue ("Enter a different color: ")}'  )
    adjective3 = input(f'{crayons.red ("Enter another adjective:")}'  )
    animal = input(f'{crayons.yellow ("Enter a type of animal: ")}'  )
    phrase = input(f'{crayons.blue ("Enter a phrase (something you say, like, Hey youuu guys!!): ")}'  )

    # Generating a random number to select one of the 3 stories
    story_number = random.randint(1, 3)

    # The base story is selected by the random number
    
    if story_number == 1:
        story = f"\fOnce upon a time, Mary and Molly woke up in a {adjective1} {noun1}, they decided they wanted to go to a {adjective2} {noun2} that was deep inside the {color} forest. " \
               f"On the way there, Molly tripped and hurt her {body_part}, yelling out '{phrase}!' So Mary bandadged her up till it was nice and {color2}. " \
               f"They met a {noun2} who loved to {verb1} {adverb1} and dream about {verb2} the {noun3}, so the girls told him {phrase}! " \
               f"They never made it to the forest, but they had a {adjective3} good time! THE END! " \
    
    elif story_number == 2:
        story = f"\fIn a {adjective1} land, there were two brave girls who always {verb1} {adverb1}. " \
                f"One day, they discovered a {adjective2} {noun1} and decided to {verb2} it with all their might. " \
                f"Before they knew what was happening, the {noun1} and turned into a {color} {noun2}! " \
                f"Worried about their {adjective3} {color2}, {body_part} the two girls jumped on their {animal} and yelled out '{phrase}!' as they rode away.THE END! "
    
    else:  
        story = f"\fGrandma Shauna woke up one morning and remembered she had to move the {adjective1} cows! " \
                f" She got on her {adjective2} {animal} and rode out across the {color} field." \
                f"The cows weren't listening so she called Mary and Molly and told them '{phrase}!' " \
                f"Mary and Molly came to help with their {noun1}.  " \
                f"During their journey, a {noun2} would often {verb1} {adverb1} and they would marvel at the beauty of a {noun2}. " \
                f"After they got the cows in, they remembered the {noun1} and realized the true meaning of {verb2} and found inner peace. THE END! " \

    # Displaying the completed MADLIBER story
    print("\fMary and Molly's Adventure MADLIBER Story:\n")
    print(story)
   

# Run the MADLIBER function
madliber()
