from os import listdir
from os.path import isfile, join

from modules.converter.three_format import generate_tiles

import click
@click.command()
# Каталог иходных панорам
@click.option('--path', default='./assets/panoramas/', help='Укажите путь до каталога с панорамами')
@click.option('--results_path', default='./results/', help='Укажите путь до каталог результатов')
@click.option('--levels', default='3', help='Укажите количество генерируемых уровней качества (целое число)')
@click.option('--initial_quality', default='0.5', help='Укажите ачальное качество относительно исходного изображения (от 0 до 1)')
def main (path, results_path, levels, initial_quality):
    # Именование уровней (опционально)
    level_names = None
    # level_names = {0: "low", 1: "medium", 2: "high"}
    # level_names = {0: "low", 1: "low-medium", 2: "medium", 3: "medium-high", 4: "high"}

    levels = int(levels)
    initial_quality = float(initial_quality)

    # Парсим пути до панорам
    images = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith((".jpg", ".jpeg",".gif",".png",".tga", ".webp")) ]
    
    for i in images[1:2]:
        generate_tiles(
            image_path = path + i,
            result_path = results_path + ''.join(i.split('.')[:-1]),
            levels = levels,
            quality = initial_quality,
            level_names = level_names 
        )

if __name__ == '__main__':
    main()
