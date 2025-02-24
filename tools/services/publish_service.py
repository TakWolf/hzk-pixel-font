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
            for font_config in configs.font_configs:
                font_file_name = f'hzk-pixel-{font_config.font_size}px.{font_format}'
                file.write(path_define.outputs_dir.joinpath(font_file_name), font_file_name)
        logger.info("Make release zip: '{}'", file_path)


def update_docs():
    for file_dir, _, file_names in path_define.outputs_dir.walk():
        for file_name in file_names:
            if re.match(r'preview-.*px\.png', file_name) is None:
                continue
            path_from = file_dir.joinpath(file_name)
            path_to = path_define.docs_dir.joinpath(path_from.relative_to(path_define.outputs_dir))
            path_to.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path_from, path_to)
            logger.info("Copy file: '{}' -> '{}'", path_from, path_to)


def update_www():
    if path_define.www_fonts_dir.exists():
        shutil.rmtree(path_define.www_fonts_dir)

    for file_dir, _, file_names in path_define.outputs_dir.walk():
        for file_name in file_names:
            if re.match(r'.*\.woff2', file_name) is None:
                continue
            path_from = file_dir.joinpath(file_name)
            path_to = path_define.www_fonts_dir.joinpath(path_from.relative_to(path_define.outputs_dir))
            path_to.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path_from, path_to)
            logger.info("Copy file: '{}' -> '{}'", path_from, path_to)
