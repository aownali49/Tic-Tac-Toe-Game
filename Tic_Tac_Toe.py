import pygame
pygame.init()

s_width=550
s_height=600

win=pygame.display.set_mode((s_width,s_height))

pygame.display.set_caption("Tic_Tac_Toe")

sm=pygame.image.load(r'D:\Game 3\side menu.png')
icon=pygame.image.load(r'D:\Game 3\icon.png')
front=pygame.image.load(r'D:\Game 3\Front.png')
menu=pygame.image.load(r'D:\Game 3\menu tic.png')

g_over=pygame.image.load(r'D:\Game 3\QeMS.gif')

p1wins=0
p2wins=0
total_games=0
tie_game=0
tie_check=False

font=pygame.font.SysFont(None,30)
font1=pygame.font.SysFont("comicsan",60)

rect1= pygame.draw.rect(win,(255,255,255),(15,15,100,100))
rect2=pygame.draw.rect(win,(255,255,255),(130,15,100,100))
rect3=pygame.draw.rect(win,(255,255,255),(245,15,100,100))

rect4=pygame.draw.rect(win,(255,255,255),(15,130,100,100))
rect5=pygame.draw.rect(win,(255,255,255),(130,130,100,100))
rect6=pygame.draw.rect(win,(255,255,255),(245,130,100,100))

rect7=pygame.draw.rect(win,(255,255,255),(15,245,100,100))
rect8=pygame.draw.rect(win,(255,255,255),(130,245,100,100))
rect9=pygame.draw.rect(win,(255,255,255),(245,245,100,100))
def startscr():
    global p1wins,p2wins,tie_game,total_games,player,tie_check,win_count
    if not tie_check:    
        if player == "1":
            p1wins+=1
        else:
            p2wins+=1
    else:
        tie_game+=1
        tie_check=False
    total_games+=1
    player='2'
    win_count=0
    for x in range(1,10):
        board[str(x)] = " "
        
def redraw():
    count=1
    win.fill((0,255,255,100))

    win.blit(sm,(350,0))
    side_menu()

    rect1= pygame.draw.rect(win,(255,255,255),(15,15,100,100))
    rect2=pygame.draw.rect(win,(255,255,255),(130,15,100,100))
    rect3=pygame.draw.rect(win,(255,255,255),(245,15,100,100))

    rect4=pygame.draw.rect(win,(255,255,255),(15,130,100,100))
    rect5=pygame.draw.rect(win,(255,255,255),(130,130,100,100))
    rect6=pygame.draw.rect(win,(255,255,255),(245,130,100,100))

    rect7=pygame.draw.rect(win,(255,255,255),(15,245,100,100))
    rect8=pygame.draw.rect(win,(255,255,255),(130,245,100,100))
    rect9=pygame.draw.rect(win,(255,255,255),(245,245,100,100))

    for i in board.values():
        if count==1 and i=="1" :
            pygame.draw.circle(win,(255,0,0),(65,65),30)
        if count==1 and i=="2" :
            pygame.draw.circle(win,(0,255,0),(65,65),30)
            

        if count==2 and i=="1" :
            pygame.draw.circle(win,(255,0,0),(180,65),30)
        if count==2 and i=="2" :
            pygame.draw.circle(win,(0,255,0),(180,65),30)


        if count==3 and i=="1" :
            pygame.draw.circle(win,(255,0,0),(295,65),30)
        if count==3 and i=="2" :
            pygame.draw.circle(win,(0,255,0),(295,65),30)


        if count==4 and i=="1" :
            pygame.draw.circle(win,(255,0,0),(65,177),30)
        if count==4 and i=="2" :
            pygame.draw.circle(win,(0,255,0),(65,177),30)


        if count==5 and i=="1" :
            pygame.draw.circle(win,(255,0,0),(180,177),30)
        if count==5 and i=="2" :
            pygame.draw.circle(win,(0,255,0),(180,177),30)


        if count==6 and i=="1" :
            pygame.draw.circle(win,(255,0,0),(295,177),30)
        if count==6 and i=="2" :
            pygame.draw.circle(win,(0,255,0),(295,177),30)


        if count==7 and i=="1" :
            pygame.draw.circle(win,(255,0,0),(65,295),30)
        if count==7 and i=="2" :
            pygame.draw.circle(win,(0,255,0),(65,295),30)


        if count==8 and i=="1" :
            pygame.draw.circle(win,(255,0,0),(180,295),30)
        if count==8 and i=="2" :
            pygame.draw.circle(win,(0,255,0),(180,295),30)


        if count==9 and i=="1" :
            pygame.draw.circle(win,(255,0,0),(295,295),30)
        if count==9 and i=="2" :
            pygame.draw.circle(win,(0,255,0),(295,295),30)
            
        count+=1        
        
    pygame.display.update()
