def sort(file_path):
    res = list()
    with open(file_path, "r") as file:
        for line in file:
            for word in line[:-1].split(' '):
                if word not in res:
                    res.append(word)
    return sorted(res)


def rev(file_path):
    res = str()
    with open(file_path, "r") as file:
        for line in file:
            res += line[-2::-1] + line[-1]
    return res


def last(file_path, n):
    res = str()
    with open(file_path, "r") as file:
        lines = file.readlines()
        last_lines = lines[-n]
        for line in last_lines:
            res += line
    return res


print(sort("file.txt"))
print()
print(rev("file.txt"))
print()
print(last("file.txt", 1))
