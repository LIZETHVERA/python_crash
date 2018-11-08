def make_album (artist_name, album_title,tracks = " "):
    album = {"name" :artist_name, "album": album_title}
    if tracks:
        album ["tracks"] = tracks
    return album 

while True:
    print ("\nEnter an artist")
    print ("Enter an album title")
    print ("enter 'q' at any time to quit")
    print ("\n")
    artist = input ("artist_name: ")
    if artist == "q":
        break
    title = input ("album_title: ")
    if title == "q":
        break
    artist_info = make_album (artist,title)
    print ("\n" + str (artist_info))
