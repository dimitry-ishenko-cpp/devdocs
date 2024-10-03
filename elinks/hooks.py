from io import StringIO
from lxml import html as lh
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def pre_format_html_hook(url, html):
    tree = lh.parse(StringIO(html))

    for table in tree.findall(".//table"):
        if not table.get("border"):
            table.set("border", "1")

    formatter = HtmlFormatter(full=False, noclasses=True, nobackground=True)

    for code in tree.findall(".//pre"):
        if lang := code.get("data-language"):
            try:
                if lexer := get_lexer_by_name(lang):
                    repl = lh.fromstring(highlight(code.text_content(), lexer, formatter))
                    code.getparent().replace(code, repl)
            except:
                pass

    return lh.tostring(tree).decode("utf8")
