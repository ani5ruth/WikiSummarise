# importing libraries
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter


class Summarizer:
    """Summarises given article using sentence-ranking algorithm"""

    def __init__(self, article):

        self.article = article
        self.construct_stems()
        self.construct_sentences()

    def construct_stems(self):
        '''Construct word stems using porter stemming algorithm'''
        
        stop_words = set(stopwords.words("english"))
        stemmer = PorterStemmer()
        self.stems = list()
        for word in word_tokenize(self.article):
            if word in stop_words or not word.isalpha():
                continue
            self.stems.append(stemmer.stem(word))

    def construct_sentences(self):
        '''Tokenise sentences'''
        self.sentences = sent_tokenize(self.article)

    def compute_word_weight_table(self) -> Counter:
        '''Returns a Counter of stems in article'''
        return Counter(self.stems)

    def compute_sentence_score_table(self) -> dict:
        '''Returns a score table of every sentence in article'''
        
        # for each sentence cumulate the weights of its words
        word_counter = self.compute_word_weight_table()
        score_table = dict()
        for sentence in self.sentences:
            stems_in_sent = list(filter(lambda stem: stem in sentence.lower(), word_counter))
            
            # for every word in sentence that is in frequncy table sum the weights
            for stem in stems_in_sent:
                score_table[sentence] = score_table.get(sentence, 0) + word_counter[stem]
                
            # average out weight to avoid long senteces to get higher preference
            score_table[sentence] = score_table.get(sentence, 0) / len(stems_in_sent)
            
        return score_table
    
    def get_article_summary(self):
        '''Returns summary of article using threshold-limited sentence ranking algorithm'''
           
        score_table = self.compute_sentence_score_table()
        threshold = 1.5 * sum(score_table.values())/len(score_table)
    
        return "".join(list(filter(lambda sentence: score_table.get(sentence, 0) >= threshold, score_table)))

