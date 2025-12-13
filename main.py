from src.connector import Connector, HeadHunterApi
from utils.functions import ranged_vacancies, top_n, print_vacancies
from src.Vacancy import Vacancy

hh_api = HeadHunterApi("https://api.hh.ru/vacancies", {"User-Agent" : "test for skypro"})


def main():
    while True:
        try:
            target = sorted(list(map(int, input("""По каким критериям отфильтровать вакансии?
1 - ключевые слова
2 - по диапазону зарплат
3 - по самым высоким зарплатам
4 - удалёнка или офис
(Напишите в одну строку через пробел)
""").strip().split())))
        except ValueError:
            continue
        if all(number in (1, 2, 3, 4) for number in target):
            break

    if 1 in target:
        name = input("Введите ключевые слова: ")
        vacancies = hh_api.get_vacancies(name)
    else:
        vacancies = hh_api.get_vacancies()

    if 4 in target:
        work_f = input("1 - для поиска удалёнки, 2 - для поиска офиса, 3 - гибрид")
        while work_f not in ("1", "2", "3"):
            work_f = input("1 - для поиска удалёнки, 2 - для поиска офиса, 3 - гибрид")
        if work_f == "1":
            vacancies = [vacancy for vacancy in vacancies if
                         any(work_format["id"] == "REMOTE" for work_format in vacancy["work_format"])]
        if work_f == "2":
            vacancies = [vacancy for vacancy in vacancies if
                         any(work_format["id"] == "ON_SITE" for work_format in vacancy["work_format"])]
        if work_f == "3":
            vacancies = [vacancy for vacancy in vacancies if
                         any(work_format["id"] == "HYBRID" for work_format in vacancy["work_format"])]


    vacancies = Vacancy.cast_to_object_list(vacancies)

    if 2 in target:
        while True:
            range_from = input("Введите начальную зарплату: ")
            range_to = input("Введите конечную зарплату: ")
            try:
                range_from = int(range_from)
                range_to = int(range_to)
                break
            except ValueError:
                print("Введите число!")
                continue

        vacancies = ranged_vacancies(vacancies, range_from, range_to)

    if 3 in target:
        n = input("Какое отобразить количество вакансий с максимальной ЗП?  ")
        while True:
            try:
                n = int(n)
                break
            except ValueError:
                print("Введите число!")
                continue
        vacancies = top_n(vacancies, n)

    return vacancies




# Сделать перелистывание страницы







if __name__ == "__main__":
    print_vacancies(main())