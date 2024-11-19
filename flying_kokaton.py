import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像surfaceを作成する
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png") #こうかとん画像surfaceを作成する
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect() #こうかとんRectを取得する
    kk_rct.center = 300, 200
    tmr = 0
    move_lst = [(0, -1), (0, +1), (+2, 0), (-2, 0), (0, 0)]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        move = 4
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            move = 0
        elif key_lst[pg.K_DOWN]:
            move = 1
        elif key_lst[pg.K_RIGHT]:
            move = 2
        elif key_lst[pg.K_LEFT]:
            move = 3
        kk_rct.move_ip(move_lst[move]) 
        kk_rct.move_ip(-1, 0)    

        x = -(tmr%3200)
        screen.blit(bg_img,  [x, 0]) #screen surfaceに背景画像surfaceを張り付ける
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img,  [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img,  kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()