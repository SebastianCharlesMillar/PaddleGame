key_mode = 1

padpos1 = 0
x = 10

def block():
    fill(3,150,150)
    rect(x, 10, 40, 30)

        
def setup():
    size(500, 500)
    background(0)
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
    

def draw():
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
    frame()
    Innerframe()         
    pushMatrix()
    translate(padpos1,0)       
    paddle()
    popMatrix()
    
    for i in range(12):
        pushMatrix()
        translate(i*40,0)       
        block()
        popMatrix()
        for j in range (10):
            pushMatrix()
            translate(i*40,j*30)
            block()
            popMatrix()
           
    
   



  #create a keystroke mode when keyboard is used
     #within the keystroke mode we have left and right movement with keys
  
  #create a mouse mode when the mouse is used
     #within mouse mode we have left and right movement with the mouse
     
     
#when KeyPressed start key control
    #left key press moves left
    #right key press moves right
    
#when mousePressed start mouse control
    #mousex follows mouse
