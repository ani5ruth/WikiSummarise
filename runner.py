from scrapper import get_article
from summarizer import Summarizer


if __name__ == '__main__':
    while True:
        keyword = input("\n\nEnter keyword of wikipedia article to summarize (eg. Covid-19) or type exit to quit: ")
        
        if keyword == "exit":
            exit(1)
            
        article = get_article(keyword)
        if article == None:
            print("\n\nCould not find article matching keyword - " + keyword)
            continue

        print("\n\nOriginal Artcile : "  + article['original'])
        print("\n\nSummarised Article : \n" + Summarizer(article['text']).get_article_summary())
