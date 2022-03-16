import pafy
import os
from dotenv import load_dotenv
import tqdm

load_dotenv()

API_KEY = os.getenv('API_KEY')

pafy.set_api_key(API_KEY)

PREVIOUS_RECEIVED = 0


class DownLoader:

    def __init__(self, video_url):
        self.video_url = video_url
        self.previous_received = 0

    def _get_pafy_object(self):
        return pafy.new(self.video_url)

    def get_best(self):
        video_file = self._get_pafy_object().getbest()
        return video_file

    @staticmethod
    def update(progressbar, current_received):
        global PREVIOUS_RECEIVED
        diff = current_received - PREVIOUS_RECEIVED
        progressbar.update(diff)
        PREVIOUS_RECEIVED = current_received

    @property
    def video_size(self):
        self.get_best().get_filesize()
        return

    def downloader(self, filepath):
        with tqdm.tqdm(
                desc=self.get_best().title, total=self.video_size, unit_scale=True, unit='B', initial=0
        ) as progressbar:
            self.get_best().download(quiet=True, filepath=filepath, callback=lambda _, received, *args: self.update(progressbar, received))


if __name__ == '__main__':
    a = DownLoader('https://youtube.com/watch?v=dDZBs4adKNc')._get_pafy_object()
    print(a.callback)
