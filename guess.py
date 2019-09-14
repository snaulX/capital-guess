from tkinter import Tk, simpledialog, messagebox, Button, Label
from itertools import cycle
import datetime
import constructor

def cis ():
    countries = cycle(['России', 'Казахстана', 'Украины', 'Республики Беларусь', 'Армении', 'Азейбарджана', 'Узбекистана', 'Молдавии', 'Таджикистана', 'Киргизии'])
    capitals = cycle(['Москва', 'Астана', 'Киев', 'Минск', 'Ереван', 'Баку', 'Ташкент', 'Кишинёв', 'Душанбе', 'Бишкек'])
    points = 0
    for i in range(1, 11):
        c = next(countries)
        s = next(capitals)
        one = simpledialog.askstring('Вопрос №{}'.format(i), 'Введите столицу {}:'.format(c))
        if one == s:
            points = points + 1
            messagebox.showinfo('', 'Правильно!')
        else:
           messagebox. showinfo('', 'Неправильно!')
    messagebox.showinfo('Результат', 'Ваши очки: ' + str(points))
    name = simpledialog.askstring('Сохранение результата', 'Будете ли вы сохранять результат? Если нет, то введите no. Иначе введите имя:')
    if name.lower() != 'no':
        with open('results.txt', 'a', encoding = 'utf-8') as file:
            file.write('\nИгрок: ' + name + '   очки: ' + str(points) + '   уровень сложности/режим: СНГ    дата игры: ' + str(datetime.datetime.now()) + '   ' + v)
def easy ():
    capitals = cycle(['Париж', 'Вашингтон', 'Пекин', 'Токио', 'Лондон', 'Рим', 'Берлин', 'Мадрид', 'Афины', 'Анкара'])
    countries = cycle(['Франции', 'США', 'Китая', 'Японии', 'Великобритании', 'Италии', 'Германии', 'Испании', 'Греции', 'Турции'])
    points = 0
    for i in range(1, 11):
        c = next(countries)
        s = next(capitals)
        one = simpledialog.askstring('Вопрос №{}'.format(i), 'Введите столицу {}:'.format(c))
        if one == s:
            points = points + 1
            messagebox.showinfo('','Правильно!')
        else:
           messagebox. showinfo('','Неправильно!')
    messagebox.showinfo('Результат', 'Ваши очки: ' + str(points))
    name = simpledialog.askstring('Сохранение результата', 'Будете ли вы сохранять результат? Если нет, то введите no. Иначе введите имя:')
    if name.lower() != 'no':
        with open('results.txt', 'a', encoding = 'utf-8') as file:
            file.write('\nИгрок: ' + name + '   очки: ' + str(points) + '   уровень сложности/режим: Лёгкий    дата игры: ' + str(datetime.datetime.now()) + '   ' + v)
def medium ():
    capitals = cycle(['Хельсинки', 'Дели', 'Бангкок', 'Тблиси', 'Стокгольм', 'Сеул', 'Улан-Батор', 'Рига', 'Прага', 'Мехико'])
    countries = cycle(['Финляндии', 'Индии', 'Таиланда', 'Грузии', 'Швеции', 'Южной Кореи', 'Монголии', 'Латвии', 'Чехии', 'Мексики'])
    points = 0
    for i in range(1, 11):
        c = next(countries)
        s = next(capitals)
        one = simpledialog.askstring('Вопрос №{}'.format(i), 'Введите столицу {}:'.format(c))
        if one == s:
            points = points + 1
            messagebox.showinfo('', 'Правильно!')
        else:
           messagebox. showinfo('', 'Неправильно!')
    messagebox.showinfo('Результат', 'Ваши очки: ' + str(points))
    name = simpledialog.askstring('Сохранение результата', 'Будете ли вы сохранять результат? Если нет, то введите no. Иначе введите имя:')
    if name.lower() != 'no':
        with open('results.txt', 'a', encoding = 'utf-8') as file:
            file.write('\nИгрок: ' + name + '   очки: ' + str(points) + '   уровень сложности/режим: Средний    дата игры: ' + str(datetime.datetime.now()) + '   ' + v)
