def song_length(formatted_song):
    return float(formatted_song[2].replace(':', '.'))


def artist(formatted_song):
    return formatted_song[1]


def my_mp3_playlist(file_path):
    with open(file_path, "r") as file1:
        song_list = file1.read().split('\n')
        formatted_list = []
        for song in song_list:
            formatted_song = song.split(';')
            formatted_list.append(formatted_song)
        longest_song = max(formatted_list, key=song_length)
        # performer_max_times = max(formatted_list, key=artist)
        artist_dict = {}
        for formatted_song in formatted_list:
            artist_name = formatted_song[1]
            if artist_name in artist_dict:
                artist_dict[artist_name] += 1
            else:
                artist_dict[artist_name] = 1
        artist_mentioned_most = ("", 0)
        for key, value in artist_dict.items():
            if value > artist_mentioned_most[1]:
                artist_mentioned_most = key, value

        return longest_song[0], len(formatted_list), artist_mentioned_most[0]


print(my_mp3_playlist("songs.txt"))
