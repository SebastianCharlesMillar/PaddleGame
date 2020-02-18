import random
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
    
    def erase(self):
        self.active = False
    
    def hit_test(self, x, y):
        x_state = x > self.pos_x and x < self.pos_x + self.w
        y_state = y > self.pos_y and y < self.pos_y +self.h
        hit_test_state = x_state and y_state
        return hit_test_state
    
                    
    
