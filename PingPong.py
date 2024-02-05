import pygame 
import random

pygame.init()

#PARAMETERS

HEIGHT=450
WIDTH=750

FPS=60

VELOCITY=20
JOYSTICK_WIDTH=10
JOYSTICK_HEIGHT=45

BALL_RADIUS=20
BALL_VEL_X,BALL_VEL_Y=3,3
BALL_MULTIPLIER=1.25

WALL_THICKNESS=3

BACKGROUND_COLOUR=(249, 229, 12)

pygame.display.set_caption('Ping Pong')
window=pygame.display.set_mode((WIDTH,HEIGHT))

def Ball_movement(BALL):
    #BALL MOVEMENT
    global BALL_VEL_X,BALL_VEL_Y
    
    BALL.x+=BALL_VEL_X
    
    if BALL.x+BALL_RADIUS<=WIDTH:
        BALL_VEL_X=BALL_VEL_X*-1
    if BALL.x>=0:
        BALL_VEL_X=BALL_VEL_X*-1
    
    BALL.y+=BALL_VEL_Y
    
    if BALL.y+BALL_RADIUS<=HEIGHT:
        BALL_VEL_Y=BALL_VEL_Y*-1
    if BALL.y>=0:
        BALL_VEL_Y=BALL_VEL_Y*-1


def main():
    global BALL_VEL_X,BALL_VEL_Y

    #SHAPE SIZES & LOCATIONS 

    RIGHT=pygame.Rect(WIDTH-18,HEIGHT/2-25,JOYSTICK_WIDTH,JOYSTICK_HEIGHT)
    LEFT=pygame.Rect(8,HEIGHT/2-25,JOYSTICK_WIDTH,JOYSTICK_HEIGHT)
    BALL=pygame.Rect(WIDTH/2-10,HEIGHT/2-10,BALL_RADIUS,BALL_RADIUS)

    R_WALL=pygame.Rect(WIDTH-WALL_THICKNESS,0,WALL_THICKNESS,HEIGHT)
    L_WALL=pygame.Rect(0,0,WALL_THICKNESS,HEIGHT)

    T_ROOF=pygame.Rect(0,0,WIDTH,WALL_THICKNESS)
    B_ROOF=pygame.Rect(0,HEIGHT-WALL_THICKNESS,WIDTH,WALL_THICKNESS)

    R_SCORE=0
    L_SCORE=0
    

    clock=pygame.time.Clock()

    run=True
    while run:
        clock.tick(FPS)
        
        #SCORE
        FONT=pygame.font.Font('freesansbold.ttf',28)
        SCORE=FONT.render(str(L_SCORE)+' '+str(R_SCORE),True,(50,50,100))    
        
        #CLOSING THE GAME
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

            #PLAYER MOVEMENT

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w and LEFT.y-VELOCITY>=3:
                    LEFT.y-=VELOCITY
                if event.key==pygame.K_s and LEFT.y+VELOCITY+JOYSTICK_HEIGHT<=HEIGHT-1:
                    LEFT.y+=VELOCITY
                if event.key==pygame.K_UP and RIGHT.y-VELOCITY>=3:
                    RIGHT.y-=VELOCITY
                if event.key==pygame.K_DOWN and RIGHT.y+VELOCITY+JOYSTICK_HEIGHT<=HEIGHT-1:
                    RIGHT.y+=VELOCITY
                    
        
        #BALL COLLISIONS

        if BALL.colliderect(LEFT):
            BALL_VEL_X=BALL_VEL_X*-1*BALL_MULTIPLIER
        
        if BALL.colliderect(RIGHT):
            BALL_VEL_X*=-1*BALL_MULTIPLIER
        
        if BALL.colliderect(R_WALL):
            BALL.x,BALL.y=WIDTH/2-10,HEIGHT/2-10
            BALL_VEL_X=random.choice([3,-3])
            L_SCORE+=1
        if BALL.colliderect(L_WALL):
            BALL.x,BALL.y=WIDTH/2-10,HEIGHT/2-10
            BALL_VEL_X=random.choice([3,-3])
            R_SCORE+=1
        if R_SCORE==10 or L_SCORE==10:
            run=False
            
        Ball_movement(BALL)

        

        #RENDERING/DRAWING THE SHAPES AND OBJECTS

        window.fill(BACKGROUND_COLOUR)
        window.blit(SCORE,(WIDTH/2-21,3))
        pygame.draw.rect(window, (34, 45, 94),RIGHT)
        pygame.draw.rect(window, (34, 45, 94),LEFT)
        pygame.draw.ellipse(window, (34, 45, 94),BALL)
        pygame.draw.rect(window,(50,50,100),R_WALL)
        pygame.draw.rect(window,(50,50,100),L_WALL)
        pygame.draw.rect(window,(50,50,100),B_ROOF)
        pygame.draw.rect(window,(50,50,100),T_ROOF)
        pygame.draw.rect(window,(50,50,100),(WIDTH/2-WALL_THICKNESS,0,WALL_THICKNESS,HEIGHT))         
        pygame.display.flip()

    pygame.QUIT



if __name__=='__main__':
    main()