import pygame
import sys
from game_window_class import *
from button_class import *

pygame.display.set_caption("ABDELRAHMAN'S GAME OF LIFE")
gameIcon = pygame.image.load('C:/Users/Abdelrahman/OneDrive/Desktop/Cellullar Atomata/Icons/GOL.jpg')
pygame.display.set_icon(gameIcon)
WIDTH, HEIGHT = 700, 700
BACKGROUND = (184, 215, 255)
FPS = 25

#--------------------------------SETTING FUNCTIONS-------------------------------#

def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()
def update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos,game_state=state)
def draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

#--------------------------------RUNNING FUNCTIONS-------------------------------#

def running_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()
def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos,game_state=state)
    game_window.evaluate()
def running_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()

#--------------------------------PAUSED FUNCTIONS-------------------------------#

def paused_get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()
def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos,game_state=state)
def paused_draw():
    window.fill(BACKGROUND)
    for button in buttons:
        button.draw()
    game_window.draw()


def mouse_on_grid(pos):
    if pos[0] > 100 and pos[0] < WIDTH-100:
        if pos[1] > 180 and pos[1] < HEIGHT-20:
            return True
    return False

def click_cell(pos):
    grid_pos = [pos[0]-100, pos[1]-180]
    grid_pos[0] = grid_pos[0]//20
    grid_pos[1] = grid_pos[1]//20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True

def make_buttons():
    buttons = []
    buttons.append(Button(window,WIDTH//2-50,50,100,30,text='RUN',color=(28,111,51),
                          hover_color=(48,131,81),bold_text=True,function=run_game,state='setting'))
    buttons.append(Button(window, WIDTH // 2 - 50, 50, 100, 30, text='PAUSE', color=(18, 104, 135),
                          hover_color=(51, 168, 212), bold_text=True,function=pause_game,state='running'))
    buttons.append(Button(window, WIDTH // 4 - 50, 50, 100, 30, text='RESET', color=(117, 14, 14),
                          hover_color=(217, 54, 54), bold_text=True,function=reset_grid,state='paused'))
    buttons.append(Button(window, WIDTH // 1.25 - 50, 50, 100, 30, text='RESUME', color=(28,111,51),
                          hover_color=(48,131,81), bold_text=True, function=run_game, state='paused'))
    return buttons

def run_game():
    global state
    state = 'running'
def pause_game():
    global state
    state = 'paused'
def reset_grid():
    global state
    state = 'setting'
    game_window.reset_grid()

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window,100,180)
buttons = make_buttons()
state = 'setting'

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
sys.exit()