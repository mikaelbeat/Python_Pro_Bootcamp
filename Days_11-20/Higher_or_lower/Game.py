
import Art, Game_data, random
from replit import clear

clear()
#print(Art.logo)


def select_random_person():
    person = random.choice(Game_data.data)
    return person
    
def show_question(a, b):
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(f"Followers - {a['follower_count']}")
    print(Art.vs)
    print(f"Compare B: {b['name']}, {b['description']}, from {b['country']}")
    print(f"Followers - {b['follower_count']}")
    

def return_random_persons():
    personA = select_random_person()
    personB = select_random_person()
    while personB['name'] == personA['name']:
        personB = select_random_person()
    return personA, personB


def return_new_person(old_person):
    person = select_random_person()
    while old_person['name'] == person['name']:
        person = select_random_person()
    return person

    
def play_game():
    
    correct = True
    score = 0
    
    personA, personB = return_random_persons()
    
    while correct:
        clear()
        personA_followers = personA['follower_count']
        personB_followers = personB['follower_count']
        print(f"Current score: {score}")
        show_question(personA, personB)
        guess = input("\nGuess which has more Instagram followers, A or B? ")
        if guess == "a" and personA_followers > personB_followers:
            print("\nCorrect!")
            score += 1
            #personA = return_new_person(personA)
            personA = personA
            while personB != personA:
                personB = return_new_person(personB)
        elif guess == "b" and personB_followers > personA_followers:
            print("\nCorrect!")
            score += 1
            personA = personB
            while personB != personA:
                personB = return_new_person(personA)
        else:
            print("\nWrong, game over!")
            print(f"You got {score} right.")
            correct = False
            
    return score


score = play_game()


