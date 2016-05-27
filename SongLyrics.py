class Song(object):

    def __init__(self, lyrics, artist, title):
        self.lyrics = lyrics
        self.artist = artist
        self.title = title

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "These lyrics are copywrighted",
                   "So I'll stop here"],#add the name, add the title)

hotline_bling = Song(["You used to call me on my",
                      "You used to, you used to",
                      "Yeah",])
# This is your daily reminder that Drake is Canadian
Andy_Black = Song(['We fill our lives with empty memories '
                   'Weve had enough, '
                   'weve had enough We risked it all, '
                   'didnt get anything Im giving up, Im giving up'])

happy_bday.sing_me_a_song()
hotline_bling.sing_me_a_song()
Andy_Black.sing_me_a_song()
