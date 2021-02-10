#!/usr/bin/python
import sys
from flask import Flask

src = Flask(__name__)


@src.route("/")
def hello():
    class Main:
        first_header = sys.argv[1]

    HTML_File = open('/src/web.html', 'r')
    s = HTML_File.read().format(p=Main())
    return s


if __name__ == "__main__":
    src.run(host="0.0.0.0", port=int("80"), debug=True)

