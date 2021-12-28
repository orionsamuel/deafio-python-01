import os

from pathlib import Path


def read_file():
    input_file = open('input.txt', 'r')
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
    for i in range(len(servers)):
        if servers[i] < umax:
            new_server = False
            if qtd_users <= umax - servers[i]:
                servers[i] = servers[i] + qtd_users
                return servers
            else:
                qtd_users -= umax - servers[i]
                servers[i] = umax
        else:
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
    for i in range(len(servers)):
        if qtd_users < servers[i]:
            servers[i] = servers[i] - qtd_users
            return servers
        elif qtd_users == servers[i]:
            del servers[i]
            return servers
        else:
            qtd_users -= umax
            del servers[i]
    return servers


def simulate(ttask, umax, new_users):
    servers = []
    tick = 1
    count_users = 0
    servers = add_user(new_users[count_users], umax, servers)
    while len(servers) > 0:
        tick += 1
        count_users += 1


def write_file(line):
    output_file = ('output.tx', 'a')
    output_file.write(line)

def init():
    ttask, umax, new_users = read_file()
    output_file = Path('output.txt')
    if output_file.is_file():
        os.remove(output_file)


if __name__ == '__main__':
    init()
