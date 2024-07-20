from PIL import Image, ImageFont, ImageDraw
from loguru import logger

from tools.configs import FontConfig
from tools.configs import path_define


def make_preview_image_file(font_config: FontConfig):
    font = ImageFont.truetype(path_define.outputs_dir.joinpath(f'{font_config.outputs_name}.woff2'), font_config.size)
    text_color = (0, 0, 0, 255)

    image = Image.new('RGBA', (font_config.size * 27, font_config.size * 11), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.text((font_config.size, font_config.size), '汉字库像素字体 / HZK Pixel Font', fill=text_color, font=font)
    draw.text((font_config.size, font_config.size * 3), '我们度过的每个平凡的日常，也许就是连续发生的奇迹。', fill=text_color, font=font)
    draw.text((font_config.size, font_config.size * 5), 'THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.', fill=text_color, font=font)
    draw.text((font_config.size, font_config.size * 7), 'the quick brown fox jumps over a lazy dog.', fill=text_color, font=font)
    draw.text((font_config.size, font_config.size * 9), '0123456789', fill=text_color, font=font)
    image = image.resize((image.width * 2, image.height * 2), Image.Resampling.NEAREST)

    path_define.outputs_dir.mkdir(parents=True, exist_ok=True)
    file_path = path_define.outputs_dir.joinpath(font_config.preview_image_file_name)
    image.save(file_path)
    logger.info("Make preview image file: '{}'", file_path)