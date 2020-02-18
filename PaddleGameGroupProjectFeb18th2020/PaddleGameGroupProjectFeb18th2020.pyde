import random
import BallClass
import BrickClass
key_mode = 0
padpos= -10 
padpos1 = 0
prev_padpos = 0
score = 0
game_won = False

def paddle():
    fill(255)
    circle(padpos , 460 , 20)
    circle(padpos + 20 , 460, 20)
    rect(padpos, 450 , 20 , 20)
import random
    
BrickColour = 255

def setup():
    word = 'bbbbbbbbbbrrrrrrrrrrrbbbbbbbbbbrrrrrrrrrr   #This line can consist as many symbols you can. However only ''b'' and ''r'' are recognized. All the rest symbols are going t obe skipped during the level bulding. I don''t know, files did not work at all'
    word_num = 0
    print(word)
    size(500, 500)
    background(0)
    global ball
    global Bricks
    Bricks = []
    for i in range(10):
        for j in range(8):
            brick1 = BrickClass.Brick(10 + i*48, 30+j*20, 48, 20, word[word_num])
            Bricks.append(brick1)
            word_num +=1
            if word_num == len(word):
                word_num = 0
    ball = BallClass.Ball(300, 445)
    #Bricks[10].erase()
      
    
    
def draw():
    
    global ball, prev_padpos, score, game_won
    global Bricks
    global padpos1
    background(0, 0, 0)
    fill(100)
    rect(-1,0, width+1, 30)
    if (not game_won) and (not ball.game_over):    
        ball.draw(padpos1 - prev_padpos)
        prev_padpos = padpos1
        count = 0
        #Bricks[random.randint(0, 79)].erase()
        for i in range(len(Bricks)):
            if Bricks[i].hit_test(ball.pos_x, ball.pos_y):
                if Bricks[i].bottom_hit_test(ball.pos_x, ball.pos_y):
                    ball.dy *= -1
                else:
                    ball.dx *= -1
                score += Bricks[i].points
                Bricks[i].erase()    
            Bricks[i].draw()
            if Bricks[i].active:
                count += 1
        if count == 0:
            game_won = True
    #Ball release with spacebar        
        
        global key_mode
        if keyPressed:
            key_mode = 1
            if ball.dx == 0 and key == " ":
                ball.dx = 2
                ball.dy = -2 
    #Ball release with mouse        
        if mousePressed:
            key_mode = 0
            if ball.dx ==0:
                ball.dx = 2 
                ball.dy = -2
        if key_mode == 0:
            padpos1 = mouseX        
    
        #ball.pos_x = mouseX
        #ball.pos_y = mouseY
    
    #Paddle Movement left and right with keys    
        if key_mode == 1:     
            if keyPressed:
                if keyCode == LEFT:
                    padpos1 = padpos1 - 10
                    
                if keyCode == RIGHT:
                    padpos1 = padpos1 + 10
    #Limit Paddle Movement to keep within the frame along x axis                
        if padpos1 >= 470: 
            padpos1 = 470                
        if padpos1 <= 30: 
            padpos1 = 30
    #Locking Ball to paddle when ball x position is at 0    
        if ball.dx ==0:
            ball.pos_x = padpos1
        pushMatrix()
        #padpos1 = 100
        translate(padpos1,0)       
        paddle()
        popMatrix()
        ball.padpos = padpos1    
        #print(padpos1)
        #print(ball.pos_x)
        #print(ball.pos_y)
        textSize(16)
        text('score', 100, 20)
        text(score, 150, 20)
    else:
        textSize(72)
        fill(255)
        if game_won:
            text('you won', 110, 150)
            text('your score', 75, 275)
            text(score, 190, 400)
        if ball.game_over:
            text('you lost', 110, 150)
            text('your score', 75, 275)
            text(score, 190, 400)
