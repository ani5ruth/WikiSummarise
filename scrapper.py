import bs4
import urllib.request as req
import re
URL = 'https://en.wikipedia.org/wiki/'


def get_article(keyword):
    """Returns wikipedia article matching given keyword (None if no article found)"""

    # scrapping url
    try:
        scrapped_content = req.urlopen(URL + re.sub(r'\s+', '_', keyword))
    except:
        return None

    # parsing html
    article_content = scrapped_content.read()
    article_parsed = bs4.BeautifulSoup(article_content, 'html.parser')

    # find the original url of page 
    header = article_parsed.find('h1').text
    url = URL + re.sub(r'\s+', '_', header)

    # concatinate all paragraphs and remove extra spaces and boxed numbers
    paragraph = article_parsed.find_all('p')
    article_text = "".join([p.text for p in paragraph])
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)

    return {'text' : article_text, 'original' : url}
