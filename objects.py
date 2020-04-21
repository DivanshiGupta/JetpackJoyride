from colorama import Fore, Back, Style
import time
class BULLETS :
    def __init__(self,x,y):
        self.x=x
        self.y =y
    
class Coins:
    def __init__(self,x,y):
        self.x=x
        self.y =y
    
    def coins_pos(self,matrix):
        n1 = self.x
        n2 = self.y
        for i in range(n1,n1+2):
            for j in range(n2,n2+2):
                matrix[i][j]=Back.YELLOW + Fore.BLACK + '$'
    
    def remove_coins(self,matrix) :
        n1 = self.x
        n2 = self.y
        for i in range(n1,n1+2):
            for j in range(n2,n2+2):
                matrix[i][j]=' '

class Flames:
    def __init__(self,x,y,orientation):
        self.x = x
        self.y = y
        self.orientation = orientation
    
    def flames_pos(self,matrix):
        n1 = self.x
        n2 = self.y
        if self.orientation == 1 :
            for i in range(n2,n2+5):
                matrix[n1][i] = Back.RED + Fore.YELLOW + '*'
        
        elif self.orientation == 2 :
            for i in range(n1,n1+5):
                matrix[i][n2] = Back.RED +Fore.YELLOW + '*'

        else:
            for i in range(0,5):
                matrix[n1+i][n2+i] = Back.RED + Fore.YELLOW + '*'

    def flames_remove(self,matrix):
        n1 = self.x
        n2 = self.y
        if self.orientation == 1 :
            for i in range(n2,n2+5):
                matrix[n1][i] = Back.BLACK +' '
        
        elif self.orientation == 2 :
            for i in range(n1,n1+5):
                matrix[i][n2] = Back.BLACK+ ' '

        else:
            for i in range(0,5):
                matrix[n1+i][n2+i] = Back.BLACK+' '

    def flames_collision_batman(self,batman,matrix):
        n1 = self.x
        n2 = self.y
        if batman.dragon_mode == 1:
            orientation = self.orientation
            if orientation == 1 :
                if batman.x >= self.x- 6 and batman.x <= self.x+2 :
                    if batman.y >= self.y -35 and batman.y <=  self.y +4 :
                        return 1
            elif orientation == 2 :
                if batman.x >= self.x -6 and batman.x <= self.x+4:
                    if batman.y>= self.y-35 and batman.y <= self.y +2:
                        return 1
            elif orientation == 3 :
                if batman.x >= self.x-6 and batman.y >= self.y -35 :
                    if batman.x  <= self.x +4 and batman.y <= self.y + 4 :
                        return 1
        else :
            orientation = self.orientation
            if orientation == 1 :
                if batman.x >= self.x- 2 and batman.x <= self.x+2 :
                    if batman.y >= self.y -2 and batman.y <=  self.y +4 :
                        return 1
            elif orientation == 2 :
                if batman.x >= self.x -2 and batman.x <= self.x+4:
                    if batman.y>= self.y-2 and batman.y <= self.y +2:
                        return 1
            elif orientation == 3 :
                if batman.x >= self.x-2 and batman.y >= self.y -2 :
                    if batman.x  <= self.x +4 and batman.y <= self.y + 4 :        
                        return 1  
        return 0             

    def flames_collision_bullet(self,bullet,matrix):
        n1 = self.x
        n2 = self.y
        if self.orientation == 1 :
            for i in range(n2,n2+5):
                if matrix[n1][i] == Fore.BLUE + '~':
                    return 1
        
        elif self.orientation == 2 :
            for i in range(n1,n1+5):
                if matrix[i][n2] ==  Fore.BLUE + '~':
                    return 1
        else:
            for i in range(0,5):
                if matrix[n1+i][n2+i] == Fore.BLUE +  '~':
                    return 1

class Bullet(BULLETS):
    def __init__(self,x,y,stime,count):
        self.stime=stime
        self.count = count
        super().__init__(x,y)

        
    def bullet_pos(self,matrix):
        n1 = self.x
        n2 = self.y
        for i in range(n1,n1+2):
            for j in range(n2,n2+3):
                matrix[i][j]=  Fore.BLUE + '~'
    
    def remove_bullet(self,matrix) :
        
        n1 = self.x
        n2 = self.y
        for i in range(n1,n1+2):
            for j in range(n2,n2+3):
                matrix[i][j]=' '

