import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Case Open Game")

# Fonts and colors
font = pygame.font.SysFont("arial", 28)
big_font = pygame.font.SysFont("arial", 36)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

RARITY_COLORS = {
    "Common": (150, 150, 150),
    "Rare": (0, 102, 204),
    "Epic": (153, 51, 255),
    "Legendary": (255, 204, 0),
    "Mythic": (255, 0, 255)
}

# Items (name, rarity, weight)
items = [
    ("Common Sword", "Common", 60),
    ("Common Shield", "Common", 60),
    ("Common Staff", "Common", 60),
    ("Common Bow", "Common", 60),
    ("Rare Shield", "Rare", 25),
    ("Rare Sword", "Rare", 25),
    ("Rare Staff", "Rare", 25),
    ("Epic Staff", "Epic", 10),
    ("Epic Sword", "Epic", 10),
    ("Legendary Bow", "Legendary", 5),
    ("Easter Egg(Legendeveloper)", "Mythic", 1)
]

# Button setup
button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT - 80, 200, 50)

# Function to open a case
def open_case():
    names = [item[0] for item in items]
    weights = [item[2] for item in items]
    selected = random.choices(items, weights=weights, k=1)[0]
    return selected

# Main game loop
def main():
    result = None
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        # Draw button
        pygame.draw.rect(screen, GRAY, button_rect)
        text = font.render("Open Case", True, BLACK)
        screen.blit(text, (button_rect.x + 40, button_rect.y + 10))

        # Draw result
        if result:
            item_name, rarity, _ = result
            result_text = big_font.render(f"You got: {item_name}", True, RARITY_COLORS[rarity])
            rarity_text = font.render(f"Rarity: {rarity}", True, RARITY_COLORS[rarity])
            screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2, HEIGHT//2 - 50))
            screen.blit(rarity_text, (WIDTH//2 - rarity_text.get_width()//2, HEIGHT//2 + 10))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    result = open_case()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    result = open_case()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
sys.exit()
# This code creates a simple case opening game using Pygame.