import asyncio
import pygame

from app.utils import change_players_positions
from app.player_class import Player
from app.poker_round import poker_round
from app.constant import FPS
from app.menu import menu_start, menu_end


# Create players
START_STACK = 5000
Player('Alice', START_STACK, 'human')
Player('Bob', START_STACK, 'AI')


async def main():
    """
    Function starts the game
    :return: run game
    """

    pygame.init()
    clock = pygame.time.Clock()

    run = True
    player_list_chair = Player.player_list_chair

    while run:
        clock.tick(FPS)

        # menu
        menu_start()
        while len(player_list_chair) > 1:

            # Play a round
            poker_round()

            # Shift the button to the next player
            change_players_positions(shift=1)

            # Reset properties for each player
            [player.next_round() for player in player_list_chair]

            # If someone has lost ask if he want new game
            for player in player_list_chair:
                if player.stack == 0:
                    rebuy = menu_end()
                    if rebuy:
                        for p in player_list_chair:
                            p.stack = START_STACK

            # Remove players who have lost
            [player_list_chair.remove(player) for player in player_list_chair if player.stack == 0]

            if len(player_list_chair) == 1:
                run = False
                break
        await asyncio.sleep(0)

    pygame.quit()


if __name__ == '__main__':
    asyncio.run(main())

