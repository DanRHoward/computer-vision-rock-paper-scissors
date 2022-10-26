# Computer Vision RPS

### Initial download of the model

This project will use computer vision RPS modelling to create a computer version of the well-known game, 'Rock-Paper-Scissors'. The deep learning model's structure and labels found in files "keras_model.h5" and "labels.txt" were initially generated from the the website,

https://teachablemachine.withgoogle.com/

The classes defined which the machine was trainned to distinguish were the 3 different states of the game itself ('Rock', 'Paper' and 'Scissors') and the 'Nothing' state. The model used images of me gesturing in the appripriate manner corresponding to whcih class was being defined. For instance, a fist was held up to the camera when defining the 'Rock' class. 100 images of each state to allow for a more accurate prediction from the model.

We begin be creating the conda environment so that the machine lerning model we have can run. Within this environment, we imported the packages; opencv-python, tensorflow, and ipykernel. We achieved this by first installing 'pip' in the command prompt, then using this to install the other packages. This environment is named "rps_env" and was created with the following lines of code in the command prompt: 

```
conda create -n rps_env
```

After this, activate the environment and install the the desired packages using pip by:

```
pip install <package name>
```

### Manual version of the game

A manual version of the game was created which does not require the use of machine learning to gather an input from the player. Instead, the player types in their desired action when the file is run and they against the computer, who's decision is made at random before the player's. The code for this is found in the file named,
manual_rps.py. The logic of the game is based upon simple if-elif-else commands.
