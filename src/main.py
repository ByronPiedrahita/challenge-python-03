# Resolve the problem!!

import re

def run():
    hidden_text=[]
    with open('encoded.txt', 'r', encoding='utf8') as f:
        hidden = re.findall(r"[a-z]", f.read())
        print(hidden)


if __name__ == '__main__':
    run()