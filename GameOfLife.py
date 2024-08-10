import pygame
import sys
import time
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Conway's Game Of Life")
generated=False
grid_state=[[False]*30 for _ in range(40)]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
        elif(event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):generated=True
    if(pygame.mouse.get_pressed()==(True,False,False)):
        x,y=pygame.mouse.get_pos()
        if(grid_state[x//20][y//20]):grid_state[x//20][y//20]=False
        else:grid_state[x//20][y//20]=True
        time.sleep(0.25)
    if(generated):
        create_list=[]
        delete_list=[]
        for i in range(40):
            for j in range(30):
                surrounding_live=0
                for x in range(abs(i-1),i+2):
                    for y in range(abs(j-1),j+2):
                        if(x<40 and y<30):
                            if((x,y)!=(i,j) and grid_state[x][y]):surrounding_live+=1
                if((surrounding_live<2 and grid_state[i][j]==True) or (surrounding_live>3 and grid_state[i][j]==True)):delete_list.append([i,j])
                elif(surrounding_live==3 and grid_state[i][j]==False):create_list.append([i,j])
        for i in range(len(create_list)):grid_state[create_list[i][0]][create_list[i][1]]=True
        for i in range(len(delete_list)):grid_state[delete_list[i][0]][delete_list[i][1]]=False
        time.sleep(1)
    for i in range(40):
        for j in range(30):
            if(grid_state[i][j]==False):pygame.draw.rect(screen,(255,255,255),pygame.Rect((i*20),(j*20),20,20))
            else:pygame.draw.rect(screen,(0,0,0),pygame.Rect((i*20),(j*20),20,20))
    pygame.display.update()
