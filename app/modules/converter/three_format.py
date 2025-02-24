from PIL.Image import open, LANCZOS
from os import makedirs
from modules.utils.half import halve_n_times
from math import floor

# Функция для нарезки тайлов
def slice_image(image_path, result_path, level_folder, scale_factor):
    """Разрезает изображение на тайлы 256x256 с указанным масштабом."""
    image = open(image_path)
    width, height = image.size
    makedirs(result_path, exist_ok=True)
    image = image.resize((int(width * scale_factor), int(height * scale_factor)), LANCZOS)
    lvl_dir = f"{result_path}/{level_folder}"
    makedirs(lvl_dir, exist_ok=True)
    img_w, img_h = image.size

    # Разбиваем на тайлы 256x256
    for y in range(0, img_h, 256):
        for x in range(0, img_w, 256):
            tile = image.crop((x, y, min(x + 256, img_w), min(y + 256, img_h)))
            tile.save(f"{lvl_dir}/{x//256}_{y//256}.png")

# Генерация тайлов для нескольких уровней качества
def generate_tiles(image_path, result_path, levels, quality = 1.0, level_names = None):
    print('Исходное изображение: ' + image_path)
    for l in range(1, levels + 1):
        q = halve_n_times(quality, l - 1)
        level_folder = level_names[levels-l] if level_names else str(floor(q * 100))
        print('Создаем тайлы ' + '[' + level_folder + ']' + ' (' + str(floor(q * 100)) + '% качества исходного изображения)')
        slice_image(image_path, result_path, level_folder, scale_factor=q)
    print('Готово! \nКаталог с тайлами: ' + result_path + '\n\n')

