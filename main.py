from downloader import DownLoader
from selenium.webdriver import Chrome
from url_list import YouTubeChannelVideos
from webdriver_manager.chrome import ChromeDriverManager
from driver import Driver


def get_urls_file():
    channel_url = input("Введите ссылку на канал:\n")
    driver = Driver(web_driver=Chrome, driver_manager=ChromeDriverManager).get_driver()
    channel = YouTubeChannelVideos(channel_url=channel_url, driver=driver)
    channel.urls_save_in_file()
    channel.close_driver()


def download_videos(filepath):
    with open('urls.txt', 'rt') as file:
        for url in file:
            DownLoader(url).downloader(filepath)
            continue


if __name__ == '__main__':
    get_urls_file()
    download_videos(filepath=input("Введите путь для сохранения файлов:\n"))
