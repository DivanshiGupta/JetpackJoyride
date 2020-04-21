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
from check import *
from colorama import Fore,Back,Style

def implement_gravity(batman,rows,Matrix,shield,last_time) :
    if batman.dragon_mode == 0:
        if batman.x < rows -5 :
            # print(time.time() - last_time)
            if time.time() - last_time > 0.001:
                # print(1)
                last_time = time.time()
                gravity_constant = 0.01
                change_pos = round(gravity_constant*batman.time_of_flight)
                batman.remove_batman(Matrix)
                batman.x += change_pos
                if batman.x > rows - 5:
                    batman.x = rows-5
                batman.batman_pos(Matrix,shield)
                # print (change_pos)
                batman.time_of_flight+=1
            
        else :
            batman.time_of_flight =0
            last_time = time.time()
    else :
        if batman.x < rows -9 :
            # print(time.time() - last_time)
            if time.time() - last_time > 0.001:
                # print(1)
                last_time = time.time()
                gravity_constant = 0.01
                change_pos = round(gravity_constant*batman.time_of_flight)
                batman.remove_batman(Matrix)
                batman.x += change_pos
                if batman.x > rows - 5:
                    batman.x = rows-5
                batman.batman_pos(Matrix,shield)
                # print (change_pos)
                batman.time_of_flight+=1
            
        else :
            batman.time_of_flight =0
            last_time = time.time()

def fire_bullet(batman,Matrix,bullet_list):
    stime = time.time()
    if batman.dragon_mode == 0:
        bullet = Bullet(batman.x,batman.y+3,stime,0)
        bullet_list.append(bullet)

    else:
        bullet = Bullet(batman.x,batman.y+45,stime,0)
        bullet_list.append(bullet)

def fire_boss_bullet(batman,Matrix,boss_enemy_bullets,boss_enemy):
    stime = time.time()
    boss_enemy_bullet = bossenemyBullet(0,boss_enemy,batman.x,batman.y)
    boss_enemy_bullet.bullet_pos(Matrix)
    boss_enemy_bullets.append(boss_enemy_bullet)


def move_bullet(Matrix,column_start,columns,bullet_list,move_fast,batman):
    index =0 
    # print(move_fast)
    for i in bullet_list :
        # print(move_fast)

        if i.count > 150 or i.y >= column_start + columns:
            i.remove_bullet(Matrix)
            bullet_list.pop(index)
            index-=1
        
        if time.time() - i.stime > 0.02 :
            i.stime = time.time()
            i.remove_bullet(Matrix)
            i.y += 1
            if move_fast != 0 :
                i.y+=move_fast
            i.count += 1
            if move_fast : 
                i.count+=move_fast
            i.bullet_pos(Matrix)
    index +=1
       

def move_boss_enemy_bullet(Matrix,boss_enemy_bullets,boss_enemy,batman,column_start) :
    index =0 
    for i in boss_enemy_bullets:
        if i.x == i.aim_x and i.y == i.aim_y :
            i.remove_bullet(Matrix)
            boss_enemy_bullets.pop(index)
            index-=1
        else: 
            if time.time() - i.stime > 0.1 :
                i.stime = time.time()
                i.remove_bullet(Matrix)
                if i.y > i.aim_y :
                    i.y -=5
                if i.y < i.aim_y:
                    i.y = i.aim_y
                if i.x < i.aim_x :
                    i.x +=1
                if i.x > i.aim_x :
                    i.x-=1
                i.bullet_pos(Matrix)
        index +=1
    # print(index)



# def move_batman(time_start,time_to_move_screen,Matrix,batman,column_start,rows,columns,shield,dragon_mode):
    
#     elapsed_time = time.time() - time_start
#     t1 = time_to_move_screen
#     if elapsed_time > time_to_move_screen :
#         t1 += 0.05
#         column_start+=1
#         batman.remove_batman(Matrix)
#         batman.y+=1
#         batman.batman_collision(Matrix)
#         batman.batman_pos(Matrix,shield,dragon_mode)
#         print_matrix(rows,columns,Matrix,shield,batman,column_start)   
#     # return time_to_move_screen

#     if batman.x < rows -5 :
#         if batman.start_time_of_flight == 0:
#             batman.start_time_of_flight = time.time()
#         if  time.time() - batman.start_time_of_flight > 0.3 :
#             batman.remove_batman(Matrix)
            
#             batman.x +=1;
#             batman.start_time_of_flight = time.time()
#             # batman.remove_batman(Matrix)
#             batman.batman_collision(Matrix)
#             batman.batman_pos(Matrix,shield,dragon_mode)
#     else :
#         batman.start_time_of_flight =0     

#     return t1

# def  move_powerup(Matrix,powerup_list,batman)

def pull_magnet(matrix,batman,magnet_list,column_start,columns,shield) :
    index =0 
    for i in magnet_list :
        if i.y > column_start and i.y < column_start + columns :
             if time.time() - i.last_time > 0.05 :
                i.magnet_attract(batman,matrix,shield)
    index+=1

def move_boss_enemy(matrix,batman,boss_enemy,column_start,columns,boss_enemy_bullets):
    if boss_enemy.y >= column_start and boss_enemy.y < column_start + columns :
        boss_enemy.remove_boss_enemy(matrix)        
        boss_enemy.x = batman.x - 13
        if boss_enemy.x < 2:
            boss_enemy.x =2
        boss_enemy.boss_enemy_pos(matrix)

def print_matrix(n1,n2,matrix,shield,batman,column_start,boss_enemy):
    print('\033[H')
    print('SCORE:',end=' ')
    print(batman.score,end=' ')
    print('LIVES:',end = ' ')
    print(batman.lives,end=' ')
    print('BOSS-ENEMY LIFE:',end=' ')
    print(boss_enemy.life,end=' ')
    # print('SHIELD STATUS :',end=' ')
    if shield.status == 1 :
        print('SHIELD IN USE                                                ')
    else:
        if time.time()- shield.etime >10 :
            print('SHIELD IS AVAILABLE                                          ') 
        else :
            print('SHIELD NOT AVAILABLE                                ')
    # print(batman.lives)
    for i in range(0,n1):
            for j in range(column_start,n2+column_start-1):
                print(Back.BLACK+  matrix[i][j], end='')
            print('');