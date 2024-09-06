class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = file_name
    def get_all_words (self):
        all_words={}
        str_punctuation = [",", ".", "=", "!", "?", ";", ":", " - "]
        for file_name in self.file_names:
            with open(file_name, "r", encoding="utf-8") as file:
                words = []
                for line in file:
                    line=line.lower()
                    for pun in str_punctuation:
                            line = line.replace(pun, " ")
                    words.extend(line.split())
        all_words[self.file_names] = words
        return all_words
    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
                if word.lower() in value:
                    places[key] = value.index(word.lower()) + 1
        return places
    def count(self, word):
        count = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            count[value] = words_count
        return  count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
