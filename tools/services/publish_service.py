import re
import shutil
import zipfile

from loguru import logger

from tools import configs
from tools.configs import path_define


def make_release_zips():
    path_define.releases_dir.mkdir(parents=True, exist_ok=True)

    for font_format in configs.font_formats:
        file_path = path_define.releases_dir.joinpath(f'hzk-pixel-font-{font_format}-v{configs.version}.zip')
        with zipfile.ZipFile(file_path, 'w') as file:
            file.write(path_define.project_root_dir.joinpath('LICENSE-FONT.md'), 'README.md')
            for font_config in configs.font_configs:
                font_file_name = f'hzk-pixel-{font_config.font_size}px.{font_format}'
                file.write(path_define.outputs_dir.joinpath(font_file_name), font_file_name)
        logger.info("Make release zip: '{}'", file_path)


def update_docs():
    path_define.docs_dir.mkdir(parents=True, exist_ok=True)

    for path_from in path_define.outputs_dir.iterdir():
        if re.match(r'preview-.*px\.png', path_from.name) is None:
            continue
        path_to = path_define.docs_dir.joinpath(path_from.name)
        shutil.copyfile(path_from, path_to)
        logger.info("Copy file: '{}' -> '{}'", path_from, path_to)


def update_www():
    if path_define.www_fonts_dir.exists():
        shutil.rmtree(path_define.www_fonts_dir)
    path_define.www_fonts_dir.mkdir(parents=True)

    for path_from in path_define.outputs_dir.iterdir():
        if re.match(r'.*\.otf.woff2', path_from.name) is None:
            continue
        path_to = path_define.www_fonts_dir.joinpath(path_from.name)
        shutil.copyfile(path_from, path_to)
        logger.info("Copy file: '{}' -> '{}'", path_from, path_to)
