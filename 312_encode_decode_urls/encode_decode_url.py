from random import choice


class MarsURLEncoder:

    def __init__(self):
        self.charset = '012...89abc...xyzABC...XYZ'
        self.urls = {self.url_hash: self.url}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        new_hash = ''
        for _ in range(6):
            self.new_hash = choice(self.url_hash) + choice(self.charset)
            while 
            return self.new_haw
        pass

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        pass