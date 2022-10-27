import time
import random

import cv2
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

game_states = ['nothing','rock','paper','scissors']
end_game = False #Checks if the player want to exit the game ()

def get_prediction():
    time_interval = 5 #In seconds
    start_time = time.time()
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            global end_game
            end_game = True
            break

        player_choice = game_states[np.argmax(prediction)]
        if abs(start_time - time.time()) >= time_interval:    
            if player_choice == 'nothing':
                print('Unable to determine your choice! Please try again.')
                start_time = time.time()
            else:
                print(f'You chose {player_choice}.')
                break
        
def get_computer_choice():
    while True:
        computer_choice = random.choice(game_states)
        if computer_choice != 'nothing':
            break
    return computer_choice

def get_winner(computer_choice,player_choice):
    if computer_choice == 'rock':
        if player_choice == 'rock':
            winner = 'neither'
        elif player_choice == 'paper':
            winner = 'the user'
        else:
            winner = 'the computer'
    elif computer_choice == 'paper':
        if player_choice == 'rock':
            winner = 'the computer'
        elif player_choice == 'paper':
            winner = 'neither'
        else:
            winner = 'the user'
    else:
        if player_choice == 'rock':
            winner = 'the user'
        elif player_choice == 'paper':
            winner = 'the computer'
        else:
            winner = 'neither'
    return winner

def play():
    computer_wins = 0
    user_wins = 0
    while True:
        if computer_wins != 3 and user_wins !=3:
            computer_choice = get_computer_choice()
            player_choice = get_prediction()
            winner = get_winner(computer_choice,player_choice)
            if end_game == True:
                print('The game has stopped.')
                cap.release()
                cv2.destroyAllWindows()
                break
            elif winner == 'neither':
                print('The round is a draw!')
            elif winner == 'the user':
                print('You won that round!')
                user_wins += 1 
            else:
                print('The computer won that round!')
                computer_wins += 1
        elif computer_wins == 3:
            cap.release()
            cv2.destroyAllWindows()
            print('The computer wins!')
            break
        else:
            cap.release()
            cv2.destroyAllWindows()
            print('You win!!!')
            break

play()