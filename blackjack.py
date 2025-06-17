import random
def deal_card():

    cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(cards)
    return card
def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)> 21:
        cards.remove(11)
        cards.append(10)
    return sum(cards)
def compare(u_score, c_score):
    if u_score==c_score:
        print("Its a draw")
    elif c_score==0:
        print("you win")
    elif u_score>21:
        print("you lose")
    elif c_score>21:
        print("you win")
    else:
        print("you lose")
def play_game():
    user_card=[]
    computer_card=[]
    computer_score= -1
    user_score= -1
    is_game_over=False
    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"your cards: {user_card}, current score: {user_score}")
        print(f" computer's first card: {computer_card[0]}")
        if user_score > computer_score:
            print("you win")
        if user_score==0 or computer_score ==0 or user_score > 21:
            is_game_over=True
        else:
            another_card = input("Do you want to play another card? Type 'yes' or 'no': ").lower()
            if another_card == "yes":
                user_card.append(deal_card())
            else:
                is_game_over=True
    while computer_score !=0 and computer_score <17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"your final hand: {user_card}, final score: {user_score}")
    print(f"computer final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("do you wnat to play a game of  blackjack? Type 'yes' or 'no': ")=='yes':
    play_game()









