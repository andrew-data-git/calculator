'''Buttons to appear on page'''
import pygame as pg

class Button:
    def __init__(self, surface, text, x_pos, y_pos, width, height):
        self.surface = surface
        self.rect = pg.Rect(x_pos, 
                            y_pos, 
                            width, 
                            height)
        self.text = text
        self.font = pg.font.Font(None, 18)

    def draw(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            current_button_color = [50,50,50]
        else:
            current_button_color = [100,100,100]

        pg.draw.rect(self.surface, current_button_color, self.rect)
        button_text = self.font.render(self.text, True, [0,0,0])
        text_rect = button_text.get_rect(center=self.rect.center)
        self.surface.blit(button_text, text_rect)
    
    def clicked(self):
        return self.text