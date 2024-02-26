import pygame
import sys
import time
pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("Conway's Game Of Life")
generated=False
grid_state=[[False for i in range(20)] for i in range(20)]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
        elif(event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):generated=True
    if(pygame.mouse.get_pressed()==(True,False,False)):
        x,y=pygame.mouse.get_pos()
        if(grid_state[(x-(x%20))//20][(y-(y%20))//20]):grid_state[(x-(x%20))//20][(y-(y%20))//20]=False
        else:grid_state[(x-(x%20))//20][(y-(y%20))//20]=True
        time.sleep(0.25)
    if(generated):
        create_list=[]
        delete_list=[]
        for i in range(20):
            for j in range(20):
                surrounding_live=0
                if(i==0):
                    if(j==0):
                        if(grid_state[i][j+1]):surrounding_live+=1
                        if(grid_state[i+1][j]):surrounding_live+=1
                        if(grid_state[i+1][j+1]):surrounding_live+=1
                    elif(j==19):
                        if(grid_state[i][j-1]):surrounding_live+=1
                        if(grid_state[i+1][j]):surrounding_live+=1
                        if(grid_state[i+1][j-1]):surrounding_live+=1
                    else:
                        if(grid_state[i][j-1]):surrounding_live+=1
                        if(grid_state[i][j+1]):surrounding_live+=1
                        if(grid_state[i+1][j-1]):surrounding_live+=1
                        if(grid_state[i+1][j]):surrounding_live+=1
                        if(grid_state[i+1][j+1]):surrounding_live+=1
                elif(i==19):
                    if(j==0):
                        if(grid_state[i][j+1]):surrounding_live+=1
                        if(grid_state[i-1][j]):surrounding_live+=1
                        if(grid_state[i-1][j+1]):surrounding_live+=1
                    elif(j==19):
                        if(grid_state[i][j-1]):surrounding_live+=1
                        if(grid_state[i-1][j]):surrounding_live+=1
                        if(grid_state[i-1][j-1]):surrounding_live+=1
                    else:
                        if(grid_state[i][j-1]):surrounding_live+=1
                        if(grid_state[i][j+1]):surrounding_live+=1
                        if(grid_state[i-1][j-1]):surrounding_live+=1
                        if(grid_state[i-1][j]):surrounding_live+=1
                        if(grid_state[i-1][j+1]):surrounding_live+=1
                elif(j==0):
                    if(grid_state[i-1][j]):surrounding_live+=1
                    if(grid_state[i+1][j]):surrounding_live+=1
                    if(grid_state[i-1][j+1]):surrounding_live+=1
                    if(grid_state[i][j+1]):surrounding_live+=1
                    if(grid_state[i+1][j+1]):surrounding_live+=1
                elif(j==19):
                    if(grid_state[i-1][j]):surrounding_live+=1
                    if(grid_state[i+1][j]):surrounding_live+=1
                    if(grid_state[i-1][j-1]):surrounding_live+=1
                    if(grid_state[i][j-1]):surrounding_live+=1
                    if(grid_state[i+1][j-1]):surrounding_live+=1
                else:
                    if(grid_state[i-1][j-1]):surrounding_live+=1
                    if(grid_state[i-1][j]):surrounding_live+=1
                    if(grid_state[i-1][j+1]):surrounding_live+=1
                    if(grid_state[i][j-1]):surrounding_live+=1
                    if(grid_state[i][j+1]):surrounding_live+=1
                    if(grid_state[i+1][j-1]):surrounding_live+=1
                    if(grid_state[i+1][j]):surrounding_live+=1
                    if(grid_state[i+1][j+1]):surrounding_live+=1
                if((surrounding_live<2 and grid_state[i][j]==True) or (surrounding_live>3 and grid_state[i][j]==True)):delete_list.append([i,j])
                elif(surrounding_live==3 and grid_state[i][j]==False):create_list.append([i,j])
        for i in range(len(create_list)):grid_state[create_list[i][0]][create_list[i][1]]=True
        for i in range(len(delete_list)):grid_state[delete_list[i][0]][delete_list[i][1]]=False
        time.sleep(1)
    for i in range(20):
        for j in range(20):
            if(grid_state[i][j]==False):pygame.draw.rect(screen,(255,255,255),pygame.Rect((i*20),(j*20),20,20))
            else:pygame.draw.rect(screen,(0,0,0),pygame.Rect((i*20),(j*20),20,20))
    pygame.display.update()
