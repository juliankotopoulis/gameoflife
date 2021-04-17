import pygame

# Reusable button
# Pass coordinates and function to be called

class button():
    def __init__(self,  x, y, width, height, fn, text='', nomousecolor = (0,255,0), mouseovercolor = (255,0,0)):
        self.color = nomousecolor
        self.nomousecolor = nomousecolor
        self.mouseovercolor = mouseovercolor
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.fn = fn

    # Draw the button on the screen
    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        # Create the font, color, and location of the button
        if self.text != '':
            #font = pygame.font.Font(None, 40)
            font = pygame.font.SysFont(None, 40)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    # Pos is the mouse position or a tuple of (x,y) coordinates
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    # If the button is clicked call registered function
    def clicked(self, pos):
        self.fn(pos)

    # Change color of button when mouse is over button
    def mouseover(self,is_mouseover):
        if is_mouseover:
            self.color = self.mouseovercolor
        else:
            self.color = self.nomousecolor