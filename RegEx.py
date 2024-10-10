from pprint import pprint
import csv
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

#создаем список с разделениями по ФИО
list1 = []
for i in contacts_list:
    list1.append(" ".join(i[:3]).split())

#pprint(list1)

#вытаскиваем телефоны
list2 = []
for i in contacts_list:
    list2.append(i[5])
c=f'{list2}'
#print(c)

#приведение номеров в требуемый вид
list3 = []
for i in list2:
    pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    sub = r'+7(\2)\3-\4-\5\7\8\9'
    result = re.sub(pattern, sub, i)
    list3.append(result)

#print(list3)

#поиск дублей по имени и фамилии
list4 = []
for i in list1:
    a = f'{i[0]}{i[1]}'
    list4.append(a)
#print(list4)
        
#наполняем список ФИО остальными полями
l = len(contacts_list)
k = 0
listfin = []
for k in range(l):
    a = contacts_list[k][3]
    b = contacts_list[k][4]
    c = contacts_list[k][6]
    d = list3[k]
    e = list1[k][0]
    f = list1[k][1]
    if len(list1[k])>2:
        g = list1[k][2]
    else:
        g = ''    
    listfin.append([e, f, g, a, b, d, c])
    #print(listfin[k])
    k += 1
#pprint(listfin)

#создаем новый словарь без дублей, ключь Фамилия и имя, остальное - значение
dict_fin = {}
listfin_ = []
for i in range(len(listfin)):
    #print(f'выбираем запись {i}')
    a = listfin[i]
    b = " ".join(a[:2])
    #print(b)
    #print(a)
    if b not in dict_fin.keys(): 
        dict_fin.setdefault(b,a)
        listfin_ = a
        #print(f'добавлена новая запись {b}')
    else:
        #print(f'обновление {b}')
        for x in dict_fin.values():
            if x[4] =='':
                x[4] = a[4]
            else:
                pass
            if x[6] == '':
                x[6] = a[6]
            else:
                pass
        listfin_ = dict_fin.get(b)        
        #print(f'обновление до {dict_fin.get(b)}')
    
#pprint(dict_fin)
listfin_ = list(dict_fin.values())
#pprint(listfin_)        
    
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(listfin_)