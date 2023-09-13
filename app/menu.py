import pygame.transform
from app.constant import BACKGROUND_MENU, button_new_game_image, button_exit_image

ratio = 2
button_width = int(576 / ratio)
button_height = int(220 / ratio)


class Button:
    def __init__(self, x, y, image, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.draft = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def isOver(self, mouse_position):
        if self.draft.collidepoint(mouse_position):
            return True
        return False


def menu_start():
    """
    The function displays the menu
    :return:
    """
    from app.constant import WIN, WIDTH
    WIN.blit(BACKGROUND_MENU, (0, 0))
    button_new_game = Button((WIDTH - button_width)//2, 200, button_new_game_image, button_width, button_height)
    button_exit = Button((WIDTH - button_width)//2, 400, button_exit_image, button_width, button_height)

    pause_menu = True
    while pause_menu:
        button_exit.draw(WIN)
        button_new_game.draw(WIN)

        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_new_game.isOver(mouse_position):
                    pause_menu = False
                if button_exit.isOver(mouse_position):
                    run = False
                    pygame.quit()
                    quit()

        pygame.display.flip()


def menu_end():
    from app.player_class import Player
    from app.constant import WIN, WIDTH, BEIGE

    player_list_chair = Player.player_list_chair
    for player in player_list_chair:
        if player.stack != 0:
            winner = player.name
    WIN.blit(BACKGROUND_MENU, (0, 0))
    font = pygame.font.SysFont('comicsans', 60)
    text = font.render(winner+' won the game', True, BEIGE)
    WIN.blit(text, ((WIDTH - text.get_width()) // 2, 100))
    button_new_game = Button((WIDTH - button_width)//2, 300, button_new_game_image, button_width, button_height)
    button_exit = Button((WIDTH - button_width)//2, 500, button_exit_image, button_width, button_height)
    rebuy = False
    pause_menu = True
    while pause_menu:
        button_exit.draw(WIN)
        button_new_game.draw(WIN)

        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_new_game.isOver(mouse_position):
                    rebuy = True
                    pause_menu = False
                if button_exit.isOver(mouse_position):
                    run = False
                    pygame.quit()
                    quit()

        pygame.display.flip()
    return rebuy