import random
import os
from threading import Thread
from tkinter import *

import pygame

curdir = os.path.dirname(__file__)

def start_game() -> None:
    global run

    global start_time
    global curret_time
    global obs_gen_time

    global new_record_menu

    global bg_x

    global score_surface
    global point_surface
    global new_record_surface
    global new_record_rect
    global point_rect
    global record_rect
    global again_rect
    global play_rect
    global how_to_play_rect

    global new_record_menu
    global record_surface

    # Инициализируем pygame
    pygame.init()

    # Объевляем переменные и константы
    WIDTH = 1200
    HEIGHT = 600

    start_time = 0

    obs_gen_time = 0

    bg_x = 0
    bg_y = 0

    new_record_menu = False

    clock = pygame.time.Clock()

    # Создание окна
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Загрузка изображений
    background = pygame.image.load(os.path.join(curdir, 'files\game_file\\background.png')).convert()
    menu = pygame.image.load(os.path.join(curdir, 'files\game_file\\menu.png')).convert()
    font = pygame.font.Font(os.path.join(curdir, 'files\game_file\\font.ttf'), 75)
    big_font = pygame.font.Font(os.path.join(curdir, 'files\game_file\\font.ttf'), 100)

    again = pygame.image.load(os.path.join(curdir, 'files\game_file\\again_ru.png')).convert()
    how_to_play = pygame.image.load(os.path.join(curdir, 'files\game_file\\how_to_play_ru.png')).convert()
    play = pygame.image.load(os.path.join(curdir, 'files\game_file\\play_ru.png')).convert()

    soft_name_htp = 'Как играть?'
    curret_time = 0


    # Создание классов
    class Hero(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()

            self.hero_fly1 = pygame.image.load(os.path.join(curdir, 'files\game_file\\hero1.png')).convert_alpha()
            self.hero_fly2 = pygame.image.load(os.path.join(curdir, 'files\game_file\\hero2.png')).convert_alpha()
            self.hero_fly3 = pygame.image.load(os.path.join(curdir, 'files\game_file\\hero3.png')).convert_alpha()
            self.hero_fly = [self.hero_fly1, self.hero_fly2, self.hero_fly3]
            self.hero_index = 0

            self.image = self.hero_fly[self.hero_index]
            self.rect = self.image.get_rect(midbottom=(155, 500))

            self.gravity = 0

        def animation_state(self):
            self.hero_index += 0.25
            if self.hero_index >= len(self.hero_fly):
                self.hero_index = 0
            self.image = self.hero_fly[int(self.hero_index)]

        def player_input(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.rect.midbottom[1] >= 500:
                self.gravity = -50

        def apply_gravity(self):
            self.gravity += 3.5
            self.rect.y += self.gravity
            if self.rect.bottom >= 500:
                self.rect.bottom = 500

        def update(self):
            self.player_input()
            self.apply_gravity()
            self.animation_state()


    class Obstacle(pygame.sprite.Sprite):
        def __init__(self, type):
            super().__init__()

            fly1 = pygame.image.load(os.path.join(curdir, 'files\game_file\\fly1.png')).convert_alpha()
            fly2 = pygame.image.load(os.path.join(curdir, 'files\game_file\\fly2.png')).convert_alpha()
            fly3 = pygame.image.load(os.path.join(curdir, 'files\game_file\\fly3.png')).convert_alpha()
            self.frames = [fly1, fly2, fly3]
            self.animation_index = 0
            self.image = self.frames[self.animation_index]

            if type == 'fly':
                y_pos = 250
            else:
                y_pos = 500
            self.rect = self.image.get_rect(midbottom=(random.randint(1250, 1375), y_pos))

        def animation_state(self):
            self.animation_index += 0.5
            if self.animation_index >= len(self.frames):
                self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]

        def update(self):
            self.animation_state()
            self.rect.x -= 20
            self.destroy()

        def destroy(self):
            if self.rect.x <= -100:
                self.kill()


    # Функции

    # Обновление квдратов и поверхностей
    def surface_rect_update() -> None:
        global score_surface
        global point_surface
        global new_record_surface
        global new_record_rect
        global point_rect
        global record_rect
        global again_rect
        global play_rect
        global how_to_play_rect

        # Обновление надписей
        record_surface = big_font.render(f'Ваш рекорд: {record_point}', False, (32, 32, 32))
        point_surface = big_font.render(f'Ваш счет:  {curret_time}', False, (32, 32, 32))
        new_record_surface = big_font.render('У вас новый рекорд!', False, (32, 32, 32))

        # Обновление квадратов надписей
        new_record_rect = new_record_surface.get_rect(center=(600, 100))
        point_rect = point_surface.get_rect(center=(600, 235))
        record_rect = record_surface.get_rect(center=(600, 75))

        # Обновление квадратов кнопок
        again_rect = again.get_rect(midbottom=(600, 450))
        play_rect = play.get_rect(midbottom=(600, 275))
        how_to_play_rect = how_to_play.get_rect(midtop=(600, 300))


    # Движение фона
    def background_update() -> None:
        global bg_x

        bg_x -= 15
        if bg_x <= -1200:
            bg_x = 0


    # Счет на экране
    def display_score() -> None:
        global curret_time
        curret_time = int(pygame.time.get_ticks() / 1000) - int(start_time / 1000)
        score_surf = font.render(f'{curret_time}', False, (32, 32, 32))
        score_rect = score_surf.get_rect(center=(600, 75))
        screen.blit(score_surf, score_rect)


    # Меню в котором показано как играть
    def htp() -> None:
        tk = Tk()
        # tk.protocol('WM_DELETE_WINDOW')
        tk.title(soft_name_htp)
        tk.resizable(0, 0)
        canvas = Canvas(tk, width=600, height=300, bd=0, highlightthickness=0)
        canvas.pack()
        image = PhotoImage(file=os.path.join(curdir, 'files\game_file\\table_ru.png'))
        label = Label(tk)
        label.image = image
        label['image'] = label.image
        label.place(x=0, y=0)
        tk.mainloop()


    # Надпись на случай если игрок установит новый рекорд
    def new_record_func(nrm: bool) -> None:
        global again_rect
        global new_record_menu
        global point_surface
        global point_rect
        global record_surface

        if nrm:
            new_record_menu = True
            point_surface = big_font.render(f'Ваш счет:  {curret_time}', False, (32, 32, 32))
            record_surface = big_font.render(f'Ваш рекорд:  {curret_time}', False, (32, 32, 32))
            point_rect = record_surface.get_rect(center=(600, 230))
            again_rect = again.get_rect(midbottom=(600, 450))
        else:
            new_record_menu = False
            surface_rect_update()


    # Проверка на столкновение игрока с препядствием
    def collision_sprite() -> None:
        # Проверка на столкновение с препядствием
        if pygame.sprite.spritecollideany(player.sprite, obstacle_group):
            obstacle_group.empty()
            # Вычисление рекорда
            with open(os.path.join(curdir, 'files\game_file\\record.txt'), 'r') as record_file:
                record = int(record_file.read())
            # Проверка установлен ли новый рекорд
            if int(record) < int(curret_time):
                with open(os.path.join(curdir, 'files\game_file\\record.txt'), 'w') as record_file:
                    record_file.write(str(curret_time))
                new_record_func(True)
            else:
                new_record_func(False)

            return 1
        else:
            return 2


    # Генератор препядствий
    def ostacle_generator() -> None:
        global obs_gen_time
        if obs_gen_time <= 0:
            if random.randint(0, 10) == 2:
                if random.randint(0, 1):
                    type = 'small'
                else:
                    type = 'fly'
                obstacle_group.add(Obstacle(type))
                obs_gen_time = 660
        else:
            obs_gen_time -= 30


    player = pygame.sprite.GroupSingle()
    player.add(Hero())

    obstacle_group = pygame.sprite.Group()

    with open(os.path.join(curdir, 'files\game_file\\record.txt'), 'r') as record_file:
        record_point = int(record_file.read())

    # Создание надписей
    record_surface = big_font.render(f'Ваш рекорд: {record_point}', False, (32, 32, 32))
    point_surface = big_font.render(f'Ваш счет:  {curret_time}', False, (32, 32, 32))
    new_record_surface = big_font.render('У вас новый рекорд!', False, (32, 32, 32))

    # Создание квадратов надписей
    new_record_rect = new_record_surface.get_rect(center=(600, 100))
    point_rect = point_surface.get_rect(center=(600, 450))
    record_rect = record_surface.get_rect(center=(600, 75))

    # Создание квадратов кнопок
    again_rect = again.get_rect(midbottom=(600, 450))
    play_rect = play.get_rect(midbottom=(600, 275))
    how_to_play_rect = how_to_play.get_rect(midtop=(600, 300))
    # Цикл событий
    game_status = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                continue

        if game_status == 0:
            screen.blit(menu, (0, 0))
            screen.blit(play, play_rect)
            screen.blit(how_to_play, how_to_play_rect)
            screen.blit(record_surface, record_rect)

            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_rect.collidepoint(mouse_pos):
                        game_status = 2
                        start_time = pygame.time.get_ticks()
                        continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if how_to_play_rect.collidepoint(mouse_pos):
                        Thread(target=htp, daemon=True).start()
                        continue

        elif game_status == 1:
            if new_record_menu:
                screen.blit(menu, (0, 0))
                screen.blit(again, again_rect)
                screen.blit(new_record_surface, new_record_rect)
                screen.blit(point_surface, point_rect)

                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if again_rect.collidepoint(mouse_pos):
                            game_status = 2
                            obstacle_group.empty()
                            start_time = pygame.time.get_ticks()
                            continue
            else:
                screen.blit(menu, (0, 0))
                screen.blit(again, again_rect)
                screen.blit(point_surface, point_rect)
                screen.blit(record_surface, record_rect)

                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if again_rect.collidepoint(mouse_pos):
                            game_status = 2
                            obstacle_group.empty()
                            start_time = pygame.time.get_ticks()
                            continue

        elif game_status == 2:

            ostacle_generator()

            screen.blit(background, (bg_x, bg_y))
            screen.blit(background, (bg_x + 1200, bg_y))
            background_update()

            display_score()

            player.draw(screen)
            player.update()

            obstacle_group.draw(screen)
            obstacle_group.update()

            game_status = collision_sprite()

        pygame.display.update()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    start_game()
