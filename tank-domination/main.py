import pygame as pg

pg.init()

# Create game screen.
monitor_display = (800, 600)

game_display = pg.display.set_mode(monitor_display)

pg.display.set_caption("Tank Domination")

system_clock = pg.time.Clock()

game_tank_svg = pg.image.load("tank.svg")

game_tank_sprite = pg.transform.scale(game_tank_svg, (75, 75))

game_characteristics = {
    "sky": {
        "color": (135, 206, 235)
    },
    "grass": {
        "color": (0, 255, 0),
        "position": {
            "y": 0.8 * monitor_display[1]
        }
    },
    "player": {
        "position": {
            "x": 0.2 * monitor_display[0]
        },
        "hp": 1
    },
    "cpu": {
        "position": {
            "x": 0.8 * monitor_display[0] - game_tank_sprite.get_width()
        },
        "hp": 1 
    }
}

#Game logic
game_running_flag = True

while game_running_flag:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_running_flag = False

    if not game_running_flag:
        pg.quit()

        break

    key_pressed = pg.key.get_pressed()

    position_delta = 0

    if key_pressed[pg.K_LEFT]:
        position_delta = -1
    elif key_pressed[pg.K_RIGHT]:
        position_delta = 1

    if 0 <= game_characteristics["player"]["position"]["x"] + position_delta and game_characteristics["player"]["position"]["x"] + position_delta + game_tank_sprite.get_width() <= game_characteristics["cpu"]["position"]["x"]:
        game_characteristics["player"]["position"]["x"] += position_delta

    # Game graphics.
    game_display.fill(game_characteristics["sky"]["color"])

    pg.draw.rect(game_display, game_characteristics["grass"]["color"], pg.Rect(0, game_characteristics["grass"]["position"]["y"], monitor_display[0], monitor_display[1] - game_characteristics["grass"]["position"]["y"]))

    game_tank_sprite_player = game_tank_sprite
    
    game_display.blit(game_tank_sprite_player, (game_characteristics["player"]["position"]["x"], game_characteristics["grass"]["position"]["y"] - game_tank_sprite_player.get_height()))

    game_tank_sprite_cpu = pg.transform.flip(game_tank_sprite, True, False)

    game_display.blit(game_tank_sprite_cpu, (game_characteristics["cpu"]["position"]["x"], game_characteristics["grass"]["position"]["y"] - game_tank_sprite_player.get_height()))

    # Render game frame by frame
    pg.display.update()

    system_clock.tick(30)

