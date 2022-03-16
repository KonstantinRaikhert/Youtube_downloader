import os

import pytube
import json
from colorama import Fore
# from pytube import YouTube
from pytube.cli import on_progress
import ffmpeg
import time

url = 'https://youtube.com/watch?v=dDZBs4adKNc'
# url = 'https://youtube.com/watch?v=VyrsHv2fqeQ'
# url_channel = 'https://www.youtube.com/c/RusjetRu'

JSON_DATA_URLS_PATH = 'temp_data/data.json'
JSON_ERROR_DOWNLOAD = 'error.txt'
DOWNLOAD_VIDEO_PATH = 'download/video'
DOWNLOAD_AUDIO_PATH = 'download/audio'

object = pytube.YouTube(url, on_progress_callback=on_progress)
q = object.streams.filter(only_video=True, adaptive=True).order_by("resolution").last()
s = object.streams.filter(only_audio=True).order_by("abr").last()

print(dir(q))
print(q.url)
print(q)
# s.download(filename="audio.webm")
q.download(filename="video.webm")


# video_stream = ffmpeg.input('audio.webm')
# audio_stream = ffmpeg.input('video.webm')
# ffmpeg.output(audio_stream, video_stream, 'out.mp4').run()

# c = pytube.Channel(url_channel)
# print(len(c))


# class ObjectUrlData:
#     def __init__(self, data_path):
#         self.json_data_path = data_path
#         self.url_data = self._extract_data()
#
#     @property
#     def check_json_file(self):
#         if os.path.exists(self.json_data_path):
#             return True
#         return False
#
#     @property
#     def file_is_empty(self):
#         with open(self.json_data_path, 'r') as data_file:
#             url_data = json.load(data_file)
#             if not url_data:
#                 return True
#             return False
#
#     def _extract_data(self):
#         if not self.check_json_file:
#             raise print(Fore.YELLOW + f"{self.json_data_path} отсутствует в каталоге!")
#         with open(self.json_data_path, 'r') as data_file:
#             url_data = json.load(data_file)
#         return url_data
#
#     @staticmethod
#     def add_streams_object(obj):
#         pytube_object = pytube.YouTube(obj["url"], on_progress_callback=on_progress)
#         obj['video_best'] = pytube_object.streams.filter(adaptive=True).order_by("resolution").last()
#         obj['audio_best'] = pytube_object.streams.filter(only_audio=True).order_by("abr").last()
#         return obj
#
#     def download(self):
#         for item in self.url_data:
#             try:
#                 obj = self.add_streams_object(item)
#                 video = obj['video_best']
#                 audio = obj['audio_best']
#                 video.download(output_path=DOWNLOAD_VIDEO_PATH)
#                 audio.download(output_path=DOWNLOAD_AUDIO_PATH)
#                 print(f"Скачан - {obj['title']} - {obj['id']}")
#                 continue
#             except KeyError:
#                 with open(JSON_ERROR_DOWNLOAD, "a+") as json_file:
#                     del item['video_best']
#                     del item['audio_best']
#                     json_file.write(str(item['id']) + ' ' + item['title'] + item['url'] + ' ' + '\n')
#                 print('Ошибка!!!')
#                 time.sleep(3)
#
# if __name__ == "__main__":
#
#     ObjectUrlData(JSON_DATA_URLS_PATH).download()
#     # print(data)
