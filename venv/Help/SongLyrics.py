import lyricsgenius
# genius = lyricsgenius.Genius(token)
genius = lyricsgenius.Genius()
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
