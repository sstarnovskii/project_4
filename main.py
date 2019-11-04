# Project file.
txt = input()
txt = txt[0].upper() + txt[1:]
n = txt.find('.')
while n > 0:
    if txt[n+1] == " ":
        txt = txt[:n] + '.' + ' ' + txt[n + 2].upper() + txt[n + 3:]
    else:
        txt = txt[:n] + '.' + ' ' + txt[n + 1].upper() + txt[n + 2:]
    n = txt.find('.', n + 2, len(txt) - 1)
print(txt)
