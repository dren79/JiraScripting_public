from json2html import *


def json_to_html_page(input_):
    html_start = '''<!DOCTYPE html><html><head><title>Json 2 HTML</title></head><body>'''
    html_end = '''</body></html>'''
    table = json2html.convert(json=input_)
    complete_html_page = html_start + table + html_end
    return complete_html_page


if __name__ == "__main__":
    json_input = {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    }
    html_page = json_to_html_page(json_input)
    file = open('json2html.html', 'w')
    file.write(html_page)
    file.close()
