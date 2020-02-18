import BallClass
import BrickClass
padpos = -10
padpos1 = 0   
key_mode = 0
 
def setup():
    size(500,500)
    background(0)
    global ball
    global Bricks
    Bricks = [] 
    for i in range(10):    #drawing bricks 10 columns wide
        for j in range(8): #drawing bricks 8 rows high
            brick1 = BrickClass.Brick(10 + i*48, 30+j*20, 48, 20) #coordinates for the first brick 
            Bricks.append(brick1) 
    ball = BallClass.Ball(300, 445) 

          
def paddle():
    fill(255)
    circle(padpos, 460, 20)
    circle(padpos + 20, 460, 20)
    rect(padpos, 450, 20, 20)

def draw():
    global ball
    global Bricks
    background(0)
    fill(100)
    rect(-1, 0, width+1, 30)
    ball.draw()
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
            ball.dy = -2
    if key_mode == 0:
        padpos1 = mouseX
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
    translate(padpos1,0)       
    paddle()
    popMatrix()
    ball.padpos = padpos1     
    

def youWin():
    fill(3, 169, 252);
    textSize(90);
    text("You Win", (width/2)-200, height/2);

    
     
