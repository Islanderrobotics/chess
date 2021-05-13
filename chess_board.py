import sys
import pygame
from settings import Settings
class Chess_Game:
    def __init__(self):
        # initialize the game and create game resources
        pygame.init()

        self.black = (0, 0, 0) # RGB color for black

        self.white = (255, 255, 255) # RGB color for white

        # self.screen = pygame.display.set_mode((8, 8))

        self.lead_x = 0 # coordinates for display box
        self. lead_y = 0 # coordinates for display box
        pygame.display.set_caption("Welcome to Chess!")
    def board(self):

        black_first_border = 800
        self.white_border = black_first_border-50
        display_size = 1000
        # print(white_border)
        b_box = 770
        self.gameDisplay = pygame.display.set_mode((display_size, display_size))
        self.gameDisplay.fill(self.white)
        pygame.draw.rect(self.gameDisplay, self.black, [self.lead_x + (display_size - black_first_border) / 2, self.lead_y + (display_size - black_first_border) / 2, black_first_border, black_first_border])
        pygame.draw.rect(self.gameDisplay,self.white,[self.lead_x+(display_size-self.white_border)/2, self.lead_y+(display_size - self.white_border)/2,self.white_border,self.white_border])
        pygame.display.update()
        # variable for black boxes
        # for loop
        # use i within for loop to place each box with pygame.draw.rect

        for i in range(1,6):
            pygame.draw.rect(self.gameDisplay, self.black, [(self.lead_x + b_box)*i,
                                                            (self.lead_y + b_box),
                                                            20, 20])
        pygame.display.update()
    def run_game(self):# this will be the driver
        """This function will start the loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.board()
            pygame.display.flip()





