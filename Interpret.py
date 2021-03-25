# Interpret.py
# Gathers information from the user input necessary for constructing an intelligent response.
# Anthony de Bem 2021

import Dogs
import Responses
import DogParse
import Grammar

# the information that PuppyChat needs to remember in order to properly answer the question
topics = {
    'user': str(),
    'previous_dog1': None,
    'previous_dog2': None,
    'dog1': None,
    'dog2': None,
    'subject': None,
    'description_detail': 0,
    'compare': False,
    'comparison_keyword': None,
    'what/which': False
}

disclaimer = "According to the American Kennel Club:\n"
first_question = True
response = ''
parse_tree = dict()
sentence = None
debug = False

# true if the user input is a 'bye', 'goodbye', or 'farewell', false otherwise
def notGoodbye(userInput):
    if len(userInput) > 0:
        if not userInput[-1].isalpha():
            userInput = userInput[:-1]

        first_word = userInput.lower().split(' ')[0]
        if first_word in {'bye', 'goodbye', 'farewell'}:
            if topics['user']:
                print(f'Goodbye {topics["user"]}!')
            else:
                print(f'Goodbye!')
            return False
        else:
            return True

# meant for debugging, prints all of the info that PuppyChat knows about the given sentence
def printTopics():
    print("topics:")
    print(f"    user: {topics['user']}")
    print(f"    previous_dog1: {topics['previous_dog1']}")
    print(f"    previous_dog2: {topics['previous_dog2']}")
    print(f"    dog1: {topics['dog1']}")
    print(f"    dog2: {topics['dog2']}\n")
    print(f"    subject: {topics['subject']}")
    print(f"    description_detail: {topics['description_detail']}")
    print(f"    compare: {topics['compare']}")
    print(f"    comparison_keyword: {topics['comparison_keyword']}")
    print(f"    what: {topics['what/which']}")


# if there is a sentence tree in the parse tree, return the biggest sentence tree
def getSentenceTree():
    possible_trees = [t for t in list(parse_tree.values()) if (t.rule == 'S')]

    try:
        biggest_sentence, max_len = possible_trees[0], possible_trees[0].length()
    except IndexError:
        return None

    for possible_tree in possible_trees[1:]:
        if possible_tree.length() >= max_len:
            biggest_sentence, max_len = possible_tree, possible_tree.length()

    return biggest_sentence


# returns a dog name if the given name is a valid dog name
# returns nothing otherwise
def getDogName(name):

    # first, we find the first letter of the given name and get that index
    first_letter = name[0].lower()
    if first_letter in list(Dogs.dogInfo.keys()):
        name_index = Dogs.dogInfo[first_letter]

        # then, we search all dog names and nicknames in that index for the name of the dog
        for dog_name, dog_info in name_index.items():
            if name == dog_name:
                return name
            elif ('nicknames' in dog_info.keys()) and (name in dog_info['nicknames']):
                return dog_name

        # if the name wasn't in that list, check the nicknames of every dog not that list
        for index in Dogs.dogInfo.keys():
            for dog_name, dog_info in Dogs.dogInfo[index].items():
                # skip the index that we already searched through and only check the nicknames
                if (index != name[0].lower()) and ('nicknames' in dog_info.keys()) and (name in dog_info['nicknames']):
                    return dog_name


# saves the dog name in whatever place is available
def addDog(name):
    if topics['dog1']:
        topics['dog2'] = name
    else:
        topics['dog1'] = name


# finds if there is a keyword to be saved from a given word
# keywords need to be remembered for comparison questions
def findKeyword(word):
    # 'shorter' is a special case: if the subject is also 'lifespan', then we save a special comparison keyword
    if (word == 'shorter') and (topics['subject'] == 'lifespan'):
        topics['comparison_keyword'] = 'shorter minimum life expectancy'

    # otherwise, different words imply different question subjects
    # certain words also warrant saving certain comparison keywords
    elif word in {'behave', 'act', 'personality', 'behavior'}:
        topics['subject'] = 'temperament'

    elif word in {'tall', 'taller', 'short', 'shorter'}:
        topics['subject'] = 'height'
        if word in {'taller', 'shorter'}:
            topics['comparison_keyword'] = word

    elif word in {'weigh', 'weighs', 'heavy', 'heavier', 'lighter'}:
        topics['subject'] = 'weight'
        if word == 'heavier':
            topics['comparison_keyword'] = 'more'
        elif word == 'lighter':
            topics['comparison_keyword'] = 'less'

    elif word in {'live', 'lives', 'longer'}:
        topics['subject'] = 'lifespan'
        if (not (topics['subject'] and topics['subject'] != 'lifespan')) and word == 'longer':
            topics['comparison_keyword'] = 'longer maximum life expectancy'

    elif word in {'describe', 'summarize, summary', 'description'}:
        topics['subject'] = 'description'


