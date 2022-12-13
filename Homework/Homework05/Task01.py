#1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
#Пример:
#Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
#Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок

text_to_edit_in = 'Пугать ты галок пугай'

def del_some_words(text_to_edit):
    text_to_edit = list(filter(lambda x: 'пуг' not in x, text_to_edit.split()))
    return " ".join(text_to_edit)

print('До:', text_to_edit_in)
text_to_edit = del_some_words(text_to_edit_in)
print('После:', text_to_edit)