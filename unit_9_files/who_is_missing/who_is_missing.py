def copy_file_content(file_path_1, file_path_2):
    with open(file_path_1, "r") as file1:
        num_list = file1.read().split(',')
        num_list.sort()
        missing = 1
        for num in num_list:
            if missing == int(num):
                missing += 1
            else:
                break
        with open(file_path_2, "w") as file2:
            file2.write(str(missing))
    print('found the missing number from [{}] + wrote it into [{}]'.format(file_path_1, file_path_2))


copy_file_content("findMe.txt", "found.txt")
