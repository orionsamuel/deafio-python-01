import os

from pathlib import Path


def read_file(file):
    input_file = open(file, 'r')
    count, ttask, umax = 0, 0, 0
    new_users = []
    for line in input_file:
        if count == 0:
            ttask = int(line)
        elif count == 1:
            umax = int(line)
        else:
            new_users.append(int(line))
        count += 1
    input_file.close()
    return ttask, umax, new_users


def add_user(qtd_users, umax, servers):
    new_server = False
    if qtd_users == 0:
        return servers
    if len(servers) == 0:
        if qtd_users <= umax:
            servers.append(qtd_users)
            return servers
        else:
            servers.append(umax)
            qtd_users = qtd_users - umax
            new_server = True
    else:
        for i in range(len(servers)):
            if servers[i] < umax:
                new_server = False
                if qtd_users <= umax - servers[i]:
                    servers[i] = servers[i] + qtd_users
                    return servers
                else:
                    qtd_users -= umax - servers[i]
                    servers[i] = umax
        if qtd_users > 0:
            new_server = True

    if new_server:
        if qtd_users <= umax:
            servers.append(qtd_users)
            return servers
        else:
            while qtd_users > 0:
                if qtd_users >= umax:
                    servers.append(umax)
                    qtd_users -= umax
                else:
                    servers.append(qtd_users)
                    qtd_users = 0
            return servers


def remove_user(qtd_users, umax, servers):
    i = 0
    while len(servers) > 0:
        if qtd_users < servers[i]:
            servers[i] = servers[i] - qtd_users
            return servers
        elif qtd_users == servers[i]:
            del servers[i]
            return servers
        else:
            qtd_users -= servers[i]
            del servers[i]
            i -= 1
        i += 1
    return servers


def simulate(ttask, umax, new_users):
    servers = []
    tick = 1
    user_tick = []
    count_users = 0
    if len(new_users) > 0:
        servers = add_user(new_users[count_users], umax, servers)
        user_tick.append((new_users[count_users], tick))
        write_file(servers)
    while len(servers) > 0:
        tick += 1
        count_users += 1
        for user in user_tick:
            if user[1] + ttask == tick:
                servers = remove_user(user[0], umax, servers)
        if count_users <= len(new_users) - 1:
            servers = add_user(new_users[count_users], umax, servers)
            user_tick.append((new_users[count_users], tick))
        if len(servers) > 0:
            write_file(servers)
        else:
            write_file(0)


def write_file(servers):
    output_file = open('output.txt', 'a')
    if isinstance(servers, list):
        output_file.write(str(servers)[1:-1] + '\n')
        output_file.close()
    else:
        output_file.write(str(servers) + '\n')
        output_file.close()


def init():
    ttask, umax, new_users = read_file('input.txt')
    output_file = Path('output.txt')
    if output_file.is_file():
        os.remove(output_file)
    simulate(ttask, umax, new_users)


if __name__ == '__main__':
    init()
