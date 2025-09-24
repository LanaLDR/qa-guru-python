import os
import shutil

import pytest
from selene import browser
from zipfile import ZipFile

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'tmp')
RESOURCES_DIR = os.path.join(CURRENT_DIRECTORY, 'resources')
ZIP_FILE_IN_RESOURCES = os.path.join(RESOURCES_DIR, 'test.zip')

@pytest.fixture()
def setup_browser():
    browser.config.window_height = 2560  # задает высоту окна браузера
    browser.config.window_width = 1664  # задает ширину окна браузера
    yield
    browser.quit()

@pytest.fixture()
def zip_packing_files():
    os.makedirs(RESOURCES_DIR, exist_ok=True)
    with ZipFile(ZIP_FILE_IN_RESOURCES, mode='w') as zf:
        for file in os.listdir(TMP_DIR):
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, arcname=file)
    yield
    shutil.rmtree(RESOURCES_DIR)