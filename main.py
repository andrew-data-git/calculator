'''Main file for simple calculator app
May require CLI input: 
$ export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
'''
import os
os.environ["LD_PRELOAD"] = "/usr/lib/x86_64-linux-gnu/libstdc++.so.6"
print("LD_PRELOAD set to:", os.environ["LD_PRELOAD"])

import pygame as pg

from calc import *
from utils import *
from button import Button


# Pygame conditions 
WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOUR = (50, 50, 50)
pg.init()
pg.display.set_caption('Pygame Calculator')
DISPLAY = pg.display.set_mode((WIDTH, HEIGHT))

# Instantiate calculator
calc = Calculation()
button_labels = [
    [1, 2, 3, '+'],
    [4, 5, 6, '-'],
    [7, 8, 9, '*'],
    ['.', 0, '^', '/'],
]

# Run -------------------------------------------------------------------------------
if __name__ == '__main__':
    running = True

    # Main Loop ---------------------------------------------------------------------
    while running == True:
        
        # Draw ----------------------------------------------------------------------
        DISPLAY.fill(BACKGROUND_COLOUR)
        draw_title(surface=DISPLAY, title_text="Andrew's Calculator")
        draw_input(surface=DISPLAY, text=calc.input_text)
        draw_output(surface=DISPLAY, text=str(calc.result))

        # Create num buttons
        buttons = []
        for i, row in enumerate(button_labels):
            for j, col in enumerate(row):
                button = Button(
                    surface=DISPLAY, 
                    value=button_labels[i][j],
                    x_pos=100 + j*50, 
                    y_pos=150 + i*50, 
                    width=40, 
                    height=30)
                button.draw()
                buttons.append(button)

        # Create Equals and Cancel buttons
        equals = Button(
                    surface=DISPLAY, 
                    value='Eval',
                    x_pos=WIDTH-180, 
                    y_pos=HEIGHT/2-20, 
                    width=80, 
                    height=100)
        equals.draw()

        cancel = Button(
                    surface=DISPLAY, 
                    value='C',
                    x_pos=WIDTH-180, 
                    y_pos=150, 
                    width=80, 
                    height=60)
        cancel.draw()
        buttons.append(cancel)

        # Events --------------------------------------------------------------------
        for event in pg.event.get():

            # QUIT
            if event.type == pg.QUIT:
                running = False 

            # CLICK BUTTON
            if event.type == pg.MOUSEBUTTONDOWN: # if clicked

                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        calc.ingest(
                            button.clicked()
                            )

                if equals.rect.collidepoint(event.pos):
                    calc.evaluate()

        # Update --------------------------------------------------------------------
        pg.display.flip()