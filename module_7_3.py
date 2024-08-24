class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                line = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(j, '')
            all_words[i] = line.split()
        return all_words

    def find(self, word):
        places = {}
        for values, key in self.get_all_words().items():
            if word.lower() in key:
                places[values] = key.index(word.lower()) + 1
        return places

    def count(self, word):
        coun = {}
        for values, key in self.get_all_words().items():
            number = key.count(word.lower())
            coun[values] = number
        return coun


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('captain'))  # 3 слово по счёту
print(finder2.count('captain'))  # 4 слова teXT в тексте всего
