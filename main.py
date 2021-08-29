import pygame
import math
import random
a=pygame.image.load('parachute0.png')
pygame.display.set_icon(a)
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parachute Game!")
RADIUS = 20
GAP = 15
let= []
stx = round((WIDTH- (RADIUS * 2 + GAP) * 13) / 2)
sty = 400
A = 65
for i in range(26):
    x = stx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = sty + ((i // 13) * (GAP + RADIUS * 2))
    let.append([x, y, chr(A + i), True])
LET_FONT = pygame.font.SysFont('Dubai Medium', 40)
WOR_FONT = pygame.font.SysFont('Dubai Medium', 60)
TIT_FONT = pygame.font.SysFont('Dubai Medium', 70)
img = []
for i in range(7):
    image = pygame.image.load("parachute" + str(i) + ".png")
    img.append(image)
parachute_status = 0
words = ["OLYMPIC", "PARALYMPIC", "INSPIRATION", "GOLD","SILVER", "BRONZE", "MEDALS", "SPORTS",
         "SWIMMING", "TENNIS", "CRICKET", "FOOTBALL","BATSMAN", "BOWLER", "UMPIRE", "RANKING",
         "ATHLETICS", "HANDBALL", "JAVELEIN", "BADMINTON","FINAL", "ARCHERY", "CHAMPION", "HOCKEY",
         "BOXING", "WRESTLING", "WEIGHTLIFTING", "GOLF"]
word = random.choice(words)
g= []
WHITE = (255,255,255)
BLACK = (0,0,0)
def draw():
    win.fill(WHITE)
    text = TIT_FONT.render("PARACHUTE MAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    display_word = ""
    for letter in word:
        if letter in g:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WOR_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))
    for letter in let:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LET_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(img[parachute_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WOR_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global parachute_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in let:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            g.append(ltr)
                            if ltr not in word:
                                parachute_status += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in g:
                won = False
                break
        
        if won:
            display_message("You WON!")
            break

        if parachute_status == 6:
            display_message("You LOST!")
            break
    pygame.quit()

    
while True:
    
    main()
    pygame.quit()