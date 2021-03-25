# PuppyChat.py
# runs the PuppyChat program
# also contains helper functions meant to test PuppyChat against all possible questions
# Anthony de Bem 2021

import Interpret
import Dogs

# pieces together a every possible singular question about every possible dog and enters it to PuppyChat
def individualQuestions():
    question_types = {
        'temperament': 'How do {}s behave?',
        'height': 'How tall are {}s?',
        'weight': 'How much do {}s weigh?',
        'lifespan': 'How long do {}s live',
        'group': 'What group are {}s in?',
        'description': 'Describe {}s.'

    }

    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$ INDIVIDUAL QUESTIONS $$$$$$$$$$$$$$$$$$$$$$$$$$')

    for typ, question in question_types.items():
        print(f'________Individual {typ}_________')

        for index in Dogs.dogInfo.values():
            for dog in index.keys():
                proper_name = dog.replace('_', ' ')
                print(question.format(proper_name))
                yield question.format(proper_name)

                if typ == 'description':
                    print('Describe more.')
                    yield 'Describe more.'
        print()


# pieces together a every possible one-to-all comparison for every single dog and enters it to PuppyChat
def broadQuestions():
    question_types = {
        'height': ['What dogs are taller than {}s?', 'What dogs are shorter than {}s?'],
        'weight': ['What dogs weigh more than {}s?', 'What dogs weigh less than {}s?'],
        'lifespan': ['What dogs live longer than {}s?', 'What dogs live shorter than {}s?'],
        'group': ['What dogs are in the same group as {}s?']
    }

    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$ BROADER QUESTIONS $$$$$$$$$$$$$$$$$$$$$$$$$$')

    for index in Dogs.dogInfo.values():
        for dog in index.keys():
            print(f'________Comparing {dog}_________')
            proper_name = dog.replace('_', ' ')
            for typ in question_types.keys():
                for question in question_types[typ]:
                    print(question.format(proper_name))
                    yield question.format(proper_name)
            print()

    for group_name in {'sporting', 'hound', 'working', 'terrier', 'toy', 'non-sporting', 'herding'}:
        response = 'what dogs are in the {} group?'.format(group_name)
        print(response)
        yield response


# pieces together every possible one-to-one comparison between every single dog in every order and enters it to PuppyChat
def comparisonQuestions():
    dog_list = []

    question_types = {
        'height': ['Are {}s taller than {}s?', 'Are {}s shorter than {}s?'],
        'weight': ['Do {}s weigh more than {}s?', 'Do {}s weigh less than {}s?'],
        'lifespan': ['Do {}s live longer than {}s?', 'Do {}s live shorter than {}s?'],
        'group': ['Are {}s in the same group as {}s?', 'Are {}s in a different group than {}s?']
    }

    print(f'$$$$$$$$$$$$$$$$$$$$$$$$$$ COMPARISON QUESTIONS $$$$$$$$$$$$$$$$$$$$$$$$$$')

    for index in Dogs.dogInfo.values():
        dog = ''
        for dog in index.keys():
            print(f'________Comparing {dog}_________')

            for c_index in Dogs.dogInfo.values():
                for comparator_dog in c_index.keys():
                    if comparator_dog not in dog_list:
                        for typ in question_types.keys():
                            for question in question_types[typ]:
                                proper_name = dog.replace('_', ' ')
                                comparator_name = comparator_dog.replace('_', ' ')

                                print(question.format(proper_name, comparator_name))
                                yield question.format(proper_name, comparator_name)
            print()
        if dog != '':
            dog_list.append(dog)


# tests every:
#     singular dog question
#     one-to-all comparison
#     one-to-one comparison
def test():
    for singular_question in individualQuestions():
        Interpret.respond(singular_question)

    for broad_question in broadQuestions():
        Interpret.respond(broad_question)

    for comparison_question in comparisonQuestions():
        Interpret.respond(comparison_question)


# checks if the user wants to debug or test
# prompts the user with a question until the user says a keyword denoting a 'goodbye'
if __name__ == '__main__':
    print('\nWelcome to PuppyChat! This is a project meant to showcase my skills in the python programming language.\n'
          'PuppyChat intelligently answers trivia questions about the American Kennel Club\'s top 60 most popular dog\n'
          'breeds from 2019. You can ask about specific dogs, compare two dogs, or even compare one dog to the rest.\n'
          '\nNOTE: All of the dog breed information is sourced from the American Kennel Club\'s Website.\n'
          '      None of the information supplied is mine.\n\n')
    user_input = input('Hello! I\'m the PuppyBot! Any dog questions?\n\n')

    while Interpret.notGoodbye(user_input):
        if user_input == 't':
            test()
            break
        else:
            Interpret.respond(user_input)
            user_input = input()
