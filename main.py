import os
import tty
import sys
import termios
import colorama
from select import select
from characters import *
from objects import *
import random
import time
from initialise import *
from moving import *
from check import *
from colorama import Fore, Back, Style

game_over = False
w,h=10001,101; #width and height of matrix
rows,columns,column_start=30,100,0; # rows,columns = no of rows and columns in one frame
Matrix = [[0 for x in range(w)] for y in range(h)]  # h == no of rows ; w == no of columns
batman = Batman(rows-5,column_start,0,5,0,0,0);
frames=12
coin_list=[]
flames_list=[]
bullet_list=[]
powerup_list=[]
magnet_list =[]
boss_enemy_bullets=[]
dragon_icon_list=[]
shield = Shield(0,0,0)
boss_enemy = BossEnemy(11,1200,20)
dragon_mode =0 
os.system('cls' if os.name == 'nt' else 'clear')
start_game(Matrix,batman,w,h,coin_list,flames_list,shield,rows,columns,column_start,powerup_list,boss_enemy,magnet_list,dragon_icon_list)
orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)     

time_start = time.time()
time_to_move_screen= 0.05
last_time = 0
move_fast = 0 
move_fast1 =0
powerup_time = 0 
fight_time =0 
time_to_fire = time_start
time_to_move =0 
sys.stdout.write("\033[?25l")
sys.stdout.flush()
while not game_over:
    if batman.dragon_mode == 0:
        move_fast1 = 0
    if boss_enemy.life < 1:
        win_matrix(Matrix,rows,columns,w,h)
        print_matrix(rows,columns,Matrix,shield,batman,0,boss_enemy)  
        time.sleep(4)
        
        game_over = True
        break
    if batman.lives < 1:
        # time.sleep(5)
        lose_matrix(Matrix,rows,columns,w,h)
        print_matrix(rows,columns,Matrix,shield,batman,0,boss_enemy)  
        time.sleep(4)
        
        game_over = True
        break
    if check_powerup_collision(powerup_list,batman,Matrix,bullet_list,shield):
        move_fast=1
        powerup_time = time.time()

    if move_fast and time.time() - powerup_time >10 :
        move_fast =0 

    if boss_enemy.y >= column_start and boss_enemy.y +51 < column_start + columns :
        fight_time = 1
    
    if fight_time == 0 :    
        elapsed_time = time.time() - time_start
        if elapsed_time > time_to_move_screen :
            time_to_move_screen += 0.05
            column_start+=1
            if move_fast :
                column_start+=1
            batman.remove_batman(Matrix)
            batman.y+=1
            if move_fast :
                batman.y+=1
            batman.batman_collision(Matrix)
            batman.batman_pos(Matrix,shield)
            print_matrix(rows,columns,Matrix,shield,batman,column_start,boss_enemy)  
    else:
        elapsed_time = time.time() 
        if elapsed_time > time_to_move :
            time_to_move = elapsed_time +  0.02 
            print_matrix(rows,columns,Matrix,shield,batman,column_start,boss_enemy)      
        
        elapsed_time = time.time() 
        if elapsed_time > time_to_fire :
            time_to_fire = elapsed_time+ 1
            fire_boss_bullet(batman,Matrix,boss_enemy_bullets,boss_enemy)
            batman.batman_pos(Matrix,shield)
            print_matrix(rows,columns,Matrix,shield,batman,column_start,boss_enemy)          

    if shield.status == 1:
        if time.time() - shield.stime > 10 :
            shield.status = 0
            shield.etime = time.time()

    implement_gravity(batman,rows,Matrix,shield,last_time)
    last_time = time.time()
    if fight_time == 1 :
        move_fast1 =4
        check_batman_boss_enemy_bullet_collision(Matrix,boss_enemy_bullets,batman,shield)
        check_boss_enemy_collision(batman,Matrix,bullet_list,boss_enemy)
        check_coin_collision(coin_list,bullet_list,Matrix)
        move_boss_enemy(Matrix,batman,boss_enemy,column_start,columns,boss_enemy_bullets)
        # move_bullet(Matrix,column_start,columns,bullet_list,move_fast,batman)
        if move_fast1 >0:
            temp = move_fast

            move_fast = move_fast1
            # temp = move_fast
        move_bullet(Matrix,column_start,columns,bullet_list,move_fast,batman)
        if move_fast1 > 0:
            move_fast  = temp
        move_boss_enemy_bullet(Matrix,boss_enemy_bullets,boss_enemy,batman,column_start)
        print_matrix(rows,columns,Matrix,shield,batman,column_start,boss_enemy)
        check_flame_collision(flames_list,batman,Matrix,bullet_list,shield)
        check_bullet_collision(powerup_list,Matrix,bullet_list,shield,magnet_list,dragon_icon_list)
        # move_bullet(Matrix,column_start,columns,bullet_list,move_fast,batman)
        pull_magnet(Matrix,batman,magnet_list,column_start,columns,shield)
        check_magnet_collision(magnet_list,batman,Matrix,shield)

    else :
        if check_dragonicon_collision(Matrix,batman,dragon_icon_list):
            batman.dragon_mode =1 
            batman.x -= 5
            move_fast1 = 4
        check_coin_collision(coin_list,bullet_list,Matrix)
        check_flame_collision(flames_list,batman,Matrix,bullet_list,shield)
        check_bullet_collision(powerup_list,Matrix,bullet_list,shield,magnet_list,dragon_icon_list)
        if move_fast1 >0:
            temp = move_fast

            move_fast = move_fast1
            # temp = move_fast
        move_bullet(Matrix,column_start,columns,bullet_list,move_fast,batman)
        if move_fast1 > 0:
            move_fast  = temp
        pull_magnet(Matrix,batman,magnet_list,column_start,columns,shield)
        check_magnet_collision(magnet_list,batman,Matrix,shield)
      
    if kb_hit():
        x = getch()
        if x == chr(27):
            game_over=True
        if x == chr(115) :
            if time.time() - shield.etime > 10:
                shield.status =1 
                shield.stime = time.time()
        elif x == chr(102) :
            fire_bullet(batman,Matrix,bullet_list)
            print_matrix(rows,columns,Matrix,shield,batman,column_start,boss_enemy)

        else :
            batman.remove_batman(Matrix)
            batman.move(x,columns,column_start)
            if batman.x <= 1 :
                batman.x = 2 
            if batman.x >= rows -4 :
                batman.x = rows-5
            batman.batman_collision(Matrix)
            batman.batman_pos(Matrix,shield)
            print_matrix(rows,columns,Matrix,shield,batman,column_start,boss_enemy)
    else:
        pass
    # time.sleep(0.02)