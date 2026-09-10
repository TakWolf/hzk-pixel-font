from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).parent.joinpath('..', '..').resolve()

ASSETS_DIR = PROJECT_ROOT_DIR.joinpath('assets')
GLYPHS_DIR = ASSETS_DIR.joinpath('glyphs')
FONTS_DIR = ASSETS_DIR.joinpath('fonts')

BUILD_DIR = PROJECT_ROOT_DIR.joinpath('build')
DUMP_DIR = BUILD_DIR.joinpath('dump')
OUTPUTS_DIR = BUILD_DIR.joinpath('outputs')
RELEASES_DIR = BUILD_DIR.joinpath('releases')

DOCS_DIR = PROJECT_ROOT_DIR.joinpath('docs')

WWW_DIR = PROJECT_ROOT_DIR.joinpath('www')
WWW_FONTS_DIR = WWW_DIR.joinpath('fonts')
