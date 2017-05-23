# Py-Tron

1.	Install Python 2.7.5 from https://www.python.org/ 
2.	Install Pygame for Python 2.7 from http://www.pygame.org/download.shtml
3.	Follow the instructions for your current Operative System (Windows, Mac or Linux)
4.	Open PYTRON.py from the PYTRON folder
5.	Run PYTRON.py from IDLE

PYTRON GAME DESCRIPTION
 Pytron is a two-player game, based on the 80’s Disney movie Tron. During a match each player controls a “Light Cycle”, a virtual motorcycle represented by a line that grows in length over a plane.  The objective is to outmaneuver the other player by blocking their path with the trail left by each line, which in turn creates an obstacle for both players.

The structure of the game consists of four stages, 1) an introduction, 2) a match, 3) the result of the match, and 4) a conclusion. At each stage different screens are shown, adding up to a total of eight screens. Every time a user runs Pytron the typical sequence would be the following:

First, an introductory screen is displayed showing a looped animation of a blue Light Cycle, which indicates the user to press the spacebar. The title of the game (“Pytron”) is shown as well.  During this screen, if the key “c” is pressed, the credits screen is displayed for four seconds showing the names of the team members as well as the authors of the music used throughout the game.

After the spacebar is pressed the instructions screen is displayed describing the controls for player 1 (P1) and player 2 (P2). Again, the user is indicated to continue by pressing the space bar. Additionally, during these two initial screens, the song “Son of Flynn” by Daft Punk plays on the background. 

When a match begins, the song playing on the background changes to “Derezzed” also by Daft Punk, and the lines for both players start at equidistant positions on the plane, i.e. P1 starts on the middle of the left side and P2 on the middle of the right size. Simultaneously, they automatically start moving towards the center of the plane forcing them to move in order to avoid a crash. If at any given point both players crash against an object (another player, a border, or with themselves) at the same time, a tie occurs. In this case, an image of two Light Cycles clashing with each other and the message: “End of line” is shown. However, if only one of the players crashes with an object, then another image displaying the winner is shown (one image for P1 if that’s the case, and vice versa). 

The users can play as many matches as they want, however if they wish to quit the game, they can simply press “q” every time any of the three screens described above is shown (tie, P1 wins, P2 wins). When doing so, yet another screen is displayed showing an image of some characters of the Tron movie and the message: “Thanks for playing”, then after two seconds the whole window closes, hence concluding the game. 
