import pygame

# create list of buttons
class buttons:
    buttonlist = []

    # add buttons to list
    def add(self, bt):
        self.buttonlist.append(bt)

    # draw all buttons
    def draw(self, win):
     for bt in self.buttonlist:
          bt.draw(win, (0, 0, 0))

    # process events for all buttons
    def proc_event(self, event):
        pos = pygame.mouse.get_pos()
        for bt in self.buttonlist:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bt.isOver(pos):
                    bt.clicked(pos)
            if event.type == pygame.MOUSEMOTION:
                bt.mouseover(bt.isOver(pos))