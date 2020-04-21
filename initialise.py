import random
import os
import tty
import sys
import termios
import colorama
from select import select
from characters import *
from objects import *
import time
from moving import *
from check import *
from colorama import Fore, Back, Style

def kb_hit():
    dr, dw, de = select([sys.stdin], [], [], 0)
    return dr != []

def getch():
    return sys.stdin.read(1)[0]

def matrix_init (matrix,coin_list,flames_list,w,h,rows,column_start,powerup_list,boss_enemy,magnet_list,dragon_icon_list):
    for i in  range(0,h):
        for j in range(0,w):
            matrix[i][j]=' '
    
    boss_enemy.boss_enemy_pos(matrix)
    # boundary
    for i in range(0,w):
        matrix[0][i]= Back.BLUE + Fore.MAGENTA + 'T'
        matrix[1][i]=Back.BLUE + Fore.MAGENTA +'T'
        matrix[rows-1][i]=Back.GREEN + Fore.MAGENTA +'T'
        matrix[rows-2][i]=Back.GREEN+ Fore.MAGENTA+'T'

    # coins 
    p  = random.randint(150,250)
   
    for i in range(0,p):
        y1 = random.randint(5,w-3)
        x1 = random.randint(5,rows-4)
        if boss_enemy.y -1 <= y1 and boss_enemy.y + 51 >=y1:
            i-=1
        else:
            coins = Coins(x1,y1)
            coins.coins_pos(matrix)
            coin_list.append(coins)
    
    # flames 
    q = random.randint(150,250)
    for i in range(0,q):
        y1 = random.randint(7,w-7)
        x1 = random.randint(2,rows-7)
        orientation = random.randint(1,3)
        f=0
        if boss_enemy.y -1 <= y1 and boss_enemy.y + 51 >=y1:
            f=1
        if orientation == 1 :
            for i in range(y1,y1+5):
                if matrix[x1][i] != ' ':
                    f=1
        elif orientation == 2 :
            for i in range(x1,x1+5):
                if matrix[i][y1] != ' ':
                    f=1
        else:
            for i in range(0,5):
                if matrix[x1+i][y1+i] != ' ':
                    f=1
        if f == 0 :
            flames = Flames(x1,y1,orientation)
            flames.flames_pos(matrix)
            flames_list.append(flames)
        else : 
            i-=1
   
    # powerup 
    t = random.randint(5,10)
    for i in range(0,t):
        y1 = random.randint(7,w-7)
        x1 = random.randint(5,rows-4)
        f=0
        if boss_enemy.y -1 <= y1 and boss_enemy.y + 51 >=y1:
            f=1
        for j in range(x1,x1+3):
            for k in range(y1,y1+3):
                if matrix[j][k]!=' ':
                    f=1
        if f == 0:
            powerup = Powerup(x1,y1)
            powerup.powerup_pos(matrix)
            powerup_list.append(powerup)
        else :
            i-=1
    
    # magnet 
    z = random.randint(5,8)
    for i in range(0,z):
        
        y1 = random.randint(7,w-7)
        x1 = random.randint(5,rows-10)
        f=0
        for j in range(x1,x1+3):
            for k in range(y1,y1+3):
                if matrix[j][k]!=' ':
                    f=1
        if boss_enemy.y -1 <= y1 and boss_enemy.y + 51 >=y1:
            f = 1
        if f == 0:
            magnet = Magnet(x1,y1,0)
            magnet.magnet_pos(matrix)
            magnet_list.append(magnet)
        else :
            i-=1
    #dragon_icon 
    y1 = 200
    x1 = 12
    dragon_icon = Dragon_icon(x1,y1)
    dragon_icon_list.append(dragon_icon)
    dragon_icon.dragon_icon_pos(matrix) 

def lose_matrix(Matrix,rows,columns,w,h):
    for i in range(0,h):
        for j in range(0,w):
            Matrix[i][j]= Back.BLACK + Fore.BLACK+ ' '
    Matrix1 = [[0 for x in range(1000)] for y in range(1000)]  # h == no of rows ; w == no of columns
    f = open("lose.txt", "r")
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
   
    for i in range(8,8+xi) :
        j1= 0
        for j in range(24,25+mx):
            if Matrix1[i1][j1] != 0:
                Matrix[i][j]= Fore.RED+ Matrix1[i1][j1]
            j1+=1
        i1+=1

def win_matrix(Matrix,rows,columns,w,h):
    for i in range(0,h):
        for j in range(0,w):
            Matrix[i][j]= Back.BLACK + Fore.BLACK+ ' '
    Matrix1 = [[0 for x in range(1000)] for y in range(1000)]  # h == no of rows ; w == no of columns
    f = open("win.txt", "r")
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
   
    for i in range(9,9+xi) :
        j1= 0
        for j in range(15,15+mx):
            if Matrix1[i1][j1] != 0:
                Matrix[i][j]= Fore.RED+ Matrix1[i1][j1]
            j1+=1
        i1+=1

def start_game(Matrix,batman,w,h,coin_list,flames_list,shield,rows,columns,column_start,powerup_list,boss_enemy,magnet_list,dragon_icon_list):
    matrix_init(Matrix,coin_list,flames_list,w,h,rows,column_start,powerup_list,boss_enemy,magnet_list,dragon_icon_list)
    batman.batman_pos(Matrix,shield)
    print_matrix(rows,columns,Matrix,shield,batman,column_start,boss_enemy)        
