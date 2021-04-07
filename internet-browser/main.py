import sys, os
from browser import Browser


def parse_args():
    """
    Parse argument from terminal. The argument corresponds to the browser's cache folder.
    example: 'python main.py temp-folder'
    :return: a Browser object
    """
    # create directory from terminal input
    script, path = sys.argv
    try:
        os.mkdir(path)
    except Exception:
        pass  # directory already exists
    return Browser(path)


if __name__ == "__main__":
    browser = parse_args()
    browser.run()
