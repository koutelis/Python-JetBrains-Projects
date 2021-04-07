"""
TASK:

The server is becoming smarter along with your hacking program. Now the admin has implemented a security system by login and password. 
In order to access the site with admin privileges, you need to know the admin's login and password. 
Fortunately, we have a dictionary of different logins and a very interesting vulnerability. You need to improve your program once again to hack the new system.
Also, now the admin has made a complex password that is guaranteed to be absent in the databases since it's randomly generated from several characters.
The server now uses JSON to send messages.
First of all, you should adjust your program so that it can send the combination of login and password in JSON format to the server.
Use the dictionary of typical admin logins. Since you don’t know the login, 
you should try different variants from the dictionary as you did at the previous stage with the passwords.
You will know that the login is correct when you get the ‘wrong password’ result instead of ‘wrong login’.
As for passwords, they’ve become yet harder, so a simple dictionary is no longer enough. 
Fortunately, a vulnerability has been found: the ‘exception’ message pops up when the symbols you tried for the password match the beginning of the correct one.

In case of the wrong password, the response you receive looks like this:
{"result": "Wrong login!"}

If you got the login right but failed to find the password, you get this:
{"result": "Wrong password!"}

If some exception happens, you'll see this result:
{"result": "Exception happened during login"}

When you finally succeed in finding both the login and the password, you'll see the following:
{"result": "Connection success!"}

===========

Your program has successfully hacked the new system! 
However, you've been spotted: the admin noticed your first failed attempts, found the vulnerability and made a patch. 
You should overcome this patch and hack the system again. It’s not easy being a hacker!
The admin has improved the server: the program now catches the exception and sends a simple ‘wrong password’ message to the client,
even when the real password starts with current symbols.
But here's the thing: the admin probably just caught this exception. 
We know that catching an exception takes the computer a long time, so there should be a delay in the server response when this exception takes place. 
You can use it to hack the system: count the time period in which the response comes and find out which starting symbols work out for the password.


run the following from terminal:
python main.py localhost 9090
"""

import hack


if __name__ == "__main__":
    hack.run()
