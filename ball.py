import pygame
import random

# Inisialisasi pygame
pygame.init()

# Mengatur dimensi layar
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Ball")

# Warna
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Suara
catch_sound = pygame.mixer.Sound("catch.mp3")  # Pastikan file 'catch.wav' ada
miss_sound = pygame.mixer.Sound("miss.wav")  # Suara saat bola terlewat
pygame.mixer.music.load("background_music.mp3")  # Pastikan file 'background_music.mp3' ada
pygame.mixer.music.play(-1)  # Mainkan musik secara looping

# Kecepatan pemain dan bola
player_speed = 10
ball_speed = 5

# Ukuran pemain
player_width = 100
player_height = 20

# Inisialisasi posisi pemain
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10

# Inisialisasi bola
ball_x = random.randint(0, screen_width - 20)
ball_y = 0
ball_radius = 20

# Skor dan nyawa
score = 0
lives = 3
font = pygame.font.SysFont(None, 35)

# Fungsi untuk menampilkan skor dan nyawa
def show_score(x, y, score, lives):
    text = font.render(f"Score: {score}   Lives: {lives}", True, black)
    screen.blit(text, (x, y))

# Fungsi untuk menampilkan pesan di layar
def message_display(text):
    large_text = pygame.font.SysFont(None, 75)
    text_surface = large_text.render(text, True, black)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)  # Tunggu 2 detik sebelum menghapus pesan

# Game loop
running = True
while running:
    screen.fill(white)
    
    # Event loop untuk menangani input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Mendapatkan input keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    
    # Menggerakkan bola
    ball_y += ball_speed
    
    # Reset bola jika jatuh ke bawah
    if ball_y > screen_height:
        lives -= 1
        pygame.mixer.Sound.play(miss_sound)  # Mainkan suara jika terlewat
        ball_y = 0
        ball_x = random.randint(0, screen_width - ball_radius)
        if lives == 0:
            message_display("Game Over")
            running = False
    
    # Cek tabrakan
    if (ball_y + ball_radius >= player_y and
        player_x <= ball_x <= player_x + player_width):
        score += 1
        ball_y = 0
        ball_x = random.randint(0, screen_width - ball_radius)
        ball_speed += 0.5  # Tingkatkan kecepatan bola seiring skor naik
        pygame.mixer.Sound.play(catch_sound)  # Mainkan suara saat bola tertangkap
    
    # Menggambar pemain dan bola
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)
    
    # Menampilkan skor dan nyawa
    show_score(10, 10, score, lives)
    
    # Mengupdate layar
    pygame.display.update()

    # Atur FPS (frame per detik)
    pygame.time.Clock().tick(60)

# Keluar dari pygame
pygame.quit()
