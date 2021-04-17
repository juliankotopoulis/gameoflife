import pygame
import random

# Define grid for board
class grid_class():
    grid = []


    def __init__(self,  x, y, width, height, rows):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = rows
        self.cursorx = -1
        self.cursory = -1

    # Create grid for board with random cells
    def create_grid(self):
        for x in range(self.rows):
            self.grid.append([])
            for y in range(self.rows):
                random_num = random.randint(0, 9)
                if random_num < 7:
                    random_boolean = 0
                else:
                    random_boolean = 2
                self.grid[x].append(random_boolean)

    # Create an empty grid
    def create_grid_empty(self):
        self.grid = []
        for x in range(self.rows):
            self.grid.append([])
            for y in range(self.rows):
                val = 0
                self.grid[x].append(val)

    # Insert a predefined shape
    def add_shape(self,x, y, shape):
        for point in shape:
            self.grid[x + point[0]][y + point[1]] = 2

    # Update the grid according to the rules
    def update_grid(self):
        grid2 = []
        # print("update_self.grid")
        for x in range(self.rows):
            grid2.append([])
            for y in range(self.rows):
                new_cell = self.stays_alive(x, y)
                grid2[x].append(new_cell)
        self.grid = grid2

    # Draw the cells on the screen
    def draw_cells(self,surface):
        for y in range(self.rows):
            for x in range(self.rows):
                if self.grid[x][y] == 2:
                    self.draw_cell(surface, x, y)
                elif self.grid[x][y] == 1:
                    self.draw_cell(surface, x, y,color =(1,125,1))
        if self.cursorx != -1 and self.cursory != -1:
            self.draw_cell(surface,self.cursorx,self.cursory)

    # Draw a single cell
    def draw_cell(self,surface, x, y,color = (255,255,255)):
        dis = self.width // self.rows
        pygame.draw.rect(surface, color, (x * dis + 1, y * dis + 1, dis - 2, dis - 2))

    # Draw the surviving cells
    def draw(self, win):
        self.drawGridLines(win)

    # Decide if current cell stays alive
    def stays_alive(self,x, y):
        count = 0
        if y > 0:
            if x > 0 and self.grid[x - 1][y - 1] == 2: count += 1
            if self.grid[x][y - 1] == 2: count += 1
            if x < self.rows - 1 and self.grid[x + 1][y - 1] == 2: count += 1
        if x > 0 and self.grid[x - 1][y] == 2: count += 1
        if x < self.rows - 1 and self.grid[x + 1][y] == 2: count += 1
        if y < self.rows - 1:
            if x > 0 and self.grid[x - 1][y + 1] == 2: count += 1
            if self.grid[x][y + 1] == 2: count += 1
            if x < self.rows - 1 and self.grid[x + 1][y + 1] == 2: count += 1

        if self.grid[x][y] == 0 or self.grid[x][y] == 1:
            if count == 3:
                return 2
            else:
                return self.grid[x][y]

        if self.grid[x][y] == 2:
            if count < 2 or count > 3: return 1
            if count == 3 or count == 2: return 2

    # Decide if cell dies
    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    # Under development (but will draw shape where clicked)
    def clicked(self, pos):
        print ("clicked: " + str(pos)+ ", " + str(self.value))
        new_value = (pos[0]-self.x) * (self.max-self.min)/self.width +self.min
   # if pos[0] >= self.value:
  #          self.value = new_value
  #  if pos[0] <= self.value:
        self.value = int(new_value)


    # Draw grid lines on screen
    def drawGridLines(self, surface):
        sizeBtwn = self.width // self.rows


        x = 0
        y = 0
        for l in range(self.rows):
            x = x + sizeBtwn
            y = y + sizeBtwn

            pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, self.width))
            pygame.draw.line(surface, (255, 255, 255), (0, y), (self.width, y))

    #Process mouse event
    def proc_event(self, event):
        pos = pygame.mouse.get_pos()
        cellsize = self.width//self.rows
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.isOver(pos):
                self.cursorx = (pos[0] - self.x)//cellsize
                self.cursory = (pos[1] - self.y)//cellsize
