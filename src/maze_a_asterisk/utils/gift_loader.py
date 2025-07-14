from PIL import Image
import pygame

def load_gif_frames(filename):
    pil_img = Image.open(filename)
    frames = []

    try:
        while True:
            frame = pil_img.convert('RGBA')
            mode = frame.mode
            size = frame.size
            data = frame.tobytes()

            pg_image = pygame.image.fromstring(data, size, mode)
            frames.append(pg_image)
            pil_img.seek(pil_img.tell() + 1)
    except EOFError:
        pass

    return frames