class bossenemyBullet(BULLETS):
    def __init__(self,stime,boss_enemy,aim_x,aim_y):
        self.aim_x = aim_x
        self.aim_y = aim_y
        self.stime=stime
        super().__init__(boss_enemy.x + 8,boss_enemy.y + 5)

    def bullet_pos(self,matrix):
        n1 = self.x
        n2 = self.y
        for i in range(n1,n1+2):
            for j in range(n2,n2+3):
                matrix[i][j]=  Fore.BLUE + '#'
    
    def remove_bullet(self,matrix) :
        n1 = self.x
        n2 = self.y
        for i in range(n1,n1+2):
            for j in range(n2,n2+3):
                matrix[i][j]=' '

class Shield:
    def __init__(self,status,stime,etime):
        self.status = status 
        self.stime = stime
        self.etime = etime

class Powerup:
    def __init__(self,x,y):
        self.x =x
        self.y =y 
    def powerup_pos(self,matrix):
        n1 = self.x
        n2 = self.y
        matrix[n1][n2] = Back.BLUE+' '
        matrix[n1][n2+1]=Back.RED+' '
        matrix[n1][n2+2]=Back.CYAN+' '
        matrix[n1+1][n2]=Back.GREEN +' '
        matrix[n1+1][n2+2]=Back.BLUE+ ' '
        matrix[n1+2][n2]= Back.RED+ ' '
        matrix[n1+2][n2+1]=Back.BLUE +' '
        matrix[n1+2][n2+2] = Back.YELLOW+' '
        matrix[n1+1][n2+1] = Back.MAGENTA + Fore.YELLOW+ 'P'
    def remove_powerup(self,matrix) :
        n1 = self.x
        n2 = self.y
        for i in range(n1,n1+3):
            for j in range(n2,n2+3):
                matrix[i][j]=' '
    def powerup_collision_batman(self,batman,matrix):
        n1 = self.x
        n2 = self.y
        if batman.x >= self.x - 2 and batman.x <= self.x +2:
            if batman.y >= self.y - 2 and batman.y <= self.y+2 :
                return 1
        return 0

class Dragon_icon:
    def __init__(self,x,y):
        self.x =x
        self.y =y 
    def dragon_icon_pos(self,matrix):
        n1 = self.x
        n2 = self.y
        matrix[n1][n2] = Back.BLUE+' '
        matrix[n1][n2+1]=Back.MAGENTA+' '
        matrix[n1][n2+2]=Back.BLUE+' '
        matrix[n1+1][n2]=Back.MAGENTA +' '
        matrix[n1+1][n2+2]=Back.MAGENTA+ ' '
        matrix[n1+2][n2]= Back.BLUE+ ' '
        matrix[n1+2][n2+1]=Back.MAGENTA +' '
        matrix[n1+2][n2+2] = Back.BLUE+' '
        matrix[n1+1][n2+1] = Back.BLUE + ' '
    def remove_dragonicon(self,matrix) :
        n1 = self.x
        n2 = self.y
        for i in range(n1,n1+3):
            for j in range(n2,n2+3):
                matrix[i][j]=' '
    def dragonicon_collision_batman(self,batman,matrix):
        n1 = self.x
        n2 = self.y
        if batman.x >= self.x - 2 and batman.x <= self.x +2:
            if batman.y >= self.y - 2 and batman.y <= self.y+2 :
                return 1
        return 0

class Magnet:
    def __init__(self,x,y,last_time):
        self.x = x
        self.y = y 
        self.last_time = last_time
    def magnet_pos(self,matrix):
        n1 = self.x
        n2 = self.y
        matrix[n1][n2]=Back.RED +' '
        matrix[n1][n2+1]=Back.RED +' '
        matrix[n1][n2+2]=Back.RED +' '
        matrix[n1+1][n2]=Back.RED +' '
        matrix[n1+1][n2+2]=Back.RED +' '
        matrix[n1+2][n2] = Back.BLUE + ' '
        matrix[n1+2][n2+2] = Back.BLUE+' '
    def remove_magnet(self,matrix) :
        n1 = self.x
        n2 = self.y
        for i in range(n1,n1+3):
            for j in range(n2,n2+3):
                matrix[i][j]=' '

    def magnet_attract(self,batman,matrix,shield):
        if batman.x <= self.x+30 and batman.x >= self.x -30: 
            if  batman.y <= self.y+40 and batman.y >= self.y -40:
                # print('ues')
                batman.remove_batman(matrix)
                if batman.x < self.x -1 :
                    batman.x +=1
                if batman.x > self.x +2:
                    batman.x-=1
                if batman.y > self.y +2:
                    batman.y -=1
                if batman.y < self.y -1:
                    batman.y +=1   

                self.last_time = time.time()
                batman.batman_pos(matrix,shield)