class Revenue:

    def init(self, x, y):
        #protected property
        self._twitchRev = 0
        #private property
        self.__youtubeRev = 0
        
    #function that take x and assigns it to "__youtubeRev"
    def stream1(self, x):
        self.__youtubeRev1 = x

    #method to get the value of the "__youtubeRev" private property
    def getYoutubeRev(self):
        return self.__youtubeRev

    #function that takes y and assigns it to "_twitchRev"
    def stream2(self, y):
        self._twitchRev = y

#instantiates a "Revenue" object name "streaming"
streaming = Revenue()
#assigns a value of 20000 to "__youtubeRev"
streaming.stream1(20000)
#assigns a value of 30000 to "__twitchRev"
streaming.stream2(30000)

# add youtuberev and twitch rev properties
totalRev = streaming.getYoutubeRev() + streaming._twitchRev

print(totalRev)
