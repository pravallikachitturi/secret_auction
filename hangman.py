import random
word_list=["pencil", "umbrella","television", "badminton"]
computer_word=random.choice(word_list)
print(computer_word)
gameover=False
while not gameover:
    guess=input("guess a letter : ").lower()
    print(guess)
placeholder=""
for position in range(0,len(computer_word)+1):
    placeholder+="_"
print(placeholder)
display=""
for letter in computer_word:
    if letter==guess:
        display +=letter
    else:
        display += "_"
print(display)
    # while computer_word.count(letter)>1:
    #     input("guess a letter: ")
    #     if letter in computer_word:
    #         print("correct")
    #      else:
    #         print("wrong")