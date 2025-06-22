# import random
# print("welcome to the higher lower game")
# score=0
# def format_data(account):
#     account_name=account['name']
#     account_descr=account['description']
#     account_country=account['country']
#     return f"{account_name}, {account_descr}, {account_country}"
# def check_answer(user_guess, a_followers, b_followers):
#     if a_followers > b_followers and user_guess == 'a':
#         return True
#     else:
#         return False
#
# data=[{'name':'dwayne johnson',
#        'follower_count':181,
#        'description':'actor and professional wrestler',
#        'country' : 'united states'},
#       {'name':'selena gomez',
#        'follower_count':251,
#        'description':'actor and professional wrestler',
#        'country' : 'united states'},
#       {'name': 'ronaldo',
#        'follower_count': 2501,
#        'description': 'actor and professional wrestler',
#        'country': 'united kingdom'},
#       {'name': 'stephen',
#        'follower_count': 1801,
#        'description': 'actor and professional wrestler',
#        'country': 'united states'},
#       {'name': 'tyler swift',
#        'follower_count': 1001,
#        'description': 'actor and professional wrestler',
#        'country': 'united states'},
#       {'name': 'NANI',
#        'follower_count': 1321,
#        'description': 'actor and professional wrestler',
#        'country': 'INDIA'},
#       {'name': 'RAM CHARAN',
#        'follower_count': 1451,
#        'description': 'actor and professional wrestler',
#        'country': 'INDIA'},
#       {'name': 'DULQUER SALMAN',
#        'follower_count': 4281,
#        'description': 'actor and professional wrestler',
#        'country': 'INDIA'},
#       {'name': 'PRABHAS',
#        'follower_count': 3126,
#        'description': 'actor and professional wrestler',
#        'country': 'INDIA'},
#       {'name': 'CHIRANJEEVI',
#        'follower_count': 1850,
#        'description': 'actor and professional wrestler',
#        'country': 'INDIA'},
#       {'name': 'PAWAN KALYAN',
#        'follower_count': 1283,
#        'description': 'actor and professional wrestler',
#        'country': 'INDIA'}
#       ]
# game_should_continue=True
#
# compare_B = random.choice(data)
# while game_should_continue:
#     compare_A=compare_B
#     compare_B=random.choice(data)
#
#     if compare_A==compare_B:
#         compare_B=random.choice(data)
#     print(f"compare A:{format_data(compare_A)}")
#     print(f"compare B:{format_data(compare_B)}")
#     guess=  input("who has more followers? type a or b")
#     print("\n*20")
#     a_follower_count=compare_A['follower_count']
#     b_follower_count=compare_B['follower_count']
#     is_correct=check_answer(guess, a_follower_count, b_follower_count)
# if is_correct:
#     score=score+1
#     print("you are right and your final score is:",score)
# else:
#     print("you are wrong\n final score is:",score)
#     game_should_continue=False
import random

print("Welcome to the Higher Lower Game!")
score = 0

def format_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

data = [
    {'name': 'Dwayne Johnson', 'follower_count': 181, 'description': 'actor and professional wrestler', 'country': 'United States'},
    {'name': 'Selena Gomez', 'follower_count': 251, 'description': 'singer and actress', 'country': 'United States'},
    {'name': 'Ronaldo', 'follower_count': 2501, 'description': 'footballer', 'country': 'Portugal'},
    {'name': 'Stephen', 'follower_count': 1801, 'description': 'actor', 'country': 'United States'},
    {'name': 'Taylor Swift', 'follower_count': 1001, 'description': 'singer-songwriter', 'country': 'United States'},
    {'name': 'Nani', 'follower_count': 1321, 'description': 'actor', 'country': 'India'},
    {'name': 'Ram Charan', 'follower_count': 1451, 'description': 'actor', 'country': 'India'},
    {'name': 'Dulquer Salman', 'follower_count': 4281, 'description': 'actor', 'country': 'India'},
    {'name': 'Prabhas', 'follower_count': 3126, 'description': 'actor', 'country': 'India'},
    {'name': 'Chiranjeevi', 'follower_count': 1850, 'description': 'actor', 'country': 'India'},
    {'name': 'Pawan Kalyan', 'follower_count': 1283, 'description': 'actor', 'country': 'India'}
]

game_should_continue = True
compare_B = random.choice(data)

while game_should_continue:
    compare_A = compare_B
    compare_B = random.choice(data)

    # Make sure A and B are not the same
    while compare_A == compare_B:
        compare_B = random.choice(data)

    print(f"\nCompare A: {format_data(compare_A)}")
    print("VS")
    print(f"Compare B: {format_data(compare_B)}")

    guess = input("Who has more followers? Type 'a' or 'b': ").lower()
    print("\n" + "*" * 20)

    a_follower_count = compare_A['follower_count']
    b_follower_count = compare_B['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