# gathers information from the sentence tree
def processTree(sentence_tree):
    global topics, response

    leaves = sentence_tree.leaves()
    name_given = False

    # analyses each word in the tree
    for wordType, word in leaves:

        is_question_word = (word in {'temperament', 'height', 'weight', 'lifespan', 'group', 'description'})

        # if the user enters a question word or asks about a specific group
        # then the word given is the subject of the question
        if (wordType == 'group') or is_question_word:
            topics['subject'] = word
            continue

        # important if the following word is 'dogs'
        # if the user entered 'what/which dog(s)/breed(s)', then they want one-to-all comparison
        if word in {'what', 'which'}:
            topics['what/which'] = True

        # if 'dogs' doesn't follow 'what/which', forget that they typed 'what/which'
        elif (word not in {'dog', 'dogs', 'breed', 'breeds'}) and topics['what/which']:
            topics['what/which'] = False

        # all-to-one comparison if the user entered 'who' or 'what dogs'
        elif (word == 'who') or ((word in {'dog', 'dogs', 'breed', 'breeds'}) and topics['what/which']):
            addDog('ALL')

        # remember the keyword if the user wants to compare groups
        elif (wordType == 'GroupName') or (word in {'same', 'different'}):
            topics['comparison_keyword'] = word

        #  remember the keyword if the user wants to compare weight
        elif (topics['subject'] == 'weight') and (word in {'more', 'less'}):
            topics['comparison_keyword'] = word

        # remember the previous dog if the user types 'they', 'those', or 'them'
        elif (wordType == 'Pronoun') and (word in {'they', 'those', 'them'}):
            addDog(topics['previous_dog1'])

        # if the user entered a name
        elif wordType == 'Name':
            name = getDogName(word.title())
            if name:  # if it's a valid dog name, save that dog's name
                addDog(name)
            elif response == '':  # if not, save it as the user's name and remember that the user's name was given
                name_given = True
                topics['user'] = word.title()

        # if the user entered a preposition
        elif wordType == 'Preposition':
            if word == 'like':
                topics['subject'] = 'temperament'
            if word == 'than':
                topics['compare'] = True

        # if the user entered an adjective, verb, or a noun
        # find if there is a keyword to be saved
        if wordType in {'Adjective', 'Verb', 'Noun'}:
            findKeyword(word)

    # if the user only mentioned their name
    if name_given and (not topics['subject']) and (not topics['dog1']):
        response += 'Hi, {}!\n'.format(topics['user'])


# if the sentence is valid
#     parses the sentence
#     finds a sentence tree
#     gathers information from the tree
# returns false otherwise
def parseQuestion(question):
    global parse_tree

    words = [word for word in question.split(' ') if (word != '')]

    if len(words) > 1:
        # updates the parse tree
        parse_tree = DogParse.parse(words, Grammar.dictionary, Grammar.syntax_rules)

        try:
            # finds the sentence tree if possible
            sentence_tree = getSentenceTree()
            if sentence_tree:
                # gathers information from that sentence tree
                processTree(sentence_tree)
                return True
            else:
                return False
        except ValueError:
            return False


