"""
* CSCI3180 Principles of Programming Languages
*
* --- Declaration ---
* For all submitted files, including the source code files and the written
* report, for this assignment:
*
* I declare that the assignment here submitted is original except for source
* materials explicitly acknowledged. I also acknowledge that I am aware of
* University policy and regulations on honesty in academic work, and of the
* disciplinary guidelines and procedures applicable to breaches of such policy
* and regulations, as contained in the website
* http://www.cuhk.edu.hk/policy/academichonesty/
*
* Name: <FILL YOUR NAME HERE>
* Student ID: <FILL YOUR STUDENT ID HERE>
* Email Address: <FILL YOUR EMAIL ADDRESS HERE>
*
* Source material acknowledgements (if any):
*
* Students whom I have discussed with (if any):
"""

import time
import random

# constants
GAME_MAP_ROWS = 16
GAME_MAP_COLS = 48

ENEMY_LIFE = 5
ENEMY_SHOOT_INTERVAL = 5
ENEMY_SIZE_ROWS = 3
ENEMY_SIZE_COLS = 7
ENEMY_SPEED = 1

PLAYER_LIFE = 2
PLAYER_SHOOT_INTERVAL = 5
PLAYER_SIZE_ROWS = 2
PLAYER_SIZE_COLS = 5
PLAYER_SPEED = 1

# enums
class DirectionType:
    DIR_UP = 0
    DIR_DOWN = 1
    DIR_LEFT = 2
    DIR_RIGHT = 3
    DIR_ERROR = 4

class BulletType:
    BUL_FROM_ENEMY = 0
    BUL_FROM_PLAYER = 1

class GameOverType:
    PLAYER_WIN = 1
    ENEMY_WIN = 2

# global variables
global_directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
global_game_map = [[' ' for _ in range(GAME_MAP_COLS)] for _ in range(GAME_MAP_ROWS)]
global_player = None
global_enemy = None
global_bullets = []

class Plane:
    def __init__(self, init_location, init_symbol, init_size, init_speed, init_direction, init_life):
        self._life = init_life
        self._location = init_location
        self._size = init_size
        self._symbol = init_symbol
        self._speed = init_speed
        self._direction = init_direction

    # TODO: add Property Decorator for attributes self._life, self._symbol, self._direction here, including setter.
    
    
    def draw(self):
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                global_game_map[(self._location[0] + i) % GAME_MAP_ROWS][(self._location[1] + j) % GAME_MAP_COLS] = self._symbol

    def move(self):
        # TODO: Implement the logic of the next position the plane moves to here.
        

    def is_collision(self, bullet_location):
        # TODO: Implement the logic to determine whether the plane has been hit by a bullet here.
        

    def shoot(self, bullet_location, bullet_direction, bullet_type):
        new_bullet = Bullet(bullet_location, self._symbol, bullet_direction, bullet_type)
        global_bullets.append(new_bullet)
    
    def hit(self):
        self.life -= 1
    
class Bullet:
    def __init__(self, init_location, init_symbol, init_direction, init_type):
        assert init_direction == DirectionType.DIR_UP or init_direction == DirectionType.DIR_DOWN
        assert init_type == BulletType.BUL_FROM_ENEMY or init_type == BulletType.BUL_FROM_PLAYER
        self._validity = True
        self._bullet_type = init_type
        self._bullet_on_edge = False
        self._location = init_location
        self._symbol = init_symbol
        self._speed = 1
        self._direction = init_direction

    # TODO: add Property Decorator for attributes self._validity here, including setter.
    
    
    def draw(self):
        if not self._validity:
            return
        global_game_map[self._location[0] % GAME_MAP_ROWS][self._location[1] % GAME_MAP_COLS] = self._symbol

    def move(self):
        if self._bullet_on_edge:
            self.validity = False
            return

        # TODO: Implement the logic of the next position the bullet moves to here.
        
        
        # TODO: Implement the logic to determine whether the bullet hits the plane.
        
        
        self.check_on_edge()
    
    def check_on_edge(self):
        # TODO: Implement the logic to determine whether the bullet reaches the map boundary.
        

