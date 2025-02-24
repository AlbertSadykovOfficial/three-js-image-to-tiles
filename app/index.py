from os import listdir
from os.path import isfile, join

from modules.converter.three_format import generate_tiles

if __name__ == '__main__':
    # Именование уровней (опционально)
    # level_names = {0: "low", 1: "medium", 2: "high"}
    # Каталог иходных панорам
    inital_path = './assets/panoramas/'
    # Каталог результатов
    results_path = './results/'
    # Кол-во уровней детализации
    # (Каждый уровень детализации по качеству хуже в 2 раза, чем предыдущий)
    levels = 5
    # Начальное качество относительно исходного изображения
    initial_quality = 1

    # Парсим пути до панорам
    images = [f for f in listdir(inital_path) if isfile(join(inital_path, f)) and f.endswith((".jpg", ".jpeg",".gif",".png",".tga", ".webp")) ]

    for i in images[-1:]:
        generate_tiles(
            inital_path + i,
            results_path + ''.join(i.split('.')[:-1]),
            levels,
            initial_quality,
            level_names = None
        )
