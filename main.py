# Program capitalizes first letter in the text, adds spaces and capitalizes letters after dots.
txt = input("Введите текст: ")
# Capitalizing first letter in text.
txt = txt[0].upper() + txt[1:]

n = txt.find('.')
count = 1
# Finding dots and adding spaces and capital letters after them.
while n > 0:
    if txt[n+1] == " ":
        txt = txt[:n] + '.' + ' ' + txt[n + 2].upper() + txt[n + 3:]
    else:
        txt = txt[:n] + '.' + ' ' + txt[n + 1].upper() + txt[n + 2:]
    count += 1
    n = txt.find('.', n + 2, len(txt) - count)

n = txt.find('!')
count = 1
# Then same for exclamation marks.
while n > 0:
    if txt[n+1] == " ":
        txt = txt[:n] + '!' + ' ' + txt[n + 2].upper() + txt[n + 3:]
    else:
        txt = txt[:n] + '!' + ' ' + txt[n + 1].upper() + txt[n + 2:]
    count += 1
    n = txt.find('!', n + 2, len(txt) - count)

n = txt.find('?')
count = 1
# And question marks.
while n > 0:
    if txt[n+1] == " ":
        txt = txt[:n] + '?' + ' ' + txt[n + 2].upper() + txt[n + 3:]
    else:
        txt = txt[:n] + '?' + ' ' + txt[n + 1].upper() + txt[n + 2:]
    count += 1
    n = txt.find('?', n + 2, len(txt) - count)

print(txt)
