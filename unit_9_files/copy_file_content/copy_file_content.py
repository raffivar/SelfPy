def copy_file_content(file_path_1, file_path_2):
    with open(file_path_1, "r") as file1:
        with open(file_path_2, "w") as file2:
            file2.write(file1.read())
    print('copied the contents of [{}] into [{}]'.format(file_path_1, file_path_2))


copy_file_content("file1.txt", "file2.txt")
