class Revenue:

    def init(self, x, y):
        self._twitchRev = 0

    def stream1(self):
        self.__youtubeRev = x

    def getYoutubeRev(self):
        return self.__youtubeRev
    
    def stream2(self):
        self._twitchRev = y

streaming = Revenue()

streaming.stream1(20000)

streaming.stream2(30000)

totalRev = streaming.getYoutubeRev() + streaming._twitchRev

print(totalRev)
