#BrickGame

#Ball is moving at a constant speed and bounce off the walls
#Ball Reflects when it hits walls and ceiling
#bonus Features, could include making the rows of bricks a different colour
#Hit detection - 
import random
key_mode = 0
padpos= -10 
padpos1 = 0

def paddle():
    fill(255)
    circle(padpos , 460 , 20)
    circle(padpos + 20 , 460, 20)
    rect(padpos, 450 , 20 , 20)
import random
    
BrickColour = 255

def setup():
    size(500, 500)
    background(0)
    global ball
    global Bricks
    Bricks = []
    for i in range(10):
        for j in range(8):
            brick1 = Brick(10 + i*48, 30+j*20, 48, 20)
            Bricks.append(brick1)
    ball = Ball(300, 445)
    #Bricks[10].erase()
    
def draw():
    global ball
    global Bricks
    background(0, 0, 0)
    fill(100)
    rect(-1,0, width+1, 30)    
    ball.draw()
    #Bricks[random.randint(0, 79)].erase()
    for i in range(len(Bricks)):
        if Bricks[i].hit_test(ball.pos_x, ball.pos_y):
            Bricks[i].erase()    
        Bricks[i].draw()
        
    global padpos1
    global key_mode
    if keyPressed:
        key_mode = 1
        if ball.dx == 0 and key == " ":
            ball.dx = 4
            ball.dy = -6 
        
    if mousePressed:
        key_mode = 0
        if ball.dx ==0:
            ball.dx = 2
            ball.dy = -3
    if key_mode == 0:
        padpos1 = mouseX        

    #ball.pos_x = mouseX
    #ball.pos_y = mouseY
   
       
    if key_mode == 1:     
        if keyPressed:
            if keyCode == LEFT:
                padpos1 = padpos1 - 10
                
            if keyCode == RIGHT:
                padpos1 = padpos1 + 10
                
    if padpos1 >= 470: 
        padpos1 = 470                
    if padpos1 <= 30: 
        padpos1 = 30
    if ball.dx ==0:
        ball.pos_x = padpos1
    pushMatrix()
    #padpos1 = 100
    translate(padpos1,0)       
    paddle()
    popMatrix()    
    #print(padpos1)
    #print(ball.pos_x)
    #print(ball.pos_y)
    ball.padpos = padpos1
"""
    print(mouseX, mouseY)
    if ball.pos_y >= 435 and ball.pos_y <= 462:
        background(200)
        rect(padpos1-80, 435, 100, 20)
        if ball.pos_x >= padpos1-80 and ball.pos_x <= padpos + 80:
            
            print("In paddle")
            ball.dy *= -1
        else:
            print("not in paddle")
    else:
        print("not in paddle")
    print(padpos1)
    print(mouseX, mouseY)   
 """   
    


class Brick:
    def __init__(self, pos_x, pos_y, w, h):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.active = True
        self.BrickColour = random.randint(50, 255)
        
    def draw(self):            
        if self.active == True:
            fill(self.BrickColour)        
            rect(self.pos_x, self.pos_y, self.w, self.h)
        #else:
            #fill(0,0,0,0)
            #rect(self.pos_x, self.pos_y, self.w, self.h)
        
    def erase(self):
        self.active = False
        #fill(0, 0, 0, 255)
        #rect(self.pos_x, self.pos_y, self.w, self.h)
        
    def hit_test(self, x, y):
        x_state = x > self.pos_x and x < self.pos_x + self.w
        y_state = y > self.pos_y and y < self.pos_y + self.h
        hit_test_state = x_state and y_state
        return hit_test_state    
    
            
        
class Ball:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = 0
        self.dy = 0
        self.sz = 10
        self.padpos = 0
        self.lives = 3
    
    def draw(self):
        global time
        self.pos_x = self.pos_x + self.dx
        self.pos_y = self.pos_y + self.dy
    
        if self.pos_x > width - self.sz/2:
            self.dx *= -1
            
        if self.pos_x < self.sz/2:
            self.dx *= -1
        if self.pos_y > height-50 - self.sz/2:
            if self.paddle_hit_detection():
                self.dy *= -1
        if self.pos_y > height+100 - self.sz/2:
            self.new_life()
        if self.pos_y < 30 + self.sz/2:
            self.dy *= -1
                    
        fill(255)
        circle(self.pos_x,self.pos_y, self.sz)
        for i in range(self.lives):
            circle(10+i * 20, 15, self.sz)
        
        
    def paddle_hit_detection(self):        
        if self.pos_x > self.padpos - 20 and self.pos_x < self.padpos + 20 and self.pos_y < height-49:
            on_the_paddle = True
        else:
            on_the_paddle = False
            print(on_the_paddle)
        return on_the_paddle
    def new_life(self):
        if self.lives > 0:
            self.lives -=1
            self.dx = 0
            self.dy = 0
            self.pos_x = self.padpos
            self.pos_y = 445
        else:
            print("gameover")
