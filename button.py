'''Buttons to appear on page'''
import pygame as pg

class Button:
    def __init__(self, surface, value, x_pos, y_pos, width, height):
        self.surface = surface
        self.rect = pg.Rect(x_pos, 
                            y_pos, 
                            width, 
                            height)
        self.value = value
        self.text = str(value)
        self.font = pg.font.Font(None, 18)

    def draw(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            current_button_color = [200,200,200]
        else:
            current_button_color = [250,250,250]

        pg.draw.rect(self.surface, current_button_color, self.rect)
        button_text = self.font.render(self.text, True, [0,0,0])
        text_rect = button_text.get_rect(center=self.rect.center)
        self.surface.blit(button_text, text_rect)
    
    def clicked(self):
        return self.value