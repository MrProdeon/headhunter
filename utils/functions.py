from src.Vacancy import Vacancy


def top_n(vacancies : list[Vacancy], n : int):
    """Функция для отображения топовых вакансий по зарплате.
    Количество отображения регулируется параметром n"""

    top_vacancies = sorted(vacancies, key=lambda x: x.salary_from)

    top_n_vacancies = [top_vacancies[i] for i in range(n)]


    return top_n_vacancies

def ranged_vacancies(vacancies : list[Vacancy], range_from : int | float, range_to : int | float = None):
    """Функция для отображения вакансий в выбранном диапазоне зарплат."""

    if not range_to:
        ranged_vacancies = [vacancy for vacancy in vacancies if vacancy.salary_from >= range_from]
    else:
        ranged_vacancies = [vacancy for vacancy in vacancies if vacancy.salary_from >= range_from
                            and vacancy.salary_to <= range_to]

    return ranged_vacancies
