from scrapper import get_article
from summarizer import Summarizer


if __name__ == '__main__':
    keyword = input("Enter keyword of wikipedia article to summarize (eg. Covid-19): ")

    article = get_article(keyword)
    if article == None:
        print("Could not find article matching keyword - " + keyword)
        exit(1)

    print("\n\nOriginal Artcile : "  + article['original'])
    print("\n\nSummarised Article : \n" + Summarizer(article['text']).get_article_summary())
