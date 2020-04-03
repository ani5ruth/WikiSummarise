# Wikipedia article summariser using sentence ranking algorithm

## Libraries Used:
Python - beautiful soup, urllib, nltk

## Installation:
- Install [Python-3](https://www.python.org/)
- Install [nltk](https://www.nltk.org/)
- Install [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    
## Working:
- Run runner.py file
- Enter keyword of article to summarise (eg. Covid 19)
- Get a breif summary of article and a wikipedia link to original article

## Algorithm Used:
Sentence ranking algorithm - calculates ranking of each sentence in article using word count table, and selects a set of sentences for summarisation that surpass a threshold (can be modified for varying results).

## References
https://blog.floydhub.com/gentle-introduction-to-text-summarization-in-machine-learning/