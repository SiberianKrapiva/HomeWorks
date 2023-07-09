text = input('Введите слово: ')

def pal(text):
    return text == text[::-1]

print(pal(text)) 


