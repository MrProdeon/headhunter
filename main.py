from src.connector import Connector, HeadHunterApi
from utils.functions import ranged_vacancies, top_n
from src.Vacancy import Vacancy

hh_api = HeadHunterApi("https://api.hh.ru/vacancies", {"User-Agent" : "test for skypro"})


def main():
    target = sorted(list(map(int,input("""По каким критериям отфильтровать вакансии?
1 - ключевые слова
2 - по диапазону зарплат
3 - по самым высоким зарплатам
4 - удалёнка или офис
(Напишите в одну строку через пробел)
""").split())))

    if 1 in target:
        name = input("Введите ключевые слова: ")
        vacancies = hh_api.get_vacancies(name)
    else:
        vacancies = hh_api.get_vacancies()

    if 2 in target or 3 in target:
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










if __name__ == "__main__":
    print(main())