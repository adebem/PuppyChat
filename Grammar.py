# Grammar.py
# contains the word dictionary and syntax rule diction necessary for parsing and interpreting the user input
# Anthony de Bem 2021

# dictionary that contains all of the words/phrases that PuppyChat recognizes
# alphabetically organized into indexes for speedy lookup
dictionary = {
    'a': [
        ('a', 'Article'),
        ('act', 'Verb'),
        ('acd', 'Name'),
        ('airedale', 'Name'),
        ('airedale_terrier', 'Name'),
        ('akita', 'Name'),
        ('akita_inu', 'Name'),
        ('am', 'Verb'),
        ('american_bulldog', 'Name'),
        ('and', 'Conjunction'),
        ('anthony', 'Name'),
        ('are', 'Verb'),
        ('australian_cattle_dog', 'Name'),
        ('australian_shepherd', 'Name'),
        ('as', 'Preposition')
    ],

    'b': [
        ('basset_hound', 'Name'),
        ('be', 'Verb'),
        ('beagle', 'Name'),
        ('belgian_malinois', 'Name'),
        ('behave', 'Verb'),
        ('behavior', 'Noun'),
        ('berner', 'Name'),
        ('bernese', 'Name'),
        ('bernese_mountain_dog', 'Name'),
        ('bichon', 'Name'),
        ('bichon_frise', 'Name'),
        ('blood_hound', 'Name'),
        ('bloodhound', 'Name'),
        ('brittany', 'Name'),
        ('breed', 'Noun'),
        ('breeds', 'Noun'),
        ('boston_terrier', 'Name'),
        ('border_collie', 'Name'),
        ('boxer', 'Name'),
        ('bulldog', 'Name'),
        ('bullmastiff', 'Name')
    ],

    'c': [
        ('cane_corso', 'Name'),
        ('cavalier_king_charles_spaniel', 'Name'),
        ('cavalier', 'Name'),
        ('chesapeake_bay_retriever', 'Name'),
        ('chessy', 'Name'),
        ('chihuahua', 'Name'),
        ('cocker_spaniel', 'Name'),
        ('collie', 'Name'),
        ('corsi', 'Name'),
    ],

    'd': [
        ('dachshund', 'Name'),
        ('dal', 'Name'),
        ('dalmatian', 'Name'),
        ('describe', 'Verb'),
        ('different', 'Adjective'),
        ('do', 'Verb'),
        ('doberman', 'Name'),
        ('doberman_pinscher', 'Name'),
        ('does', 'Verb'),
        ('dog', 'Noun'),
        ('dogs', 'Noun')
    ],

    'e': [
        ('ec', 'Name'),
        ('english_cocker_spaniel', 'Name'),
        ('english_springer_spaniel', 'Name')
    ],

    'f': [
        ('french_bulldog', 'Name'),
        ('from', 'Preposition')
    ],

    'g': [
        ('german_shepherd', 'Name'),
        ('german_shorthaired_pointer', 'Name'),
        ('golden', 'Name'),
        ('golden_retriever', 'Name'),
        ('great_dane', 'Name'),
        ('group', 'Noun'),
        ('group', 'group')
    ],

    'h': [
        ('havanese', 'Name'),
        ('heavier', 'Adjective'),
        ('heavy', 'Adjective'),
        ('heeler', 'Name'),
        ('height', 'Noun'),
        ('hello', 'Greeting'),
        ('herding', 'GroupName'),
        ('hi', 'Greeting'),
        ('hound', 'GroupName'),
        ('how', 'Adverb'),
        ('how', 'WQuestion'),
        ('husky', 'Name')
    ],

    'i': [
        ('i', 'Pronoun'),
        ('i\'m', 'i\'m'),
        ('is', 'Verb'),
        ('in', 'Preposition')
    ],

    'l': [
        ('lab', 'Name'),
        ('labrador', 'Name'),
        ('less', 'Adjective'),
        ('less', 'Adverb'),
        ('lifespan', 'Noun'),
        ('life_expectancy', 'Noun'),
        ('lighter', 'Adjective'),
        ('like', 'Preposition'),
        ('live', 'Verb'),
        ('lives', 'Verb'),
        ('long', 'Adjective'),
        ('longer', 'Adjective')
    ],

    'm': [
        ('mal', 'Name'),
        ('malinois', 'Name'),
        ('maltese', 'Name'),
        ('mastiff', 'Name'),
        ('mini', 'Name'),
        ('mini_american_shepherd', 'Name'),
        ('miniature_american_shepherd', 'Name'),
        ('mini_schnauzer', 'Name'),
        ('miniature_schnauzer', 'Name'),
        ('more', 'Adjective'),
        ('more', 'Noun'),
        ('more', 'Adverb'),
        ('much', 'Adjective'),
        ('my', 'Adjective')
    ],

    'n': [
        ('name', 'Noun'),
        ('newf', 'Name'),
        ('newfoundland', 'Name'),
        ('non-sporting', 'GroupName')
    ],

    'o': [
        ('of', 'Preposition')
    ],

    'p': [
        ('pap', 'Name'),
        ('papillon', 'Name'),
        ('pembroke_welsh_corgi', 'Name'),
        ('personality', 'Noun'),
        ('pug', 'Name'),
        ('pointer', 'Name'),
        ('pomeranian', 'Name'),
        ('poodle', 'Name'),
        ('portie', 'Name'),
        ('portuguese_water_dog', 'Name'),

    ],

    'q': [
        ('queensland', 'Name')
    ],

    'r': [
        ('rhodesian_ridgeback', 'Name'),
        ('ridgeback', 'Name'),
        ('rottie', 'Name'),
        ('rottweiler', 'Name')
    ],

    's': [
        ('saint_bernard', 'Name'),
        ('same', 'Adjective'),
        ('samoyed', 'Name'),
        ('scottie', 'Name'),
        ('scottish_terrier', 'Name'),
        ('shelty', 'Name'),
        ('shetland_sheepdog', 'Name'),
        ('shiba', 'Name'),
        ('shiba_inu', 'Name'),
        ('shih_tzu', 'Name'),
        ('shih-tzu', 'Name'),
        ('short', 'Adjective'),
        ('shorter', 'Adjective'),
        ('siberian_husky', 'Name'),
        ('soft_coated_wheaten_terrier', 'Name'),
        ('sporting', 'GroupName'),
        ('summarize', 'Verb'),
        ('summary', 'Noun')
    ],

    't': [
        ('tall', 'Adjective'),
        ('taller', 'Adjective'),
        ('temperament', 'Noun'),
        ('terrier', 'GroupName'),
        ('than', 'Preposition'),
        ('the', 'Article'),
        ('their', 'Determiner'),
        ('they', 'Pronoun'),
        ('those', 'Pronoun'),
        ('them', 'Pronoun'),
        ('toy', 'GroupName'),
    ],

    'w': [
        ('was', 'WQuestion'),
        ('weigh', 'Verb'),
        ('weighs', 'Verb'),
        ('weight', 'Noun'),
        ('weimaraner', 'Name'),
        ('westy', 'Name'),
        ('west_highland_white_terrier', 'Name'),
        ('welsh_corgi', 'Name'),
        ('wiener_dog', 'Name'),
        ('will', 'WQuestion'),
        ('with', 'Preposition'),
        ('what', 'What'),
        ('wheaten', 'Name'),
        ('when', 'WQuestion'),
        ('which', 'WQuestion'),
        ('whippet', 'Name'),
        ('who', 'WQuestion'),
        ('working', 'GroupName'),
    ],

    'v': [
        ('vizsla', 'Name')
    ],

    'y': [
        ('yorkie', 'Name'),
        ('yorkshire_terrier', 'Name'),
    ]
}


