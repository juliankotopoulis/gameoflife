
import pygame
class slider():
    def __init__(self,  x, y, width, height, initial, min, max, text='', nomousecolor = (0,255,0), ):
        self.color = nomousecolor
        self.nomousecolor = nomousecolor
        self.min = min
        self.max = max
        self.x = x
        self.y = y
        self.initial = initial
        self.width = width
        self.height = height
        self.text = text
        self.value = initial


    def draw(self, win):
        # Call this method to draw the button on the screen
        s = 18
        knob_pos = (self.value - self.min)/(self.max - self.min) * self.width
        pygame.draw.rect(win, (50,205,50), (self.x, self.y + 0.5 * self.height, self.width , 20), 0)
        pygame.draw.rect(win, (210,105,30), (self.x + knob_pos - s * 1/2, self.y + 0, s, self.height + 20), 0)


        if self.text != '':
            font = pygame.font.SysFont(None, 40)
            text = font.render(self.text, 1, (0, 0, 0))
            text_size= text.get_width()
            win.blit(text, (
            self.x - 200 + (self.width / 2 - text.get_width() / 2), self.y + 10))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def clicked(self, pos):
        print ("clicked: " + str(pos)+ ", " + str(self.value))
        new_value = (pos[0]-self.x) * (self.max-self.min)/self.width +self.min
       # if pos[0] >= self.value:
      #          self.value = new_value
      #  if pos[0] <= self.value:
        self.value = int(new_value)

