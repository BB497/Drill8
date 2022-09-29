from pico2d import *
TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0
dirx = 0
diry = 0
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2

def handle_events():
    global running
    global dirx
    global diry
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    imx = dirx * 100
    if imx < 0:
        character.clip_draw(frame * 100, imx+100, 100, 100, x, y)
        imx = imx + 100
    elif imx > 0:
        character.clip_draw(frame * 100, imx, 100, 100, x, y)
    elif imx == 0:
        character.clip_draw(frame * 100, imx, 100, 100, x, y)
    if x > TUK_WIDTH:
        x = TUK_WIDTH
    elif x < 0:
        x = 0
    if y > TUK_HEIGHT:
        y = TUK_HEIGHT
    elif y < 0:
        y = 0
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 5
    y += diry * 5
    delay(0.01)