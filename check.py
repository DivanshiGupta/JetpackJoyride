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
from moving import *
from initialise import *

def check_flame_collision(flames_list,batman,Matrix,bullet_list,shield):
    index =0 
    for i in flames_list:
        checker = i.flames_collision_batman(batman,Matrix)
        if checker == 1 :
            if shield.status == 0:
                batman.lives-=1
            i.flames_remove(Matrix)
            flames_list.pop(index)
            index-=1
            if batman.dragon_mode == 1 and shield.status == 0:
                batman.remove_batman(Matrix)
                batman.dragon_mode = 0
                batman.batman_pos(Matrix,shield)
        else :
            in1 =0
            for j in bullet_list :
                checker = i.flames_collision_bullet(j,Matrix)
                if checker == 1:
                    i.flames_remove(Matrix)
                    flames_list.pop(index)
                    j.remove_bullet(Matrix)
                    bullet_list.pop(in1)
                    in1-=1
                    index-=1
                    break
                in1+=1
        index+=1

def check_coin_collision(coin_list,bullet_list,Matrix):
    index =0
    for i in coin_list :
        index =0
        for j in bullet_list :            
            if j.x >= i.x -1 and j.x <=i.x+1 :
                if j.y >= i.y - 2 and j.y <=i.y+1 :
                    j.remove_bullet(Matrix)
                    bullet_list.pop(index)
                    index -=1
                    i.coins_pos(Matrix)
                    break
            index+=1
       
def check_powerup_collision(powerup_list,batman,Matrix,bullet_list,shield):
    index =0 
    f=0
    for i in powerup_list :
        checker = i.powerup_collision_batman(batman,Matrix)
        if checker == 1:
            i.remove_powerup(Matrix)
            powerup_list.pop(index)
            f=1
            index-=1
            break
        index+=1
    return f

def check_bullet_collision(powerup_list,Matrix,bullet_list,shield,magnet_list,dragon_icon_list):
    index =0
    for j in bullet_list :
        for i in powerup_list :
             if j.x >= i.x - 1 and j.x <= i.x +2 :
                if j.y >= i.y -2 and j.y <= i.y +2 :
                    j.remove_bullet(Matrix)
                    bullet_list.pop(index)
                    i.powerup_pos(Matrix)
                    index-=1
                    break

        index +=1
    index =0 
    for j in bullet_list :
        for i in magnet_list :
             if j.x >= i.x - 1 and j.x <= i.x +2 :
                if j.y >= i.y -2 and j.y <= i.y +2 :
                    j.remove_bullet(Matrix)
                    bullet_list.pop(index)
                    i.magnet_pos(Matrix)
                    index-=1
                    break

        index +=1
    index =0 
    for j in bullet_list :
        for i in dragon_icon_list :
             if j.x >= i.x - 1 and j.x <= i.x +2 :
                if j.y >= i.y -2 and j.y <= i.y +2 :
                    j.remove_bullet(Matrix)
                    bullet_list.pop(index)
                    i.dragon_icon_pos(Matrix)
                    index-=1
                    break

        index +=1

def check_magnet_collision(magnet_list,batman,matrix,shield):
    for i in magnet_list :
        if batman.x >= i.x - 2 and batman.x <= i.x+2:
            if batman.y >= i.y -2 and batman.y <= i.y +2 :
                batman.remove_batman(matrix)
                batman.x = i.x+3
                batman.y = i.y + 3
                batman.batman_pos(matrix,shield)
                i.magnet_pos(matrix)
                 
def check_boss_enemy_collision(batman,matrix,bullet_list,boss_enemy):
    index =0
    for i in bullet_list:
        f=0
        if i.x >= boss_enemy.x -1 and i.x <= boss_enemy.x + 16 :
            if i.y >= boss_enemy.y -1 and i.y <= boss_enemy.y + 51 :
                f=1
                boss_enemy.life -=1
                i.remove_bullet(matrix)
                bullet_list.pop(index)
                index-=1
                boss_enemy.boss_enemy_pos(matrix)

        if f==0 : 
            if i.y > boss_enemy.y + 51  :
                i.remove_bullet(matrix)
                bullet_list.pop(index)
                index-=1
    index+=1

def check_batman_boss_enemy_bullet_collision(matrix,boss_enemy_bullets,batman,shield):
    index =0
    for i in boss_enemy_bullets :
        if i.x >= batman.x -1 and i.x <= batman.x +2 :
            if i.y >= batman.y -2 and i.y <= batman.y +2 :
                batman.lives-=1
                i.remove_bullet(matrix)
                boss_enemy_bullets.pop(index)
                index-=1
                batman.batman_pos(matrix,shield)
        index += 1            

def check_dragonicon_collision(matrix,batman,dragon_icon_list):
    index = 0
    f = 0 
    for i in dragon_icon_list :
        if i.dragonicon_collision_batman(batman,matrix):
            dragon_icon_list.pop(index)
            index-=1
            f = 1
            i.remove_dragonicon(matrix)
            break
        index +=1 
    return f