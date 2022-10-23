# Computer Vision RPS

### Initial download of the model

This project will use computer vision RPS modelling to create a computer version of the well-known game, 'Rock-Paper-Scissors'. The deep learning model's structure and labels found in files "keras_model.h5" and "labels.txt" were initially generated from the the website,

https://teachablemachine.withgoogle.com/

The classes defined which the machine was trainned to distinguish were the 3 different states of the game itself ('Rock', 'Paper' and 'Scissors') and the 'Nothing' state. The model used images of me gesturing in the appripriate manner corresponding to whcih class was being defined. For instance, a fist was held up to the camera when defining the 'Rock' class. 100 images of each state to allow for a more accurate prediction from the model.
