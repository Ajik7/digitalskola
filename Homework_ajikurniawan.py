from mrjob.job import MRJob
from mrjob.step import MRStep
import re

## 2 file in one folder
##Python File Name : Homework_ajikurniawan.py
##Script Name : TheAbyssScript.txt
##run file on cmd : python Homework_ajikurniawan.py TheAbyssScript.txt

WORD_RE = re.compile(r"[\w']+")


class TheAbyss(MRJob):

    def mapper_get_words(self, _, line):
        # yield each word in the line
        for word in WORD_RE.findall(line):
            self.increment_counter('group','lines',1)
            yield (word.upper(), 1)

    def combiner_count_words(self, word, counts):
        # sum the words we've seen so far
        self.increment_counter('group','combiners',1)
        yield (word, sum(counts))

    def reducer_count_words(self, word, counts):
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        self.increment_counter('group','reducers',1)
        yield None, (sum(counts), word)

    def reducer_find_max_word(self, _, word_count_pairs):
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        self.increment_counter('group','reducers_2',1)
        yield max(word_count_pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)
        ]


if __name__ == '__main__':
    TheAbyss.run()
    