def hard ():
    capitals = cycle(['Бразилиа', 'Канберра', 'Буэнос-Айрес', 'Монтевидео', 'Веллингтон', 'Абу-Даби', 'Лиссабон', 'Оттава', 'Куала-Лумпур', 'Каир'])
    countries = cycle(['Бразилии', 'Австралии', 'Аргентины', 'Уругвая', 'Новой Зеландии', 'ОАЭ', 'Португалии', 'Канады', 'Малайзии', 'Египта'])
    points = 0
    for i in range(1, 11):
        c = next(countries)
        s = next(capitals)
        one = simpledialog.askstring('Вопрос №{}'.format(i), 'Введите столицу {}:'.format(c))
        if one == s:
            points = points + 1
            messagebox.showinfo('', 'Правильно!')
        else:
           messagebox. showinfo('', 'Неправильно!')
    messagebox.showinfo('Результат', 'Ваши очки: ' + str(points))
    name = simpledialog.askstring('Сохранение результата', 'Будете ли вы сохранять результат? Если нет, то введите no. Иначе введите имя:')
    if name.lower() != 'no':
        with open('results.txt', 'a', encoding = 'utf-8') as file:
            file.write('\nИгрок: ' + name + '   очки: ' + str(points) + '   уровень сложности/режим: Сложный    дата игры: ' + str(datetime.datetime.now()) + '   ' + v)
def afric ():
    capitals = cycle(['Яунде', 'Претория', 'Алжир', 'Рабат', 'Тунис', 'Хартум', 'Могадишо', 'Луанда', 'Антананариву', 'Мапуту'])
    countries = cycle(['Камеруна', 'ЮАРа', 'Алжира', 'Марокко', 'Туниса', 'Судана', 'Сомали', 'Анголы', 'Мадагаскара', 'Мозамбика'])
    points = 0
    for i in range(1, 11):
        c = next(countries)
        s = next(capitals)
        one = simpledialog.askstring('Вопрос №{}'.format(i), 'Введите столицу {}:'.format(c))
        if one == s:
            points = points + 1
            messagebox.showinfo('', 'Правильно!')
        else:
           messagebox. showinfo('', 'Неправильно!')
    messagebox.showinfo('Результат', 'Ваши очки: ' + str(points))
    name = simpledialog.askstring('Сохранение результата', 'Будете ли вы сохранять результат? Если нет, то введите no. Иначе введите имя:')
    if name.lower() != 'no':
        with open('results.txt', 'a', encoding = 'utf-8') as file:
            file.write('\nИгрок: ' + name + '   очки: ' + str(points) + '   уровень сложности/режим: Африка    дата игры: ' + str(datetime.datetime.now()) + '   ' + v)
def asia ():
    capitals = cycle(['Джакарта', 'Тегеран', 'Ханой', 'Пномпень', 'Багдад', 'Эр-Рияд', 'Улан-Батор', 'Сеул', 'Дакка', 'Исламбад'])
    countries = cycle(['Индонезии', 'Ирана', 'Вьетнама', 'Камбоджи', 'Ирака', 'Саудовской Аравии', 'Монголии', 'Южной Кореи', 'Бангладеша', 'Пакистана'])
    points = 0
    for i in range(1, 11):
        c = next(countries)
        s = next(capitals)
        one = simpledialog.askstring('Вопрос №{}'.format(i), 'Введите столицу {}:'.format(c))
        if one == s:
            points = points + 1
            messagebox.showinfo('', 'Правильно!')
        else:
           messagebox. showinfo('', 'Неправильно!')
    messagebox.showinfo('Результат', 'Ваши очки: ' + str(points))
    name = simpledialog.askstring('Сохранение результата', 'Будете ли вы сохранять результат? Если нет, то введите no. Иначе введите имя:')
    if name.lower() != 'no':
        with open('results.txt', 'a', encoding = 'utf-8') as file:
            file.write('\nИгрок: ' + name + '   очки: ' + str(points) + '   уровень сложности/режим: Азия    дата игры: ' + str(datetime.datetime.now()) + '   ' + v)
