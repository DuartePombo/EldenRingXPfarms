# EldenRingXPfarms
Using Python + Computer Vision to automate rune farming in Elden Ring


This is a Python bot that will farm indefinitly the red goblins that are chilling at Palace Ledge and has an AI vision implementation so it is extremely reliable and you do not lose all your runes during night.

### :::::::::::::::::::::::::::::::::::::::::::::::: IMPORTANT :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

This bot is an automation of the rune farm: https://www.youtube.com/watch?v=a1jFy_alp9s Therefore you need to have the sacred relic sword.

You also need to have in the key bindings, the H key set to "Move Camera / Change Target (Left)"

Also, when running the bot, you will likely prefer to have the screen windowed with a low resolution, but you have to keep at least the top right corner of the elden ring window visible. This is because the bot saves a screenshot in memory of the top right corner of the window, to understand if it is inside the map menu or not and correct itself in case the input fails for some reason (and that way does not continue and runs off the cliff).

This is an adapted code and with an added AI implementation of the repository: https://github.com/AdamBissonnette/elden-ring-bot , thank you so much Adam Bissonnette for saving me some time getting me a part of the bot framework already done. You can check more info regarding his bot also in this link: https://medium.com/@IamTheNight/writing-a-bot-for-elden-ring-b7b10aebf6e2
Also, I highly recommend this, because he explains clearly how to set this up and the requirements for this to work.

This implementation does the same thing that Adam's bot does but has slighty optimized character positioning and has much better consistency due to capability of recognizing if successfuly entered the map menu or not when attempting to teleport back to palace ledge.

The problem with the original bot was that sometimes, due to the game freezing, the input of entering the map would not go through, and the bot would continue it's procedure and just run even farther ahead and fall into the cliff, losing all the runes. Basicly would be a bit unrealiable to leave it over night because there was a not low change the bot would just fail at some point and you would lose all your runes.

Therefore, besides improving the characters positioning to slay the goblins, I developed a CNN that takes a screenshot in memory of the top right corner of the elden ring window. And If it detects the compass, that means it is inside the map menu, and can continue it's teleport procedure. This is done during all the teleport process, so you can test it yourself and when the bot clicks to teleport, you can click q to go back and you will see the bot realizing he is not on the map menu and will insist to get back to the map menu and will successfuly perform the teleportation.

Notice that the repository also has a lot of files and folders that are not needed to run the bot. If you are interested, you can check how the CNN model was constructed in the CNN.ipynb and you can also peek into the Data folder, where you have all the train and test data that was used to train the model.


For this code to work, you need to have installed the following packages:

numpy==1.23.5
tensorflow==2.12.0
PyGetWindow==0.0.9
Pillow==9.4.0
pywin32==303
pywin32-ctypes==0.2.0

you probably need additional packages if you want to run the CNN.ipynb, but just install as you go if you want to.