def end_scr():
    win.fill((0,255,255))
    mes=font1.render("Game Over ",1,(255,0,0))
    win.blit(mes,(160,70))
   
    global p1wins,p2wins,tie_game,total_games

    win.blit(sm,(170,100))
    
    mess=font.render("Total Games : " + str(total_games),1,(255,255,255))
    win.blit(mess,(190,180))

    mess=font.render("Player One : " + str(p1wins),1,(255,255,255))
    win.blit(mess,(190,250))

    mess=font.render("Player Two : " + str(p2wins),1,(255,255,255))
    win.blit(mess,(190,320))
    
    mess=font.render("Tie Game : " + str(tie_game),1,(255,255,255))
    win.blit(mess,(190,400))

    pygame.display.update()
    pygame.time.delay(3000)



def checkwin():
    if board['1'] == board['2'] == board['3'] != " ":
        return True
    elif board['4'] == board['5'] == board['6'] != " ":
        return True
    elif board['7'] == board['8'] == board['9'] != " ":
        return True
    elif board['1'] == board['4'] == board['7'] != " ":
        return True
    elif board['2'] == board['5'] == board['8'] != " ":
        return True
    elif board['3'] == board['6'] == board['9'] != " ":
        return True
    elif board['1'] == board['5'] == board['9'] != " ":
        return True
    elif board['3'] == board['5'] == board['7'] != " ":
        return True
    else:
        return False
def side_menu():
    global p1wins,p2wins,tie_game,total_games
    
    mess=font.render("Total Games : " + str(total_games),1,(255,255,255))
    win.blit(mess,(370,80))

    mess=font.render("Player One : " + str(p1wins),1,(255,255,255))
    win.blit(mess,(370,150))

    mess=font.render("Player Two : " + str(p2wins),1,(255,255,255))
    win.blit(mess,(370,220))
    
    mess=font.render("Tie Game : " + str(tie_game),1,(255,255,255))
    win.blit(mess,(370,300))

    
    
win_count=0
playercheck=False

player = "1"
board={"1":" ",
       "2":" ",
       "3":" ",
       "4":" ",
       "5":" ",
       "6":" ",
       "7":" ",
       "8":" ",
       "9":" "
       }
def main():
    global win_count,playercheck,player
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end_scr()
                game_over=True
            if event.type==pygame.MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                if rect1.collidepoint(pos):
                    if board["1"]== " ":
                        board["1"] = player
                        playercheck=True
                        win_count+=1
                if rect2.collidepoint(pos):
                    if board["2"]== " ":
                        board["2"] = player
                        playercheck=True
                        win_count+=1
                if rect3.collidepoint(pos):
                    if board["3"]== " ":
                        board["3"] = player
                        playercheck=True
                        win_count+=1
                if rect4.collidepoint(pos):
                    if board["4"]== " ":
                        board["4"] = player
                        playercheck=True
                        win_count+=1
                if rect5.collidepoint(pos):
                    if board["5"]== " ":
                        board["5"] = player
                        playercheck=True
                        win_count+=1
                if rect6.collidepoint(pos):
                    if board["6"]== " ":
                        board["6"] = player
                        playercheck=True
                        win_count+=1
                if rect7.collidepoint(pos):
                    if board["7"]== " ":
                        board["7"] = player
                        playercheck=True
                        win_count+=1
                if rect8.collidepoint(pos):
                    if board["8"]== " ":
                        board["8"] = player
                        playercheck=True
                        win_count+=1
                if rect9.collidepoint(pos):
                    if board["9"]== " ":
                        board["9"] = player
                        playercheck=True
                        win_count+=1
                if checkwin() == True:
                    redraw()
                    mess=font.render("Player " + str(player+' Wins...'),1,(255,255,255))
                    win.blit(mess,(50,400))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    startscr() 
                    print(player+ 'WINS')
                elif win_count == 9:
                    redraw()
                    mess=font.render("Game Tied... ",1,(255,255,255))
                    win.blit(mess,(50,400))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    tie_check=True
                    startscr()
                    print('Game Tie')
                if playercheck:
                    playercheck=False
                    if player == "1":
                        player="2"
                    else:
                        player="1"




        redraw()
def menu_scr():
    run=True
    frontpage()
    while run:
        win.fill((0,255,255))
        ret1=pygame.draw.rect(win,(0,255,0),(150,435,250,40),1)
        ret2=pygame.draw.rect(win,(0,255,0),(150,510,250,40),1)
        win.blit(icon,(150,80))
        win.blit(menu,(125,400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONUP:
                posi=pygame.mouse.get_pos()
                if ret1.collidepoint(posi):
                    main()
                elif ret2.collidepoint(posi):
                    run=False
                    
                    
                
                
def frontpage():
    win.blit(front,(0,0))
    mess=font.render("Loading... ",1,(255,255,255))
    win.blit(mess,(240,530))
    pygame.display.update()
    pygame.time.delay(3000)
menu_scr()

pygame.quit()

