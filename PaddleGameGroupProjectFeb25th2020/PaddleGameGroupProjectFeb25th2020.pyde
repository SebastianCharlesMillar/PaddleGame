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
t= -750
y= -750 
def setup():
    
    word = 'bbbbbbbbbbrrrrrrrrrrrbbbbbbbbbbrrrrrrrrrbrbbbbbbbbbbbrrrrrrrrrrrbbbbbbbbbbbbbbrrrrrrrrbbbbbbbbbbbb'   
    word_num = 0
    print(word)
    size(700, 500)
    background(50)
    global ball ,imgBG , imgTop, imgBot
    global Bricks , img, t, y
    Bricks = []
    imgTop = loadImage("Top.png")
    imgBot = loadImage("Bottom.png")
    imgBG = loadImage("GlowBack.png")
    for i in range(15):
        for j in range(8):
            brick1 = BrickClass.Brick(10 + i*48, 30+j*20, 48, 20, word[word_num])
            Bricks.append(brick1)
            word_num +=1
            if word_num == len(word):
                word_num = 0
    ball = BallClass.Ball(300, 445)
    img = loadImage("BlackBackground9.png")
    #Bricks[10].erase()
      
    
    
def draw():
    
    global ball, prev_padpos, score, game_won
    global Bricks , imgBG
    global padpos1 , img, t, y , key_mode
    background(0, 0, 0)
    image(imgBG,0,0)
    fill(100)
    rect(-1,0, width+1, 30)
    if (not game_won) and (not ball.game_over):    
        
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
        t = ball.pos_x - 1000
        y = ball.pos_y - 1000
            
        if keyPressed:
                key_mode = 1
                if ball.dx == 0 and key == " ":
                    ball.dx = sqrt(ball.speed/2)
                    ball.dy = -1 *  ball.dx
        #Ball release with mouse        
        if mousePressed:
                key_mode = 0
                if ball.dx ==0:
                    ball.dx = sqrt(ball.speed/2)
                    ball.dy = -1 *  ball.dx
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
        if padpos1 >= 670: 
                padpos1 = 670                
        if padpos1 <= 30: 
                padpos1 = 30
    
        #Locking Ball to paddle when ball x position is at 0    
        if ball.dx ==0:
            ball.pos_x = padpos1
        image(img,t,y)
        image(imgTop,0,0)
        image(imgBot,0,-100)
        ball.draw(padpos1 - prev_padpos)    
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
    
