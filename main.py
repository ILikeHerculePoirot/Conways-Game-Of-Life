import pygame
import sys
import time
pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("Conway's Game Of Life")
white=pygame.image.load("Dead.png").convert()
black=pygame.image.load("Live.png").convert()
icon=pygame.image.load("Icon.png").convert()
pygame.display.set_icon(icon)
generated=False
def draw(grid_state,grid_coords):
    i=0
    while(i<10):
        j=0
        while(j<10):
            if(grid_state[i][j]==False):screen.blit(white,grid_coords[i][j])
            else:screen.blit(black,grid_coords[i][j])
            j+=1
        i+=1
grid_state=[[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False,False]]
grid_coords=[[[0,0],[0,40],[0,80],[0,120],[0,160],[0,200],[0,240],[0,280],[0,320],[0,360]],[[40,0],[40,40],[40,80],[40,120],[40,160],[40,200],[40,240],[40,280],[40,320],[40,360]],[[80,0],[80,40],[80,80],[80,120],[80,160],[80,200],[80,240],[80,280],[80,320],[80,360]],[[120,0],[120,40],[120,80],[120,120],[120,160],[120,200],[120,240],[120,280],[120,320],[120,360]],[[160,0],[160,40],[160,80],[160,120],[160,160],[160,200],[160,240],[160,280],[160,320],[160,360]],[[200,0],[200,40],[200,80],[200,120],[200,160],[200,200],[200,240],[200,280],[200,320],[200,360]],[[240,0],[240,40],[240,80],[240,120],[240,160],[240,200],[240,240],[240,280],[240,320],[240,360]],[[280,0],[280,40],[280,80],[280,120],[280,160],[280,200],[280,240],[280,280],[280,320],[280,360]],[[320,0],[320,40],[320,80],[320,120],[320,160],[320,200],[320,240],[320,280],[320,320],[320,360]],[[360,0],[360,40],[360,80],[360,120],[360,160],[360,200],[360,240],[360,280],[360,320],[360,360]]]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:sys.exit()
        elif(event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):generated=True
    if(pygame.mouse.get_pressed()==(True,False,False)):
        x,y=pygame.mouse.get_pos()
        if(grid_state[(x-(x%40))//40][(y-(y%40))//40]):grid_state[(x-(x%40))//40][(y-(y%40))//40]=False
        else:grid_state[(x-(x%40))//40][(y-(y%40))//40]=True
        time.sleep(0.25)
    if(generated):
        create_list=[]
        delete_list=[]
        i=0
        while(i<10):
            j=0
            while(j<10):
                surrounding_live=0
                if(i==0):
                    if(j==0):
                        if(grid_state[i][j+1]):surrounding_live+=1
                        if(grid_state[i+1][j]):surrounding_live+=1
                        if(grid_state[i+1][j+1]):surrounding_live+=1
                    elif(j==9):
                        if(grid_state[i][j-1]):surrounding_live+=1
                        if(grid_state[i+1][j]):surrounding_live+=1
                        if(grid_state[i+1][j-1]):surrounding_live+=1
                    else:
                        if(grid_state[i][j-1]):surrounding_live+=1
                        if(grid_state[i][j+1]):surrounding_live+=1
                        if(grid_state[i+1][j-1]):surrounding_live+=1
                        if(grid_state[i+1][j]):surrounding_live+=1
                        if(grid_state[i+1][j+1]):surrounding_live+=1
                elif(i==9):
                    if(j==0):
                        if(grid_state[i][j+1]):surrounding_live+=1
                        if(grid_state[i-1][j]):surrounding_live+=1
                        if(grid_state[i-1][j+1]):surrounding_live+=1
                    elif(j==9):
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
                elif(j==9):
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
                j+=1
            j=0
            i+=1
        i=0
        while(i<len(create_list)):
            grid_state[create_list[i][0]][create_list[i][1]]=True
            i+=1
        i=0
        while(i<len(delete_list)):
            grid_state[delete_list[i][0]][delete_list[i][1]]=False
            i+=1
        time.sleep(1)
    draw(grid_state,grid_coords)
    pygame.display.update()