class Player(Plane):
    def __init__(self, init_location):
        super().__init__(init_location, '^', (PLAYER_SIZE_ROWS, PLAYER_SIZE_COLS), PLAYER_SPEED, DirectionType.DIR_LEFT, PLAYER_LIFE)
        self._shoot_interval = 0
    
    def move(self):
        super().move()
        # TODO: Implement the logic of the player automatically firing a bullet after PLAYER_SHOOT_INTERVAL frames.
        

    def shoot(self):
        bullet_location = (self._location[0], self._location[1] + (self._size[1] // 2))
        super().shoot(bullet_location, DirectionType.DIR_UP, BulletType.BUL_FROM_PLAYER)
    
    def speak(self):
        dialogues = ["I'm ready for action!", "No one can defeat me!", "I'll save the world!"]
        print("Player:\t", random.choice(dialogues))
        
    def display_info(self):
        print("Congratulations! You have defeated them.")


class Enemy(Plane):
    def __init__(self, init_location):
        super().__init__(init_location, '$', (ENEMY_SIZE_ROWS, ENEMY_SIZE_COLS), ENEMY_SPEED, DirectionType.DIR_LEFT, ENEMY_LIFE)
        self._shoot_interval = 0

    def move(self):
        super().move()
        # TODO: Implement the logic that enemy has a 10% chance of changing direction in each frame.
        
        
        # TODO: Implement the logic of the player automatically firing a bullet after ENEMY_SHOOT_INTERVAL frames.
        

    def shoot(self):
        bullet_location = (self._location[0] + self._size[0] - 1, self._location[1] + (self._size[1] // 2))        
        super().shoot(bullet_location, DirectionType.DIR_DOWN, BulletType.BUL_FROM_ENEMY)
    
    def speak(self):
        dialogues = ["You won't escape!", "Prepare to be destroyed!", "I will crush you!"]
        print("Enemy:\t", random.choice(dialogues))
        
    def display_info(self):
        print("Sad! You made sacrifices in this fierce battle.")
    
class Environment:
    def __init__(self):
        self._winner = None
        self._speaker = None
        
        global global_enemy, global_player
        global_enemy = Enemy((0, (GAME_MAP_COLS - ENEMY_SIZE_COLS) // 2))
        global_player = Player((GAME_MAP_ROWS - PLAYER_SIZE_ROWS, (GAME_MAP_COLS - PLAYER_SIZE_COLS) // 2))
        
        # counting down
        print("\n\n\t\tThe game is about to begin!")
        for i in range(3, 0, -1):
            start = time.time()
            while time.time() - start <= 1:
                pass  # 1 s

            if i > 0:
                print("\n\n\t\tCountdown:", i)

    def move_all(self):
        global_player.move()
        global_enemy.move()
        for bullet in global_bullets:
            bullet.move()

    def draw_all(self):
        global global_game_map
        global_game_map = [[0] * GAME_MAP_COLS for _ in range(GAME_MAP_ROWS)]
        global_player.draw()
        global_enemy.draw()
        for obj_ptr in global_bullets:
            obj_ptr.draw()

    def check_state(self):
        to_be_delete = []
        for i in range(len(global_bullets)):
            if not global_bullets[i].validity:
                to_be_delete.append(i)
        for idx in reversed(to_be_delete):
            global_bullets.pop(idx)
        
        # TODO: Implement the logic to determine whether the game should end.
        if global_enemy.life <= 0:
            self._winner = 
        if global_player.life <= 0:
            self._winner = 

    def display_all(self):
        print()
        for _ in range(GAME_MAP_COLS + 2):
            print('-', end='')
        print()
        for i in range(GAME_MAP_ROWS):
            print('|', end='')
            for j in range(GAME_MAP_COLS):
                if global_game_map[i][j] != 0:
                    print(global_game_map[i][j], end='')
                else:
                    print(" ", end='')
            print('|')
        for _ in range(GAME_MAP_COLS + 2):
            print('-', end='')
        print()
        
        # TODO: Implement speaking logic here.
        if random.randint(0, 1) == 0:
            self._speaker = 
        else:
            self._speaker = 
        self._speaker.speak() 
        
        for _ in range(GAME_MAP_COLS + 2):
            print('-', end='')
        print()
        print("ENEMY\tHP: ", global_enemy.life)
        print("PLAYER\tHP: ", global_player.life)

    def display_result(self):
        self._winner.display_info()
    
    def get_input(self):
        print("Please select the moving direction! (w : up, s : down, a: left, d: right)")
        player_input = input()  # get input from player
        if player_input == 'w':
            global_player.direction = DirectionType.DIR_UP
        elif player_input == 's':
            global_player.direction = DirectionType.DIR_DOWN
        elif player_input == 'a':
            global_player.direction = DirectionType.DIR_LEFT
        elif player_input == 'd':
            global_player.direction = DirectionType.DIR_RIGHT

    def run(self):
        self.check_state()
        self.draw_all()
        self.display_all()
        while not self._winner:
            self.get_input()
            self.move_all()
            self.draw_all()
            self.display_all()
            self.check_state()
        self.display_result()
    

if __name__ == "__main__":
    random.seed(555)
    env = Environment()
    env.run()
    





