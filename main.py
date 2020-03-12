from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.styles import get_all_styles
from pygments.lexers import (
    get_lexer_by_name,
    get_lexer_for_filename
)
from jinja2 import Environment, PackageLoader

import os


class Snippet(object):

    def __init__(self, style=None, code=None, language=None, filename=None):
        self.style = style
        self.code = code
        self.language = language
        self.filename = filename

    def gen_html(self):

        if self.language:
            lexer = get_lexer_by_name(self.language)
        elif self.filename:
            lexer = get_lexer_for_filename(self.filename)
        formatter = HtmlFormatter(cssclass=self.style)

        return highlight(self.code, lexer, formatter)


def main():

    env = Environment(
        loader=PackageLoader('app', 'templates'),
    )

    index_page = env.get_template('index.html')

    # Generate home page html and styles
    styles = sorted(list(get_all_styles()))

    with open("app/lang/python.py", "r") as i:
        index_code = i.read()

    snippets = []

    #  Generate index content
    for style in styles:
        snippet = Snippet(style=style, code=index_code, language="python")
        snippets.append(snippet)

    index_html = index_page.render(snippets=snippets)

    # Write to index.html
    with open("docs/index.html", "w") as ifile:
        ifile.write(index_html)

    # Get all langs
    langs = os.listdir("app/lang")

    for style in styles:
        language_styles = []
        for lang in sorted(langs):
            with open(f"app/lang/{lang}", "r") as c:
                code = c.read()
            s = Snippet(style=style, code=code, filename=lang, language=lang.split(".")[0])
            language_styles.append(s)

        style_html = env.get_template("style.html").render(langs=language_styles, style=style)
        with open(f"docs/{style}.html", "w") as stylefile:
            stylefile.write(style_html)


if __name__ == "__main__":
    main()
