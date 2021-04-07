import requests, colorama
from bs4 import BeautifulSoup as bsoup


# initialize colorama for windows (then concatenate Fore.COLOR before a string)
colorama.init(autoreset=True)

class Browser:
    """
    Simple terminal-based web browser.
    It only works with simple urls (website level)

    :cvar tag_list: a list of html tags available to be parsed
    :param cache_folder: a folder to store cached html content. It will be created in current directory, if not exists.
    :ivar cache_folder: see param cache_folder
    :ivar current_content: html currently available to be displayed by the browser
    :ivar bookmarks: a dictionary of saved webpages in the format short_url:url
    :ivar active: True when browser is running
    """

    tag_list = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title']

    def __init__(self, cache_folder):
        self.cache_folder = cache_folder
        self.current_content = None
        self.bookmarks = {}
        self.history = []
        self.active = True
    
    def __str__(self):
        return 'Error: Incorrect URL\n' if self.current_content is None else self.current_content
    
    def close(self):
        self.active = False
        print('Bye!')
    
    def menu(self):
        """
        Receive user input (url or command)
        :return: None if input is a command, else the url
        """
        print('Options:')
        print('\t* type a URL')
        print("\t* type 'exit' to quit")
        print("\t* type 'back' to go to previous URL")
        user_input = input()
        if user_input == 'exit':
            self.close()
        elif user_input == 'back':
            url = self.history_back()
            if url is not None:
                return url
            else:
                print('No browser history')
        else:
            url = user_input
            if self.is_valid(url):
                return url
            else:
                print('Error: Incorrect URL\n')
        return None
    
    def history_back(self):
        """
        One step back in browser history.
        :return: the previously viewed url
        """
        if len(self.history):
            self.history.pop()
        if len(self.history):
            return self.history.pop()
        return None
    
    @staticmethod
    def is_valid(url):
        """Check if user inputs a valid URL containing at least one dot."""
        if '.' not in url:
            return False
        return True
    
    @staticmethod
    def url_convert(url):
        """
        Add https:// in the beginning of a url.
        :return: a url starting with "https://"
        """
        if url.startswith('http'):
            return url
        return 'https://' + url

    @staticmethod
    def url_shortener(url):
        """
        :return: the last part of the url (domain + top-level domain)
        """
        if '//' in url:
            url = url.split('//')[1]
        url_parts = url.split('.')
        shortened_url = f'{url_parts[-2]}.{url_parts[-1]}'
        return shortened_url
    
    @staticmethod
    def parse_html(html):
        """
        Convert raw html text to plain text without html tags.
        :param html: raw html string
        :return: parsed html content
        """
        text = bsoup(html, 'html.parser')
        text = text.find_all(Browser.tag_list)
        result = ''
        for line in text:
            if '<a ' in str(line):
                result += colorama.Fore.BLUE + line.get_text() + '\n'
            else:
                result += colorama.Style.RESET_ALL + line.get_text() + '\n'
        return result
        
    def cache_tab(self, url, content):
        """Cache raw html content in a file named after shortened url."""
        shortened_url = self.url_shortener(url)
        self.bookmarks[self.url_shortener(url)] = url
        self.history.append(shortened_url)
        with open(f'{self.cache_folder}/{shortened_url}', 'w', encoding='utf-8') as f:
            f.write(content)
    
    def open_tab_from_cache(self, shortened_url):
        """
        Set cached raw html content, based on shortened_url.
        :param shortened_url: a shortened url that is stored in bookmarks and in cache.
        """
        with open(f'{self.cache_folder}/{shortened_url}', 'r', encoding='utf-8') as f:
            self.current_content = f.read()
        self.history.append(shortened_url)
    
    def read_url(self, url):
        """Read given url and set content to browser. Also cache content"""
        url = self.url_convert(url)  # adds https://
        try:
            r = requests.get(url)  # server request
            url_content = r.text  # get raw html text
            parsed_html = self.parse_html(url_content)  # parse raw html text, remove tags
            self.cache_tab(url, parsed_html)
            self.current_content = parsed_html
        except Exception:
            self.current_content = None
    
    def run(self):
        """Run this function to start the browser"""
        self.active = True
        while self.active:
            url = self.menu()
            if url is None:
                continue
            if url in self.bookmarks:
                self.open_tab_from_cache(url)  # get parsed html text from cache
            else:
                self.read_url(url)
            print(self)
            print(self.history)
