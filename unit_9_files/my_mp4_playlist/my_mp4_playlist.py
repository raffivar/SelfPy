def song_length(formatted_song):
    return float(formatted_song[2].replace(':', '.'))


def my_mp4_playlist(file_path, new_song_title):
    formatted_songs = []
    with open(file_path, "r") as file:
        for song in file:
            formatted_song = song.split(';')
            formatted_songs.append(formatted_song)
    with open(file_path, "w") as file:
        line_to_replace = 4
        if len(formatted_songs) >= line_to_replace:
            formatted_songs[line_to_replace - 1][0] = new_song_title
        for formatted_song in formatted_songs:
            file.write(';'.join(formatted_song))
        for i in range(len(formatted_songs), line_to_replace - 1):
            file.write('\n')
        if len(formatted_songs) < line_to_replace:
            file.write(new_song_title)


my_mp4_playlist("songs.txt", "Python Love Story")
