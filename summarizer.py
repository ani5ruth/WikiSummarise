from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter


class Summarizer:
    """Summarises given article using weighted-frequency algorithm"""

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

    def compute_word_weight_table(self):
        '''Returns a Counter of stems in article'''
        return Counter(self.stems)

    def compute_sentence_score_table(self):
        '''Returns a score table of every sentence in article'''
        # for each sentence cumulate the weights of its words
        word_counter = self.compute_word_weight_table()
        score_table = dict()
        for sentence in self.sentences:
            stems_in_sent = list(filter(lambda stem: stem in sentence.lower(), word_counter))
            # accumulate every frequency of stems in sentence
            total_sentence_score = sum(list(map(lambda stem: word_counter[stem], stems_in_sent)))
            # average out weight to avoid long senteces to get higher preference
            score_table[sentence] = total_sentence_score / len(stems_in_sent)

        return score_table

    def get_article_summary(self, threshold_factor):
        '''Returns summary of article using threshold-limited sentence ranking algorithm'''
        score_table = self.compute_sentence_score_table()
        average_sentence_score = sum(score_table.values())/len(score_table)
        threshold = threshold_factor * average_sentence_score
        return "".join(list(filter(lambda sentence: score_table.get(sentence, 0) > threshold, score_table)))


if __name__ == "__main__":
    article = '''Coronavirus disease 2019 (COVID-19) is an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). 
    The disease was first identified in December 2019 in Wuhan, the capital of China's Hubei province, and has since spread globally, resulting in the ongoing 2019–20 coronavirus pandemic.
    Common symptoms include fever, cough and shortness of breath. Other symptoms may include fatigue, muscle pain, diarrhea, sore throat, loss of smell and abdominal pain. 
    The time from exposure to onset of symptoms is typically around five days, but may range from two to 14 days. While the majority of cases result in mild symptoms, some progress to viral pneumonia and multi-organ failure.
    As of 9 April 2020, more than 1.48 million cases have been reported in more than 200 countries and territories, resulting in more than 88,600 deaths. More than 331,000 people have recovered.'''
    print(Summarizer(article).get_article_summary(1))