# dictionary that contains all of the syntax rules that PuppyChat recognizes
# keys are parent rules
# values are any possible:
#     word type that can singularly make an instance of the parent rule
#     pair of word types or syntax rules that can combine to make an instance of the parent rule
syntax_rules = {
    'S': [
        ('ADVP', 'S'),
        ('Greeting', 'S'),
        ('i\'m', 'Name'),
        ('NP', 'VP'),
        ('QP', 'VP'),
        ('S', 'ADJP'),
        ('S', 'ADVP'),
        ('S', 'PP'),
        ('WQuestion', 'NAP'),
        ('WQuestion', 'S'),
        ('WQuestion', 'VP'),
        ('Verb', 'NP'),
        ('Verb', 'Adverb'),
        ('VN', 'Verb')
    ],

    'VP': [
        ('Verb', 'Adjective'),
        ('Verb', 'NP'),
        ('Verb', 'PP')
    ],

    'NP': [
        ('Pronoun', 'N/A'),
        ('Name', 'N/A'),
        ('Noun', 'N/A'),
        ('Adjective', 'NP'),
        ('ADVP', 'NP'),
        ('Article', 'NP'),
        ('Determiner', 'Noun'),
        ('NP', 'Adjective'),
        ('NP', 'CN'),
        ('NP', 'ADJP'),
        ('GroupName', 'group'),
        ('GroupName', 'dogs')
    ],

    'ADVP': [
        ('Adverb', 'N/A'),
        ('Adverb', 'Adjective'),
        ('ADVP', 'ADVP'),
        ('Preposition', 'Noun'),

    ],

    'NAP': [
        ('NP', 'Adjective')
    ],

    'VN': [
        ('Verb', 'NP')
    ],

    'ADJP': [
        ('Adjective', 'PP')
    ],

    'PP': [
        ('Preposition', 'N/A'),
        ('Preposition', 'NP')
    ],

    'CN': [
        ('Conjunction', 'NP')
    ],

    'QP': [
        ('What', 'Noun'),
    ]
}
