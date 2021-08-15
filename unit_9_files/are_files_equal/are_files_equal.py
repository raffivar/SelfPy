def are_files_equal(file1, file2):
    with open(file1, "r") as file1, open(file2, "r") as file2:
        return file1.read() == file2.read()


print(are_files_equal("file1.txt", "file2.txt"))
