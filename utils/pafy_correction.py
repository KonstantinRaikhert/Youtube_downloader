import time
import youtube_dl
from pafy import g
from pafy.backend_youtube_dl import YtdlPafy


class YtdlPathyCorrection(YtdlPafy):
    def _fetch_basic(self):
        """ Fetch basic data and streams. """
        if self._have_basic:
            return

        with youtube_dl.YoutubeDL(self._ydl_opts) as ydl:
            try:
                self._ydl_info = ydl.extract_info(self.videoid, download=False)
            # Turn into an IOError since that is what pafy previously raised
            except youtube_dl.utils.DownloadError as e:
                raise IOError(str(e).replace('YouTube said', 'Youtube says'))

        if self.callback:
            self.callback("Fetched video info")

        self._title = self._ydl_info['title']
        self._author = self._ydl_info['uploader']
        self._rating = self._ydl_info['average_rating']
        self._length = self._ydl_info['duration']
        self._viewcount = self._ydl_info['view_count']
        self._likes = self._ydl_info['like_count'] if self._ydl_info['like_count'] else None
        self._username = self._ydl_info['uploader_id']
        self._category = self._ydl_info['categories'][0] if self._ydl_info['categories'] else ''
        self._bestthumb = self._ydl_info['thumbnails'][0]['url']
        self._bigthumb = g.urls['bigthumb'] % self.videoid
        self._bigthumbhd = g.urls['bigthumbhd'] % self.videoid
        self.expiry = time.time() + g.lifespan

        self._have_basic = True


def new(url, basic=True, gdata=False, size=False, callback=None, ydl_opts=None):
    return YtdlPathyCorrection(url, basic, gdata, size, callback, ydl_opts=ydl_opts)
