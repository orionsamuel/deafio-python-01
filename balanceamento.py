def read_file():
    input_file = open('input.txt', 'r')
    count = 0
    new_users = []
    for line in input_file:
        if count == 0:
            ttask = int(line)
        elif count == 1:
            umax = int(line)
        else:
            new_users.append(int(line))
        count += 1
    return ttask, umax, new_users

def init():
    ttask, umax, new_users = read_file()
    print(ttask)
    print(umax)
    print(new_users)

if __name__ == '__main__':
    init()