def findDogs():

    # finds the subject dog for the comparison (if there is one)
    if topics['dog1'] and (topics['dog1'] != 'ALL'):
        subject_dog = topics['dog1']
    elif topics['dog2'] and (topics['dog2'] != 'ALL'):
        subject_dog = topics['dog2']
    else:
        subject_dog = None

    group_names = {'sporting', 'hound', 'working', 'terrier', 'toy', 'non-sporting', 'herding'}
    higher_keywords = {'taller', 'more', 'longer maximum life expectancy'}
    lower_keywords = {'shorter', 'less', 'shorter minimum life expectancy'}

    # finds how the user wants to compare
    keyword = ''
    if topics['comparison_keyword'] in group_names:
        return Responses.dogsInGroup(topics['comparison_keyword'])
    if topics['comparison_keyword'] in higher_keywords:
        keyword = 'higher'
    elif topics['comparison_keyword'] in lower_keywords:
        keyword = 'lower'
    elif topics['comparison_keyword'] == 'same':
        keyword = topics['comparison_keyword']

    attr_question = ((topics['subject'] in {'height', 'weight', 'lifespan'}) and (keyword in {'higher', 'lower'}))
    group_question = ((topics['subject'] == 'group') and (keyword == topics['comparison_keyword']))

    # returns a response only if the user wants asks about attributes or group membership
    if attr_question or group_question:
        return Responses.findDogs(topics['subject'], subject_dog, keyword)
    else:
        return ''

# calls a helper function to get a response depending on the subject
def singularResponse(dog_name, proper_name):
    global response

    if topics['subject'] == 'temperament':
        response += Responses.getTemperament(dog_name, proper_name)

    elif topics['subject'] == 'description':
        topics['description_detail'] += 1
        response += Responses.getDescription(dog_name, topics['description_detail'])

    elif topics['subject'] in {'height', 'weight', 'lifespan', 'group'}:
        response += Responses.singularQuestion(dog_name, proper_name, topics['subject'])

    return response


def pickResponse():
    global response

    if topics['subject']:
        # if there are two subject dogs and the subject is group, then we compare
        if topics['dog2'] and (type(topics['subject']) == str) and (topics['subject'] == 'group'):
            topics['compare'] = True

        # if we remember two previous dogs:
        if topics['previous_dog1'] and topics['previous_dog2']:

            # if no new dog was mentioned, then we keep the last subject dog
            if not topics['dog1']:
                topics['dog1'] = topics['previous_dog1']

            # if no second dog was mentioned, then we remember a previous dog
            if not topics['dog2']:
                if topics['dog1'] != topics['previous_dog1']:
                    topics['dog2'] = topics['previous_dog1']
                else:
                    topics['dog2'] = topics['previous_dog2']

        # if we want a description and no new dog was mentioned, then we keep the last subject dog
        if (topics['subject'] == 'description') and (not topics['dog1']) and (topics['previous_dog1']):
            topics['dog1'] = topics['previous_dog1']

        # if a new dog was mentioned:
        if topics['dog1']:

            # if that new dog isn't the last subject dog
            # we only describe at the most basic detail
            if topics['previous_dog1'] != topics['dog1']:
                topics['description_detail'] = 0

            dog_name = topics['dog1']
            proper_name = dog_name.replace('_', ' ')

            # pick a comparison
            if 'ALL' in (topics['dog1'], topics['dog2']):  # one-to-all comparison
                response += findDogs()

            elif topics['compare'] and topics['dog2']:  # one-to-one comparison
                if topics['dog1'] == topics['dog2']:  # make sure we're not comparing the same dog
                    response += 'They\'re the same dog!\n'
                else:
                    dog_name2 = topics['dog2']
                    proper_name2 = dog_name2.replace('_', ' ')
                    response += Responses.compare(dog_name, proper_name, dog_name2, proper_name2, topics['subject'],
                                                  topics['comparison_keyword'])

            elif not topics['compare']:  # no comparison
                response += singularResponse(dog_name, proper_name)

    return response


def resetTopics():
    global response, parse_tree, sentence

    topics['previous_dog1'] = topics['dog1']
    topics['previous_dog2'] = topics['dog2']

    topics['dog1'] = None
    topics['dog2'] = None
    topics['subject'] = None
    topics['compare'] = None
    topics['comparison_keyword'] = None
    topics['what/which'] = False

    response = ''
    parse_tree = dict()
    sentence = None

# for each question:
#     parses the user's question
#     picks a response
# afterwords, resets the topics
def respond(user_input):
    global topics, response, first_question

    questions = [q for q in user_input.lower().replace('.', '?').split('?') if q]

    for question in questions:
        parsed = parseQuestion(question)

        if parsed:
            pickResponse()

        if response == '':
            print('Sorry, I don\'t understand. Can you ask again?\n\n')
        else:
            if first_question:
                # always disclaim in the first response that the American Kennel Club is the source of the information:
                if 'American Kennel Club' not in response:
                    response = disclaimer + response
                first_question = False
            print(response)

        resetTopics()
