first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda first, second:first == second , first, second)))




def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open (file_name, "w", encoding="utf-8") as file:
            for line in data_set:
                file.write(str(line))
                file.write("\n")
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

from random import choice
class MysticBall:
    def __init__(self, *words):
        self.word = words

    def __call__(self, *args, **kwargs):
        word = choice(self.word)
        return word


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())