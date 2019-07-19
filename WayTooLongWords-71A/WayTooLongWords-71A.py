def too_long():
    number = int(input())
    str_list = []
    for _ in range(0, number):
        str_list.append(input())
    for item in str_list:
        length = len(item)
        if length > 10:
            print("{}{}{}".format(item[0], length-2, item[length-1]))
        else:
            print(item)

if __name__ == "__main__":
    too_long()
