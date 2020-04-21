# JetpackJoyride
This is an amazing implementation of a subset of the Jetpack Joyride game. This is implemented from scratch without use of PyGame library. Only numpy and colorama are the major libraries used. All characters of the game are made using ASCII characters. You will most probably enjoy it smiley.

# Running
1. Install the requirements using command : pip3 install requirements.txt
2. Run game using python3 main.py

# Instructions
1.WAD to move.                     
2.Fire Bullets with F.                       
3.Activate shield with Space.                                                                                                   
4.You get 3 lives in the game.                                                                                                 
5.Increase your score by taking coins,hitting fire-beams and killing enemies.                                                   
6.Grab the Speed-Boost Powerup by jumping on it.                                                                               
7.You can become a dragon too by taking Special Dragon Powerup.                                                                
8.Kill the final Boss-Enemy to win the game.


![alt text](https://github.com/DivanshiGupta/JetpackJoyride/blob/master/IMG_20200421_165822.jpg)


![alt text](https://github.com/DivanshiGupta/JetpackJoyride/blob/master/IMG_20200421_165856.jpg)


# Assignment related stuff
1. Polymorphism - both player and dragon have the fire_laser but it behaves differently in both of them, however, it is fired in the same way.
2. Inheritance - both player and bossenemey are inherited from same parent class character
3. Encapsulation - all variables are protected and they have getters and setters.
4. Abstraction - functions like check_collision and fire_laser hide underlying implementation and can be used in whatever way since it always works the way you want it to.
