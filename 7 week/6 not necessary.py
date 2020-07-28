# Телефонные номера в адресной книге мобильного телефона имеют один из следующих форматов:
# +7<код><номер>
# 8<код><номер>
# <номер>
# где <номер> — это семь цифр, а <код> — это три цифры или три цифры в круглых скобках.
# Если код не указан, то считается, что он равен 495. Кроме того, в записи телефонного номера может стоять знак “-”
# между любыми двумя цифрами (см. пример). На данный момент в адресной книге телефона Васи записано всего три
# телефонных номера, и он хочет записать туда еще один. Но он не может понять, не записан ли уже такой номер
# в телефонной книге. Помогите ему! Два телефонных номера совпадают, если у них равны коды и равны номера.
# Например, +7(916)0123456 и 89160123456 — это один и тот же номер.
# В первой строке входных данных записан номер телефона, который Вася хочет добавить в адресную книгу своего телефона.
# В следующих трех строках записаны три номера телефонов, которые уже находятся в адресной книге телефона Васи.
# Гарантируется, что каждая из записей соответствует одному из трех приведенных в условии форматов.

s = input()
fnum = input()
snum = input()
tnum = input()
dictnum = {}
slist = (fnum, snum, tnum)
flist = []
for i in slist:
    i = i.replace('-', '')
    i = i.replace('+', '')
    i = i.replace(')', '')
    i = i.replace('(', '')
    if len(i) == 7:
        i = '495' + i
    elif len(i) == 11:
        i = i[1:]
    flist.append(i)

s = s.replace('-', '')
s = s.replace('+', '')
s = s.replace(')', '')
s = s.replace('(', '')
if len(s) == 7:
    s = '495' + s
elif len(s) == 11:
    s = s[1:]

for i in flist:
    if s == i:
        print('YES')
    else:
        print('NO')