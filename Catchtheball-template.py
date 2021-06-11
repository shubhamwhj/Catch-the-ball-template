
import pygame, sys, random

pygame.init()
clock=pygame.time.Clock()
game_font=pygame.font.Font('freesansbold.ttf', 12)
gameover_font=pygame.font.Font('freesansbold.ttf', 32)
screen = pygame.display.set_mode((500,500))
score=0

#creating objects of game
ball=pygame.Rect(250,100,20,20)

player=pygame.Rect(225,470,80,20)
playerSpeed=15

def game():
    global ball
    global player
    global score
    ball.y=ball.y+7
    scoretext=game_font.render("Score : " + str(score),False,(150,200,200))
    if(ball.colliderect(player)):
        ball.y=-20
        ball.x=random.randint(0, 480)
        score=score+1 
    if(ball.y>500):
        over=gameover_font.render("Game Over",False,(200,200,200))
        screen.blit(over,(160,200))
        player.y=-100
    screen.blit(scoretext,(10,10))

while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    
    
    pygame.draw.rect(screen,(223,100,100),ball)
    pygame.draw.rect(screen,(225,225,225),player)
    game()
    pygame.display.update()
    clock.tick(30)





