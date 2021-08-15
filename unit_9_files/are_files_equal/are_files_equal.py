def are_files_equal(file_path_1, file_path_2):
    with open(file_path_1, "r") as file1, open(file_path_2, "r") as file2:
        return file1.read() == file2.read()


print(are_files_equal("file1.txt", "file2.txt"))
