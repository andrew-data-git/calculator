
import pygame as pg

import functions
from utils import *
from button import Button

# Initial conditions
WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOUR = (100, 0, 0)

# Instantiate pygame
pg.init()
DISPLAY = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Pygame Calculator')
main_clock = pg.time.Clock()

# Elements
button_labels = [
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '*'],
    ['temp1', '0', 'temp2', '/'],
    ['neg', '^y', 'bksp', 'C']
]

# Variables
out_text = 00000
input_started = False
in_text = ''

if __name__ == '__main__':

    # Main Loop ---------------------------------------------------------------------
    running = True
    while running == True:
        
        # Draw --------------------------
        DISPLAY.fill(BACKGROUND_COLOUR)
        draw_title(surface=DISPLAY, title_text="Andrew's Calculator")
        if input_started:
            draw_input(surface=DISPLAY, text=in_text)
        else:
            draw_input(surface=DISPLAY, text='INPUT')
            in_text = ''
        draw_output(surface=DISPLAY, text=str(out_text))

        # Create num buttons
        buttons = []
        for i, row in enumerate(button_labels):
            for j, col in enumerate(row):
                button = Button(
                    surface=DISPLAY, 
                    text=button_labels[i][j],
                    x_pos=150 + j*50, 
                    y_pos=150 + i*50, 
                    width=40, 
                    height=30)
                button.draw()
                buttons.append(button)

        # Create GO button
        go_button = Button(
                    surface=DISPLAY, 
                    text='GO',
                    x_pos=WIDTH-100, 
                    y_pos=HEIGHT/2, 
                    width=80, 
                    height=100)
        go_button.draw()
        # buttons.append(go_button)

        # Events ------------------------
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False 
            if event.type == pg.MOUSEBUTTONDOWN:
                if go_button.rect.collidepoint(event.pos):
                    input_started = False
                    in_text = 'INPUT'
                    out_text += 1
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        input_started = True
                        in_text += button.clicked()

        # Run ---------------------------
        pg.display.flip()