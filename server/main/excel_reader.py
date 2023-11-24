import openpyxl
def parse_xls(file_name, sheet_number):  # Функции чтение excel файла (имя файла, номер листа)

    book = openpyxl.load_workbook(file_name)
    sheet = book.worksheets[sheet_number]

    groups = {}
    week = ""
    line = [1, 1]

    for col in sheet.iter_cols():  # Итерируемся по стобцам
        day_num = 0  # Переменная для подсчёта дней недели
        i = 0

        sched = {  # Словарь для записи расписания для одной группы
            "groupName": None,
            "studyStartTS": 1694379600,
            "startTime": 28800,
            "lessonLength": 5400,
            "breaks": [1200, 600, 1200, 600, 600, 600, 600],
            "weeks": {
                "odd": [[], [], [], [], []],
                "even": [[], [], [], [], []],
            }
        }

        for cell in col:

            if cell.value is None:  # Игнорируем NoneType значения
                i += 1
                continue

            if i == 0:
                if str(cell.value)[7:] not in groups:  # Записываем название группы
                    groups[str(cell.value)[7:]] = sched
                    group = str(cell.value)[7:]
                    groups[group]["groupName"] = group

                i += 1
                continue

            if i == 1:
                if cell.value == "Чётная неделя":  # Переменная week для хранения чётности недели
                    week = "even"
                elif cell.value == "Нечётная неделя":
                    week = "odd"

                i += 1
                continue

            line = [j for j in str(cell.value).split("  ")]  # Считываем
            #print(line)

            if line[1] == "-":  # Записывем отсутствующие пары как NoneType
                lesson = None

            else:
                lesson = {"name": line[2],
                          "teacher": line[3],
                          "practical": (True if line[1] == "ПЗ" else False),
                          "room": line[4]
                          }

            groups[group]["weeks"][week][day_num].extend([lesson])

            if int(line[0]) == 7:
                day_num += 1

            i += 1
            #print(day_num)
    return groups