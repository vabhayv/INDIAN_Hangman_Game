import random

lives = [''' 

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=============      

''', '''

 +---+
  |   |
  O   |
 /|\  |
   \  |
      |
=============  

''', '''

 +---+
  |   |
  O   |
 /|\  |
      |
      |
=============  

''', '''

 +---+
  |   |
  O   |
 /|   |
      |
      |
=============  

''', '''

 +---+
  |   |
  O   |
      |
      |
      |
=============  

''', '''

 +---+
  |   |
      |
      |
      |
      |
=============  

''' ]

print("Welcome to the Indian Hangman Game")
input("Guess the name of The State or The Union Territory of INDIA!!\n**Note: Spacebar is also a choice.** \nTap enter to continue. \n")

states = [
    'ANDHRA PRADESH', 'ARUNACHAL PRADESH', 'ASSAM', 'BIHAR', 'CHHATTISGARH', 'GOA', 'GUJARAT',
    'HARYANA', 'HIMACHAL PRADESH', 'JHARKHAND', 'KARNATAKA', 'KERALA', 'MADHYA PRADESH', 'MAHARASHTRA',
    'MANIPUR', 'MEGHALAYA', 'MIZORAM', 'NAGALAND', 'ODISHA', 'PUNJAB', 'RAJASTHAN', 'SIKKIM', 'TAMIL NADU',
    'TELANGANA', 'TRIPURA', 'UTTAR PRADESH', 'UTTARAKHAND', 'WEST BENGAL', 'ANDAMAN AND NICOBAR ISLANDS',
    'CHANDIGARH', 'DADRA AND NAGAR HAVELI AND DAMAN AND DIU', 'LAKSHADWEEP', 'DELHI', 'PUDUCHERRY',
    'JAMMU & KASHMIR', 'LADAKH'
]


random_state = random.choice(states)

selected_state = []
for i in range(len(random_state)):
    selected_state += "_"

print(selected_state)

lifes = 5
game_end = False
while not game_end :
    
    user_input = input("\n\n\n\nGuess the letter : ").upper()
    if user_input in selected_state :
        print(f"You have already entered '{user_input}'. ")
    
    
    for position in range(len(random_state)):
        if user_input==random_state[position]:
            selected_state[position] = user_input
    if user_input not in random_state:
        lifes -= 1
        print(f"'{user_input}' is not in the answer.")
        
    print(f"{lives[lifes]}")
    print(f"{selected_state}\n")
    print(f"You have {lifes} lifes left.\n")

    
    if "_" not in selected_state:
        game_end = True
        print("You Won")
    elif lifes == 0:
        game_end = True
        print(f"You lose\n\nAnswer was {random_state}")
        
    
    
    
    
    
    
    
    
    






