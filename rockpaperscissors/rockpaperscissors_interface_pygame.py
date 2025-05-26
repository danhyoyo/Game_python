import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)
GREEN = (34, 139, 34)
RED = (220, 20, 60)

# Font
font = pygame.font.SysFont(None, 36)
result_font = pygame.font.SysFont(None, 28)

# Các lựa chọn
options = ["paper", "rock", "scissors"]
buttons = {
    "rock": pygame.Rect(50, 250, 100, 50),
    "paper": pygame.Rect(200, 250, 100, 50),
    "scissors": pygame.Rect(350, 250, 100, 50),
}
quit_button = pygame.Rect(200, 320, 100, 40)

# Hàm xác định kết quả
def get_result(player, bot):
    player_index = options.index(player)
    bot_index = bot
    if (player_index == bot_index + 1) or (player_index == 0 and bot_index == 2):
        return "You lose"
    elif (player_index == bot_index - 1) or (player_index == 2 and bot_index == 0):
        return "You win"
    else:
        return "Tie"

# Kết quả
player_choice = ""
bot_choice = ""
result_text = "Make your choice!"

# Vòng lặp chính
running = True
while running:
    screen.fill(WHITE)

    # Vẽ tiêu đề
    title = font.render("Rock - Paper - Scissors", True, BLACK)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))

    # Vẽ các nút lựa chọn
    for name, rect in buttons.items():
        pygame.draw.rect(screen, BLUE, rect)
        label = font.render(name.capitalize(), True, WHITE)
        screen.blit(label, (rect.x + 10, rect.y + 10))

    # Nút quit
    pygame.draw.rect(screen, RED, quit_button)
    quit_label = font.render("Quit", True, WHITE)
    screen.blit(quit_label, (quit_button.x + 20, quit_button.y + 5))

    # Hiển thị kết quả
    if player_choice:
        choice_text = result_font.render(
            f"You: {player_choice.upper()} | Bot: {options[bot_choice].upper()}", True, BLACK)
        screen.blit(choice_text, (WIDTH//2 - choice_text.get_width()//2, 150))

    result_display = result_font.render(result_text, True, GREEN if "win" in result_text.lower() else RED if "lose" in result_text.lower() else BLACK)
    screen.blit(result_display, (WIDTH//2 - result_display.get_width()//2, 190))

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for name, rect in buttons.items():
                if rect.collidepoint(mouse_pos):
                    player_choice = name
                    bot_choice = random.randint(0, 2)
                    result_text = get_result(player_choice, bot_choice)

            if quit_button.collidepoint(mouse_pos):
                running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
