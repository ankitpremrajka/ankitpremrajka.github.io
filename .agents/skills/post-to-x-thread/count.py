"""Count X (Twitter) characters for each post in a thread file.

Posts are separated by a line containing only '---'. X counts every URL
as 23 characters and most emoji as 2. Flags any post over 280.

Usage: python3 -I count.py thread.txt
"""
import re
import sys

LIMIT = 280
URL = re.compile(r'https?://\S+')


def x_length(text):
    n = len(URL.sub('x' * 23, text))
    n += sum(1 for ch in text if ord(ch) >= 0x1F000)  # emoji take two slots
    return n


def main(path):
    posts = [p.strip() for p in re.split(r'(?m)^---\s*$', open(path, encoding='utf-8').read())]
    posts = [p for p in posts if p]
    over = 0
    for i, post in enumerate(posts, 1):
        n = x_length(post)
        flag = '  <-- OVER' if n > LIMIT else ''
        over += n > LIMIT
        print(f'{i}/ {n}{flag}')
    print(f'{len(posts)} posts, {over} over the {LIMIT} limit')
    return 1 if over else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
