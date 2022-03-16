from pytube import Channel, YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError
from colorama import Fore, Style
import os
import json


INVALID_URLS_FILE_PATH = 'invalid_urls.txt'
JSON_DATA_URLS_PATH = 'temp_data/data.json'


class YoutubeChannelUrls:
    def __init__(self, channel_url):
        self.channel_url = channel_url
        self.video_urls = []
        self.video_urls_with_title = []

    def get_video_urls_from_channel(self):
        try:
            self.video_urls = Channel(self.channel_url)
            return self.video_urls
        except RegexMatchError:
            print(Fore.YELLOW + "Ссылка на канал неправильная! Введите правильную ссылку!")

    def urls_to_json(self):
        if not self.video_urls_with_title:
            self.video_title()
        if not os.path.exists(JSON_DATA_URLS_PATH):
            with open(JSON_DATA_URLS_PATH, "a+") as json_file:
                json_object = json.dumps(self.video_urls_with_title, indent=1, ensure_ascii=False)
                json_file.write(json_object)
        else:
            print(JSON_DATA_URLS_PATH + ' уже существует в каталоге.')

    @property
    def video_urls_list(self):
        return self.get_video_urls_from_channel()

    @property
    def video_titles_list(self):
        return self.video_title()

    @staticmethod
    def save_invalid_urls(video_url):
        with open(INVALID_URLS_FILE_PATH, "a+") as file:
            file.write(video_url + '\n')

    def video_title(self):
        video_id = 0
        for video_url in self.video_urls_list.videos:
            try:
                video_id += 1
                video_item_dict = {
                    'id': video_id,
                    'title': video_url.title,
                    'url': video_url.watch_url,
                }
                self.video_urls_with_title.append(video_item_dict)
            except VideoUnavailable as err:
                self.save_invalid_urls(video_url.watch_url)
                print(Fore.YELLOW + f"Видео по ссылке {video_url.watch_url} недоступно. \n Причина {err}")
                print(Style.RESET_ALL)
        return self.video_urls_with_title


if __name__ == "__main__":
    url = input("Введите ссылку на Youtube канал" + "\n")
    # print(YoutubeChannelUrls(url).video_titles_list)
    YoutubeChannelUrls(url).urls_to_json()
