class RockPaperScissors:
    def __init__(self,game_states,computer_wins=0,user_wins=0,end_game=False,time_interval=5):
        self.game_states = game_states
        self.computer_wins = computer_wins
        self.user_wins = user_wins
        self.end_game = end_game
        self.time_interval = time_interval

        # import cv2
        # from keras.models import load_model
        # import numpy as np
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    def get_prediction(self):
        import time
        import cv2
        from keras.models import load_model
        import numpy as np
        start_time = time.time()
        while True: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): #Checks if player presses 'q' key to end game early
                self.end_game = True #Reasigns vale to 'True'
                break

            player_choice = self.game_states[np.argmax(prediction)] #Player's choice is the most likely prediction of game states from the model
            if abs(start_time - time.time()) >= self.time_interval: #checks if the time interval exceeds criticl value
                if player_choice == 'nothing': #In case model cannot destinguish any playable state
                    print('Unable to determine your choice! Please try again.')
                    start_time = time.time() #Resets start time
                else:
                    print(f'You chose {player_choice}.')
                    break
    
    def get_computer_choice(self):
        import random
        while True:
            computer_choice = random.choice(self.game_states)
            if computer_choice != 'nothing': #So as to deny the computer choosing the 'nothing' class
                break
        return computer_choice
    
    def get_winner(self,computer_choice,player_choice): #Logic of the game is defined here
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
    game_states = ['nothing','rock','paper','scissors'] #All possible states for the player
    game = RockPaperScissors(game_states)
    while True:
        if game.computer_wins != 3 and game.user_wins !=3: #If either player has correct number of wins, continue the game
            game.computer_choice = game.get_computer_choice()
            game.player_choice = game.get_prediction()
            game.winner = game.get_winner(game.computer_choice,game.player_choice)
            if game.end_game == True: #If play presses 'q' key during game, end the game
                print('The game has stopped.')
                break
            elif game.winner == 'neither': #If round is a draw
                print('The round is a draw!')
            elif game.winner == 'the user': #If the user wins round
                print('You won that round!')
                game.user_wins += 1 
            else: #If the computer wins round
                print('The computer won that round!')
                game.computer_wins += 1
        elif game.computer_wins == 3: #If computer gets 3 wins, computer wins the game
            print('The computer wins!')
            break
        else: #If the user gets 3 wins, the user wins
            print('You win!!!')
            break

play()