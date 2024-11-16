'''Objects and helper tools'''

import pygame as pg
from button import Button

def draw_title(surface: None, title_text: str) -> None:
    WINDOW_WIDTH, _ = pg.display.get_window_size()
    font = pg.font.Font(None, 28)
    text = font.render(
        "Andrew's Calculator", True, (255, 255, 255)
        )
    text_rect = text.get_rect(
        center=(WINDOW_WIDTH/2, 80)
        )
    surface.blit(text, text_rect)

def draw_output(surface: None, text: str) -> None:
    _, WINDOW_HEIGHT = pg.display.get_window_size()
    font = pg.font.SysFont('courier', 30)
    text = font.render(
        text, True, (255, 255, 255), (0, 0, 0)
        )
    text_rect = text.get_rect(
        midleft=(100, WINDOW_HEIGHT-90))
    surface.blit(text, text_rect)    

def draw_input(surface: None, text: str) -> None:
    _, WINDOW_HEIGHT = pg.display.get_window_size()
    font = pg.font.SysFont('courier', 30)
    text = font.render(
        text, True, (255, 255, 255), (0, 0, 0)
        )
    text_rect = text.get_rect(
        midleft=(100, WINDOW_HEIGHT-130)
        )
    surface.blit(text, text_rect)    