def europe ():
    capitals = cycle(['Рейкъявик', 'Белград', 'Братислава', 'Бухарест', 'Варшава', 'Вильнюс', 'София', 'Амстердам', 'Брюссель', 'Вена'])
    countries = cycle(['Исландии', 'Сербии', 'Словакии', 'Румынии', 'Польши', 'Литвы', 'Болгарии', 'Нидерландов', 'Бельгии', 'Австрии'])
    points = 0
    for i in range(1, 11):
        c = next(countries)
        s = next(capitals)
        one = simpledialog.askstring('Вопрос №{}'.format(i), 'Введите столицу {}:'.format(c))
        if one == s:
            points = points + 1
            messagebox.showinfo('','Правильно!')
        else:
           messagebox. showinfo('','Неправильно!')
    messagebox.showinfo('Результат', 'Ваши очки: ' + str(points))
    name = simpledialog.askstring('Сохранение результата', 'Будете ли вы сохранять результат? Если нет, то введите no. Иначе введите имя:')
    if name.lower() != 'no':
        with open('results.txt', 'a', encoding = 'utf-8') as file:
            file.write('\nИгрок: ' + name + '   очки: ' + str(points) + '   уровень сложности/режим: Европа    дата игры: ' + str(datetime.datetime.now()) + '   ' + v)
def instruction () :
    messagebox.showinfo('Инструкция','Столицы записываются с большой буквы. \nЕсли столица пишется через тире, то писать так: Нью-Йорк.\n*Нью-Йорк не является столицей и был показан только в качестве примера.')
def answer ():
    look_answ = True
    aanswer = Tk()
    aanswer.title('Ответы')
    def answer_cis ():
        messagebox.showinfo('Ответы на тест "СНГ"','Вопрос №1: Москва\nВопрос №2: Астана\nВопрос №3: Киев\nВопрос №4: Минск\nВопрос №5: Ереван\nВопрос №6: Баку\nВопрос №7: Ташкент\nВопрос №8: Кишинёв\nВопрос №9: Душанбе\nВопрос №10: Бишкек')
    def answer_easy():
        messagebox.showinfo('Ответы на тест "Лёгкий"', 'Вопрос №1: Париж\nВопрос №2: Вашингтон\nВопрос №3: Пекин\nВопрос №4: Токио\nВопрос №5: Лондон\nВопрос №6: Рим\nВопрос №7: Берлин\nВопрос №8: Мадрид\nВопрос №9: Афины\nВопрос №10: Анкара')
    def answer_medium():
        messagebox.showinfo('Ответы на тест "Средний"', 'Вопрос №1: Хельсинки\nВопрос №2: Дели\nВопрос №3: Бангкок\nВопрос №4: Тблиси\nВопрос №5: Стокгольм\nВопрос №6: Сеул\nВопрос №7: Улан-Батор\nВопрос №8: Рига\nВопрос №9: Прага\nВопрос №10: Мехико')
    Button(aanswer, command = answer_cis, text = 'Ответы на тест "СНГ"', width = 30, height = 8, bg = colour, activebackground = colour).pack()
    Button(aanswer, command = answer_easy, text = 'Ответы на тест "Лёгкий"', width = 30, height = 8, bg = colour, activebackground = colour).pack()
    Button(aanswer, command = answer_medium, text = 'Ответы на тест "Средний"', width = 30, height = 8, bg = colour, activebackground = colour).pack()
    def answer_hard():
        messagebox.showinfo('Ответы на тест "Сложный"', 'Вопрос №1: Бразилиа\nВопрос №2: Канберра\nВопрос №3: Буэнос-Айрес\nВопрос №4: Монтевидео\nВопрос №5: Веллингтон\nВопрос №6: Абу-Даби\nВопрос №7: Лиссабон\nВопрос №8: Оттава\nВопрос №9: Куала-Лумпур\nВопрос №10: Каир')
    Button(aanswer, command = answer_hard, text = 'Ответы на тест "Сложный"', width = 30, height = 8, bg = colour, activebackground = colour).pack()
    def answer_afric():
        messagebox.showinfo('Ответы на тест "Африка"', 'Вопрос №1: Яунде\nВопрос №2: Претория\nВопрос №3: Алжир\nВопрос №4: Рабат\nВопрос №5: Тунис\nВопрос №6: Хартум\nВопрос №7: Могадишо\nВопрос №8: Луанда\nВопрос №9: Антананариву\nВопрос №10: Мапуту')
    answerafric = Button(aanswer, command = answer_afric, text = 'Ответы на тест "Африка"', width = 30, height = 8, bg = colour, activebackground = colour)
    answerafric.pack()
    def answer_asia():
        messagebox.showinfo('Ответы на тест "Азия"', 'Вопрос №1: Джакарта\nВопрос №2: Тегеран\nВопрос №3: Ханой\nВопрос №4: Пномпень\nВопрос №5: Багдад\nВопрос №6: Эр-Рияд\nВопрос №7: Улан-Батор\nВопрос №8: Сеул\nВопрос №9: Дакка\nВопрос №10: Исламбад')
    Button(aanswer, command = answer_asia, text = 'Ответы на тест "Азия"', width = 30, height = 8, bg = colour, activebackground = colour).pack()
    def answer_europe():
        messagebox.showinfo('Ответы на тест "Европа"', 'Вопрос №1: Рейкъявик\nВопрос №2: Белград\nВопрос №3: Братислава\nВопрос №4: Бухарест\nВопрос №5: Варшава\nВопрос №6: Вильнюс\nВопрос №7: София\nВопрос №8: Амстердам\nВопрос №9: Брюссель\nВопрос №10: Вена')
    Button(aanswer, command = answer_europe, text = 'Ответы на тест "Европа"', width = 30, height = 8, bg = colour, activebackground = colour).pack()
    if look_answ:
        aanswer.mainloop()
        root.withdraw()
    else:
        aanswer.withdraw()
        root.mainloop()
