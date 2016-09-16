class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
rabbit=["The moon is shining o'er the field" ,
            "A little breeze is blowing ",
            "The radish leaves are crisp and green" ,
            "The lettuces are growing."]
rabbit_song=Song(rabbit)
rabbit_song.sing_me_a_song()
