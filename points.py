import pygame


class Points():
    def __init__(self):
        self.points = 0
    
    def add_point(self):
        self.points += 1
    
    def show_points(self):
        return f"Points: {self.points}"
    
    def __str__(self):
        return f"Points: {self.points}"

    def render_points(self, screen):
        font = pygame.font.SysFont(None, 30)
        text_surface = font.render(self.show_points(), True, "white")
        text_rect = text_surface.get_rect()
        text_rect.topright = (100,50)
        screen.blit(text_surface, text_rect)
        