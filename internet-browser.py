import sys
import os
import requests
import colorama
from bs4 import BeautifulSoup as bsoup


def parser(html):
    """takes raw html text, returns plain text without html tags"""
    text = bsoup(html, 'html.parser')
    tag_list = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title']
    text = text.find_all(tag_list)
    result = ''
    for line in text:
        if '<a ' in str(line):
            result += colorama.Fore.BLUE + line.get_text() + '\n'
        else:
            result += colorama.Style.RESET_ALL + line.get_text() + '\n'
    return result


def is_valid(url):
    """checks if user inputs a valid URL containing at least one dot"""
    if '.' not in url:
        return False
    return True


def url_convert(url):
    """adds https:// in the beginning"""
    if url.startswith('http'):
        return url
    return 'https://' + url


def tabs(url, content, directory):
    """caches raw url content in a file named after url"""
    shortened_url = url.rsplit('.', 1)[0]
    with open(f'{directory}/{shortened_url}', 'w', encoding='utf-8') as f:
        f.write(content)
    return shortened_url


def open_tabs(shortened_url, directory):
    """returns cached raw URL contents, based on its shortened version"""
    with open(f'{directory}/{shortened_url}', 'r', encoding='utf-8') as f:
        content = f.read()
    return content


# initialize colorama for windows (then concatenate Fore.COLOR before a string)
colorama.init(autoreset=True)

# create directory from terminal input
script, path = sys.argv
try:
    os.mkdir(path)
except:
    pass

bookmarks = []
undo_history = []

while True:
    url_name = input('Your input here: ')

    if url_name == 'exit':
        # print('Quitting')
        break
    elif url_name == 'back':
        try:
            url_name = undo_history[-1]
        except IndexError:
            print('No browser history')
            continue

    if url_name in bookmarks:
        parsed_html = open_tabs(url_name, path)  # get parsed html text from cache
        print(parsed_html)
        undo_history.append(url_name)  # save short-url to undo-history
    else:
        if is_valid(url_name):
            url_fullname = url_convert(url_name)  # adds https://
            try:
                url_content = requests.get(url_fullname)  # server request
            except Exception:
                url_content = None
                print('Error: Incorrect URL\n')
            if url_content:
                url_content = url_content.text  # get raw html text
                parsed_html = parser(url_content)  # parse raw html text, remove tags
                print(parsed_html)
                bookmarks.append(tabs(url_name, parsed_html, path))  # save short-url to bookmarks
                undo_history.append(url_name)  # save short-url to undo-history
        else:
            print('Error: Incorrect URL\n')
