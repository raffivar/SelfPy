def song_length(formatted_song):
    return float(formatted_song[2].replace(':', '.'))


def my_mp3_playlist(file_path):
    with open(file_path, "r") as file1:
        song_list = file1.read().split('\n')

        formatted_list = []
        for song in song_list:
            formatted_song = song.split(';')
            formatted_list.append(formatted_song)

        longest_song = max(formatted_list, key=song_length)

        artist_dict = {}
        artist_mentioned_most = ("", 0)
        for formatted_song in formatted_list:
            artist_name = formatted_song[1]
            times_mentioned_so_far = artist_dict[artist_name] + 1 if artist_name in artist_dict else 1
            artist_dict[artist_name] = times_mentioned_so_far
            if times_mentioned_so_far > artist_mentioned_most[1]:
                artist_mentioned_most = artist_name, artist_dict[artist_name]

        return longest_song[0], len(formatted_list), artist_mentioned_most[0]


print(my_mp3_playlist("songs.txt"))
