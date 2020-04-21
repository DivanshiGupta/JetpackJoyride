# from objects import *
from colorama import Fore, Back, Style
import random

class Character :
    def __init__(self,x,y):
        self.x=x
        self.y =y
        
class Batman(Character) :
    def __init__(self,x,y,score,lives,time_of_flight,dragon_mode,dragon_count):
        # self.x=x
        # self.y =y
        self.score=score
        self.lives =lives
        self.time_of_flight = time_of_flight
        self.dragon_mode = dragon_mode
        self.dragon_count = dragon_count
        super().__init__(x,y)

    def batman_pos(self,matrix,shield):
        n1 = self.x
        n2 = self.y
        if self.dragon_mode == 0:
            if shield.status ==1 :
                    
                matrix[n1][n2+1]=Fore.MAGENTA + '0'
                matrix[n1+1][n2]=Fore.MAGENTA +'/'
                matrix[n1+1][n2+1]=Fore.MAGENTA +'Y'
                matrix[n1+1][n2+2]=Fore.MAGENTA +'\\'
                matrix[n1+2][n2]=Fore.MAGENTA +'/'
                matrix[n1+2][n2+2]=Fore.MAGENTA +'\\'
            else :

                matrix[n1][n2+1]=Fore.BLUE + '0'
                matrix[n1+1][n2]=Fore.BLUE +'/'
                matrix[n1+1][n2+1]=Fore.BLUE +'Y'
                matrix[n1+1][n2+2]=Fore.BLUE +'\\'
                matrix[n1+2][n2]=Fore.BLUE +'/'
                matrix[n1+2][n2+2]=Fore.BLUE +'\\'
        else :
            if self.x > 21:
                self.x = 21
            Matrix1 = [[0 for x in range(1000)] for y in range(1000)]  # h == no of rows ; w == no of columns
            dragon_count = self.dragon_count
            if dragon_count == 0:
                f = open("dragon1.txt", "r")
            if dragon_count == 1:
                f = open("dragon2.txt", "r")
            if dragon_count == 2:
                f = open("dragon3.txt", "r")
            if dragon_count == 3:
                f = open("dragon4.txt", "r")
            if dragon_count == 4:
                f = open("dragon5.txt", "r")
            if dragon_count == 5:
                f = open("dragon6.txt", "r")
            self.dragon_count += 1
            if self.dragon_count == 6:
                self.dragon_count = 0 
            xi = 0
            mx = -1
            for x in f:
                yi = 0
                y2 =0
                for y in x:
                    y2 +=1
                for y in x :   
                    Matrix1[xi][yi] = y
                    yi+=1
                    if yi == y2 -1 :
                        break
                    if yi > mx:
                        mx = yi
                xi+=1
            i1=0
            j1=0
            for i in range(self.x,self.x+xi) :
                j1= 0
                for j in range(self.y,self.y+mx+1):
                    # u = random.randint(0,1)
                    if Matrix1[i1][j1] != 0:
                        if shield.status == 1:
                            matrix[i][j]=Fore.MAGENTA + Matrix1[i1][j1]
                        else :
                            matrix[i][j]=Fore.BLUE + Matrix1[i1][j1]
                    j1+=1
                i1+=1    
        
    def batman_collision(self,matrix):
        n1 = self.x
        n2 = self.y
        if self.dragon_mode ==0 :
            for i in range(n1,n1+3):
                for j in range(n2 ,n2+3):
                    if matrix[i][j]==Back.YELLOW +Fore.BLACK + '$':
                        self.score += 1
        else :
            for i in range(n1,n1+7):
                for j in range(n2 ,n2+37):
                    if matrix[i][j]==Back.YELLOW +Fore.BLACK + '$':
                        self.score += 1    
        
                
    def remove_batman(self,matrix) :
        n1 = self.x
        n2 = self.y
        if self.dragon_mode == 0:
            for i in range(n1,n1+3):
                for j in range(n2,n2+3):
                    matrix[i][j]=' '
        else :
            for i in range(n1,n1+7):
                for j in range(n2 ,n2+37):
                    matrix[i][j]=' '         

    def move(self,x,columns,column_start):
        if x == chr(100):
            self.y +=1
            if self.y >= columns+column_start -3:
                self.y = columns+column_start -4
        elif x == chr(97):
            self.y -= 1
            if self.y < column_start:
                self.y = column_start
        elif x == chr(119):
            self.x -= 1
        elif x== chr(120):
            self.x+=1
        
       

class BossEnemy(Character) :
    def __init__(self,x,y,life):
        self.life = life
        super().__init__(x,y)

    def boss_enemy_pos(self,matrix):
        Matrix1 = [[0 for x in range(1000)] for y in range(1000)]  # h == no of rows ; w == no of columns
        f = open("batdragon.txt", "r")
        xi = 0
        mx = -1
        for x in f:
            yi = 0
            y2 =0
            for y in x:
                y2 +=1
            for y in x :   
                Matrix1[xi][yi] = y
                yi+=1
                if yi == y2 -1 :
                    break
                if yi > mx:
                    mx = yi
            xi+=1
        i1=0
        j1=0
        for i in range(self.x,self.x+xi) :
            j1= 0
            for j in range(self.y,self.y+mx):
                u = random.randint(0,1)
                if Matrix1[i1][j1] != 0:
                    if u == 1:
                        matrix[i][j]=Fore.RED + Matrix1[i1][j1]
                    else :
                        matrix[i][j]=Fore.YELLOW + Matrix1[i1][j1]
                j1+=1
            i1+=1
    
    def remove_boss_enemy(self,matrix):
        Matrix1 = [[0 for x in range(1000)] for y in range(1000)]  # h == no of rows ; w == no of columns
        f = open("batdragon.txt", "r")
        xi = 0
        mx = -1
        for x in f:
            yi = 0
            y2 =0
            for y in x:
                y2 +=1
            for y in x :   
                Matrix1[xi][yi] = y
                yi+=1
                if yi == y2 -1 :
                    break
                if yi > mx:
                    mx = yi
            xi+=1
        i1=0
        j1=0
        for i in range(self.x,self.x+xi) :
            j1= 0
            for j in range(self.y,self.y+mx):
                matrix[i][j]=' '
                j1+=1
            i1+=1