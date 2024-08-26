import pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((1024, 720))
pygame.display.set_caption("Simple Game")
image = pygame.image.load('gambar/gambar.jpeg')
# Memuat suara
sound = pygame.mixer.Sound('audio/audio.mp3')

# Loop utama permainan
x=0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

    # Memutar suara
    sound.play()
    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()