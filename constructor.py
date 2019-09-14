from tkinter import Tk, simpledialog, messagebox, Menu
from itertools import cycle
v = 'v 1.0.12'
def simpletest_for_cc():
    def new_file(): simpletest_for_cc
    def save_file():
        filename = simpledialog.askstring('Сохранение файла', 'Как вы назовёте файл?')
        with open('{}.txt'.format(filename), mode = 'w', encoding = 'utf-8') as file:
            file.write(str(list(a)) + '\t' + str(list(b)) + '\t' + str(n) +'\t' + testname + '\n')
            file.close()
    def open_file():
        filename = simpledialog.askstring('Открытие файла', 'Имя файла, который вы хотите открыть:')
        with open('{}.txt'.format(filename), mode = 'r', encoding = 'utf-8'()) as file:
            dan = file.read()
            # a, b, n, testname = dan.split('\t')
            file.close()
    def testing ():
        points = 0
        for i in range(1, n):
            d = next(a)
            f = next(b)
            one = simpledialog.askstring('Вопрос №{}'.format(i), 'Введите столицу {}:'.format(d))
            if one == f:
                points = points + 1
                messagebox.showinfo('', 'Правильно!')
            else:
               messagebox. showinfo('', 'Неправильно!')
        messagebox.showinfo('Результат', 'Ваши очки: ' + str(points))
        name = simpledialog.askstring('Сохранение результата', 'Будете ли вы сохранять результат? Если нет, то введите no. Иначе введите имя:')
        if name.lower() != 'no':
            with open('results.txt', 'a', encoding = 'utf-8') as file:
                file.write('\nИгрок: ' + name + '   очки: ' + str(points) + '   уровень сложности/режим: {}'.format(testname) + '    дата игры: ' + str(datetime.datetime.now()) + '   ' + v)
    tk = Tk()
    tk.title('Конструктор тестов (для Викторины по Столицам {}) v 1.0.4'.format(v))
    main_menu = Menu(tk)
    file_menu = Menu(main_menu)
    file_menu.add_command(label="New", command = new_file)
    file_menu.add_command(label="Save", command = save_file)
    file_menu.add_command(label="Open", command = open_file)
    main_menu.add_command(label="Exit", command = lambda tk: tk.destroy())
    main_menu.add_cascade(label="File", menu=file_menu)
    main_menu.add_cascade(label="Test", command = testing)
    tk.config(menu = main_menu)
    tk.tkraise()
    testname = simpledialog.askstring('Шаг 1', 'Имя вашего теста:') 
    n = simpledialog.askinteger('Шаг 2', 'Сколько вопросов будет в вашем тесте?')
    a = cycle([n])
    b = cycle([n])
    for i in range(1, n):
        c = next(a)
        s = next(b)
        c = simpledialog.askstring('Заполнение стран', 'Страна {}'.format(i))
        s = simpledialog.askstring('Заполнение столиц', 'Столица {}'.format(i))
