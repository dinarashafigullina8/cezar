
def replace_word(lang, word, isUpper, localStep):
    language = alph_ru if lang == 'русский' else alph_en
    index = (language.index(word.lower()) + localStep) % len(language)
    newWord = language[index].upper() if isUpper else language[index]
    return newWord


alph_en = 'abcdefghijklmnopqrstuvwxyz'
alph_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
print('Выберите напрвление: шифрование или дешифрование')
napr = input()
print('Выберите язык алфавита: русский или английский')
lang = input()
print('Введите шаг сдвига')
step = int(input())
print('Введите фразу')
sentence = input()

if napr == 'дешифрование':
    step = -step
result = ''

for i in range(len(sentence)):
        if sentence[i].isalpha():
            isUpper = sentence[i] == sentence[i].upper()
            result += replace_word(lang, sentence[i], isUpper, step)
        else:
            result += sentence[i]
print(result)
    
