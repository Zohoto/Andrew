from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Иня призывника", "Фамилия призывника", "Отчество призывника", "Год рождения призывника",
                     "Заболевание призывника"]
num = int(input("Сколько призывников прибыло? "))
for num in range(num):
    num += 1
    men = {}
    men["Имя призывника №%d: " % num] = input("Введите имя призывника №%d: " % num)
    men["Фамилия призывника №%d: " % num] = input("Введите фанилию призывника №%d: " % num)
    men["Отчество призывника №%d: " % num] = input("Введите отчество призывника №%d: " % num)
    men["Год рождения призывника №%d: " % num] = input("Введите год рождения призывника №%d: " % num)
    men["Заболевание призывника №%d: " % num] = input("Введите заболевание призывника №%d: " % num)
    table.add_row([men["Имя призывника №%d: " % num], men["Фамилия призывника №%d: " % num],
                   men["Отчество призывника №%d: " % num], men["Год рождения призывника №%d: " % num],
                   men["Заболевание призывника №%d: " % num]])
print(table)
