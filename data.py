

file = "Pink_Floyd_DB.txt"
org = []
albums = []
songs = []

songAndLyrics = [[]]
albumsAndSongs = [[]]
firstLine = ""
songsAndLength = [[]]
b = 1
with open(file,'r') as data:
    org = data.readlines()
    for lines in org:

        if lines[0] == '#':
            lines = lines.split("::")
            albums.append(lines[0][1::])
            albumsAndSongs.append([albums[-1]])
            
            
            

        if lines[0] == '*':
            firstLine = firstLine.replace("\\n", " ")
            firstLine = firstLine.replace("\\'", "'")
            songAndLyrics[-1].append(firstLine)
            firstLine = ""
            lines = lines.split("::")
            songs.append(lines[0][1::])
            songsAndLength.append([lines[0][1::] , lines[2]])
            songAndLyrics.append([songs[-1]])
            albumsAndSongs[-1].append(songs[-1])

            firsLine = lines[-1]
            
            

        else:
            firstLine += str(lines)
        

  
    albumsAndSongs = albumsAndSongs[1::]
    songAndLyrics = songAndLyrics[1::]
    songsAndLength = songsAndLength[1::]

def listOfAlbums():
    return ", ".join(albums)
def listSongsInAlbum(input):
    for i in albumsAndSongs:
        
        if input.lower() == i[0].lower():
            return ", ".join(i[1:-1:1])
        
    return "try again"
def lengthOfASong(input):
    for i in songsAndLength:
        
        if input.lower() == i[0].lower():
            return i[1]
    return "try again"
def wordsOfASong(input):
    for i in songAndLyrics:
        
        if input.lower() == i[0].lower():
            return i[1]
        
    return "try again"
def whatAlbumIsTheSong(input):
    for i in albumsAndSongs:
        for t in i[1:-1:1]:
            if input.lower() == t.lower():
                return i[0]
    return "try again"
def searchSongByName(input):
    answer = ""
    for i in songs:
        if input.lower() in i.lower():
            answer += i + ", "
    answer = answer[0:-2:1] +  "."
    if answer != ".":
        return answer
    else:
        return "No Songs Found!\n"
def songByLyrics(input):
    answer = ""
    for i in songAndLyrics:
        try:
            if input.lower() in i[1].lower():
                answer += i[0]+ ", "
        except:
            pass
    answer = answer[0:-2:1] +  "."
    if answer != ".":
        return answer
    else:
       return "No Songs Found!"

