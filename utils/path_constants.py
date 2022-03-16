import os

ROOT_DIRECTORY = os.getenv('ROOT_DIRECTORY', default='/home/konstantin/Dev/Education/Youtube_downloader')
DOWNLOAD_DIRECTORY = os.getenv('DOWNLOAD_DIRECTORY', default=(ROOT_DIRECTORY + '/download'))
