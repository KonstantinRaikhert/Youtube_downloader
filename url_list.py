from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from driver import Driver
import pathlib
import time


class YouTubeChannelVideos:
    def __init__(self, channel_url, driver):
        self.channel_url = channel_url
        self.driver = driver

    def _get_url(self):
        self.driver.get(self.channel_url)

    def close_driver(self):
        self.driver.close()

    def urls_video_list(self):
        self._get_url()

        video_urls = []

        next_height = self.driver.execute_script(
            "return document.documentElement.scrollHeight"
        )
        previous_height = -1

        while previous_height < next_height:
            previous_height = next_height
            self.driver.execute_script(f'window.scrollTo(0,{next_height + 10000})')
            time.sleep(1)
            next_height = self.driver.execute_script("return document.documentElement.scrollHeight")

        video_elements = self.driver.find_elements(by=By.ID, value='thumbnail')

        for video_element in video_elements:
            video_urls.append(video_element.get_attribute('href'))

        video_urls.remove(None)

        return video_urls

    def urls_save_in_file(self):
        file_in_path = pathlib.Path('urls.txt').exists()

        if not file_in_path:
            urls = self.urls_video_list()
            with open('urls.txt', 'xt') as file:
                for url in urls:
                    file.write(url + '\n')
        else:
            print('File already exists')


if __name__ == '__main__':
    channel_url = input("Введите ссылку на канал:\n")
    driver = Driver(web_driver=Chrome, driver_manager=ChromeDriverManager).get_driver()
    channel = YouTubeChannelVideos(channel_url=channel_url, driver=driver)
    channel.urls_save_in_file()
    channel.close_driver()
