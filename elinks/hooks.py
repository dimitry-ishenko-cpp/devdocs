from io import StringIO
from lxml import html as lh
from lxml import etree as lt
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

formatter = HtmlFormatter(full=False, noclasses=True, nobackground=True)

def pre_format_html_hook(url, html):
    tree = lh.parse(StringIO(html))

    # add border=1 to <table> elements
    for table in tree.findall(".//table"):
        if not table.get("border"):
            table.set("border", "1")

    # add <br> inside <span class="t-lines"> elements
    for elem in tree.xpath('.//span[@class="t-lines"]'):
        for index in reversed(range(1, len(elem.getchildren()))):
            elem.insert(index, lt.Element("br"))

    # highlight <pre data-language="..."> elements
    for code in tree.findall(".//pre"):
        if lang := code.get("data-language"):
            try:
                if lexer := get_lexer_by_name(lang):
                    repl = lh.fromstring(highlight(code.text_content(), lexer, formatter))
                    code.getparent().replace(code, repl)
            except:
                pass

    return lh.tostring(tree).decode("utf8")
