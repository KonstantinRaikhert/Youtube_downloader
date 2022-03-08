import pafy
import os
from dotenv import load_dotenv
import tqdm

load_dotenv()

API_KEY = os.getenv('API_KEY')

pafy.set_api_key(API_KEY)


# class DownLoader:
#     def __init__(self, url):
#         self.video_url = url
#         self.pafy_object = None
#
#     def get_pafy_object(self):
#         self.pafy_object = pafy.new(self.video_url)
# class CallBack:
#     def __init__(self, call_back_id):
#         self.call_back_id = call_back_id
#
#     def __call__(self, total, recvd, ratio, rate, eta):
#         print(total)
#         print("Downloader #{:d}: {:>7.3f} MB {:>6.1f} % {:>10.1f} kBps    ETA: {:>5.1f} s".format(self.call_back_id,
#                                                                                                   recvd / (1024 * 1024),
#                                                                                                   ratio * 100, rate,
#                                                                                                   eta))

previous_received = 0


def update(pbar, current_received):
    global previous_received

    diff = current_received - previous_received
    pbar.update(diff)
    previous_received = current_received


# --- main ---
url = 'https://www.youtube.com/watch?v=0uAxgTkr6pI'
v = pafy.new(url)
s = v.getbest()

video_size = s.get_filesize()
print("Size is", video_size)

if __name__ == '__main__':
    with tqdm.tqdm(desc=v.title, total=video_size, unit_scale=True, unit='B', initial=0) as pbar:
        s.download(quiet=True, callback=lambda _, received, *args: update(pbar, received))
