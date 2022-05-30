class Revenue:

    def init(self, x, y):
        self._twitchRev = 0

    def stream1(self):
        self.__youtubeRev = x

    def stream2(self):
        self._twitchRev = y

Youtube = Revenue("2022", 100000)
Twitch = Revenue("2022", 20000)

totalRev = Youtube + Twitch

print(Youtube.youtubeRev1)
print(Twitch._twitchRev)
