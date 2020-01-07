key_mode = 1

padpos1 = 0
x = 10

    
def frame():
    fill(145)
    rect (0, 0, 500, 500)
def Innerframe():
    fill(45)
    rect (10, 10, 480, 480)
padpos= -10    

def paddle():
    fill(255)
    circle(padpos , 460 , 20)
    circle(padpos + 20 , 460, 20)
    rect(padpos, 450 , 20 , 20)

def setup():
    size(500,500)

    background(0,0,0)
    x=0
    y=30
    
    fill (193)
    rect(x,y,width, height)
    
    fill (8, 3, 61)
    
    rect (x+10,y+10,width-20, height-50)
    

    for i in range(10):
        for j in range(8):
            Blue = random(0, 10)
            Red = random (2,255)
            Green = random (0,10)
            fill (Red, Green, Blue)
            rect (x+10+ i*48, y+10+j*20, 48, 20)
            

        
def draw():
    """
    if frameCount%120 == 0:
        stroke(8, 3, 61) 
        fill (8, 3, 61, 80)
        rect (10,200,width-20, height-50)
        stroke(255, 255, 0, ) 
        fill( 255, 255, 255, 0)
        for i in range(250):
            Xpos = random(15, 485)
            Ypos = random (202,485)
            Size = random (.1,.5)
            circle( Xpos, Ypos, Size)
    if frameCount%360 ==0:
        stroke(8, 3, 61) 
        fill (8, 3, 61, 50)
        rect (10,200,width-20, height-50)
    """
    stroke(8, 3, 61) 
    fill (8, 3, 61, 1)
    rect (10,200,width-20, height-50)
    if frameCount%2 == 0:
        stroke(255, 255, 0, ) 
        fill( 255, 255, 255, 0)
        Xpos = random(15, 485)
        Ypos = random (202,485)
        Size = random (.1,.5)
        circle(Xpos, Ypos, Size)
        
        stroke(8, 3, 61) 
        fill (8, 3, 61)
        Xpos = random(10, 465)
        Ypos = random (200,465)
        rect (Xpos, Ypos, 25, 25)
        
    if frameCount%5 == 0:    
        for i in range(10):
            for j in range(8):
                Blue = random(0, 10)
                Red = random (2,255)
                Green = random (0,10)
                fill (Red, Green, Blue, 40)
                rect (10+ i*48, 40+j*20, 48, 20)



    global padpos1
    global key_mode
    if keyPressed:
        key_mode = 1
    if mousePressed:
        key_mode = 0
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
    pushMatrix()
    translate(padpos1,0)       
    paddle()
    popMatrix()

    
    
"""
    for j in range(100):         
        positionX = map(random(0,1), 0, 1, 15, 385)
        positionY = map(random(0,1), 0, 1, 200, 385)
        
        
    for i in range(8):  
        stroke(255, 255, 0)
        strokeWeight(1)      
        x = 5 * cos(2*PI/8 * i)
        y = 5 * sin(2*PI/8 * i)
        line ( 200, 200, 200+ x, 200+y)
"""
