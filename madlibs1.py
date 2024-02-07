def mad_libs():
    # Mad Libs story template with placeholders
    story_template = "Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}. One day, the {noun} {past_verb} very {adjective} and decided to {action}. The end!"

    # Prompting the user to provide words for the placeholders
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    past_verb = input("Enter a past tense verb: ")
    action = input("Enter an action: ")

    # Filling in the blanks in the story template
    mad_lib_story = story_template.format(adjective=adjective, noun=noun, verb=verb, adverb=adverb, past_verb=past_verb, action=action)

    # Displaying the completed Mad Libs story
    print("\nYour Mad Libs story:\n")
    print(mad_lib_story)

# Run the Mad Libs function
mad_libs()