def result ():
    win = Tk()
    win.title('Результаты')
    with open('results.txt', 'r', encoding = 'utf-8') as file:
        resultln = file.readline()
        global results
        results = ''
        while resultln:
            results = str(results + resultln)
            resultln = file.readline()
        Label(win, text = results).pack()
if __name__ == "__main__":
    colour = 'light green'
    v = 'v 1.0.12'
    root = Tk()
    root.title('Викторина по Столицам {}'.format(v))
    root.wm_state('zoomed')
    root.configure(bg = 'green')
    Button(root, command = easy, text = 'Лёгкий', width = 30, height = 6, bg = colour, activebackground = colour).grid(row = 0, column = 0, ipadx = 10, ipady = 6, padx = 10, pady = 10)
    Button(root, command = cis, text = 'СНГ', width = 30, height = 6, bg = colour, activebackground = colour).grid(row = 0, column = 1, ipadx = 10, ipady = 6, padx = 10, pady = 10)
    Button(root, command = medium, text = 'Средний', width = 30, height = 6, bg = colour, activebackground = colour).grid(row = 0, column = 2, ipadx = 10, ipady = 6, padx = 10, pady = 10)
    Button(root, command = hard, text = 'Сложный', width = 30, height = 6, bg = colour, activebackground = colour).grid(row = 0, column = 3, ipadx = 10, ipady = 6, padx = 10, pady = 10)
    Button(root, command = instruction, text = 'Инструкция', width = 30, height = 3, bg = colour, activebackground = colour).grid(row = 2, column = 0, ipadx=10, ipady=6, padx=10, pady=10)
    Button(root, command = afric, text = 'Африка', width = 30, height = 6, bg = colour, activebackground = colour).grid(row = 0, column = 4, ipadx = 10, ipady = 6, padx = 10, pady = 10)
    Button(root, command = asia, text = 'Азия', width = 30, height = 6, bg = colour, activebackground = colour).grid(row = 0, column = 5, ipadx=10, ipady=6, padx=10, pady=10)
    Button(root, command = answer, text = 'Ответы', width = 30, height = 3, bg = colour, activebackground = colour).grid(row = 3, column = 0, ipadx=10, ipady=6, padx=10, pady=10)
    Button(root, command = result, text = 'Результаты', width = 150, height = 3, bg = colour, activebackground = colour).grid(row = 5, column = 0, ipadx=10, ipady=6, padx=10, pady=10, columnspan = 4)
    Button(root, command = constructor.simpletest_for_cc, text = 'Конструктор тестов для Викторины', width = 150, height = 3, bg = colour, activebackground = colour).grid(row = 6, column = 0, ipadx=10, ipady=6, padx=10, pady=10, columnspan = 4)
    Button(root, command = europe, text = 'Европа', width = 30, height = 6, bg = colour, activebackground = colour).grid(row = 1, column = 0, ipadx=10, ipady=6, padx=10, pady=10)
    Button(root, command = lambda: exit(), text = 'Выход', width = 150, height = 3, bg = colour, activebackground = colour).grid(row = 7, column = 0, ipadx=10, ipady=6, padx=10, pady=10, columnspan = 4)
    root.mainloop()
