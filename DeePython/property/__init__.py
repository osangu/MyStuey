class RapRecord:

    def __init__(self, music: str, artist: str):
        self.__music = music
        self.__artist = artist

    @property
    def record(self):
        return {self.__music: self.__artist}

    @record.setter
    def record(self, record: dict):
        self.__music = record['music']
        self.__artist = record['artist']


if __name__ == '__main__':
    ep = RapRecord("History Is Made At Night", "Siman & Huck")

    print(ep.record)

    ep.record = {
        "music": "Last One Standing",
        "artist": "Polo G & Eminem 7...else"
    }

    print(ep.record)
