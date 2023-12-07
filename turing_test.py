import random

print("Welcome to the Turing test program")

def get_determiner(quantity):
    quantity = int(quantity)
    quantity = random.randint(1, 5)
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word.capitalize()


def get_noun(quantity):
    quantity = int(quantity)
    words = ["boy", "girl", "cat", "dog", "bird", "house"]
    word = random.choice(words)

    quantity = random.randint(1, 5)
    
    if quantity ==1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    quantity = int(quantity,)
    quantity = random.randint(1, 5)
    tense = ["past", "present", "future"]
    tense = random.choice(tense)

    past = [ "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    singular = [ "drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future = [ "will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    if tense == "past":
        past = random.choice(past)
        return past
    elif tense == "present" and quantity == 1:
        verbs = random.choice(verbs)
        return verbs
    elif tense == "present" and quantity != 1:
        singular = random.choice(singular)
        return singular
    elif tense == "future":
        future = random.choice(future)
        return future
    

def get_adjective():
      
      adjectives = ["Good", "New", "First", "Last", "High", "Old", "Great", "Small", "Big", "Different",
        "Long" ,"Same", "Early", "Late", "Young", "Important", "Difficult", "Public", "Large", "Small",
        "Early", "Late", "Easy", "Hard", "Strong", "Weak", "Beautiful", "Ugly", "Fast", "Slow"]
      
      adjective = random.choice(adjectives)
      return adjective

def get_preposition():

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"
    ]
    preposition = random.choice(prepositions)
    return preposition
        


def get_prepositional_phrase(quantity):
    quantity = int(quantity,)
    quantity = random.randint(1, 5)
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)

    return (f"{preposition} {determiner} {adjective} {noun}")
    

 



def make_sentence(quantity, tense):
    print(f"{get_determiner(5)} {get_noun(5)} {get_prepositional_phrase(quantity)} {get_verb(5, 5)} {get_prepositional_phrase(quantity)}")

def main():
    make_sentence(5, 5)
    make_sentence(5, 5)
    make_sentence(5, 5)
    make_sentence(5, 5)
    make_sentence(5, 5)
    make_sentence(5, 5)
    make_sentence(5, 5)

main()