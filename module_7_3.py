class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            if file_name == file_name: 
                with open(file_name, 'r', encoding='utf-8') as file:  # Читаем все строки из файла
                    content = file.read().lower()  # Приводим к нижнему регистру
                    content = content.translate([',', '.', '=', '!', '?', ';', ':', ' - '])  # Убираем пунктуацию
                    words = content.split()
                    all_words[file_name] = words  # Добавляем в словарь
            else:
                print(f"Фаил '{file_name}' не найдено.")  # Если нет фаила
                all_words[file_name] = []  # Если файл не найден, добавляем пустой список
        return all_words

    def find(self, word):
        word_positions = {}
        word = word.lower()
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for name, words in all_words.items():
            if word in words:
                word_positions[name] = words.index(word) + 1  # Сохраняем позицию первого искомого слова
            else:
                word_positions[name] = -1

        return word_positions

    def count(self, word):
        word_counts = {}
        word = word.lower()
        all_words = self.get_all_words()

        for name, words in all_words.items():
            word_counts[name] = words.count(word)  # Считаем количество слов

        return word_counts

if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего


