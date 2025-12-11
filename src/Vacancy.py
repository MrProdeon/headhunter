class Vacancy:
    """Класс для работы с вакансиями.
    У каждой вакансии должно быть указано название, ссылка на вакансию, зарплата и описание.
    Объекты этого метода поддерживают сравнение между собой. Сравнение происходит по зарплате.
    Прописаны приватные методы валидации, которые используются при инициализации объекта.
    Валидация проверяет указана ли ЗП и в числовом ли виде, если она не указана или указана строкой, то ставим 0.
    Так же проверяем указано ли название. Если нет, то прописываем Без названия.
    """

    __slots__ = ("title", "link", "salary_from","salary_to", "description")

    def __init__(self, title: str, link: str, salary_from: int | float, salary_to: int | float):
        self.title = self.__validate_title(title)
        self.link = link
        self.salary_from = self.__validate_salary(salary_from)
        self.salary_to = self.__validate_salary(salary_to)

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.salary > other
        raise ValueError("Переданы несравнимые данные")

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.salary >= other
        raise ValueError("Переданы несравнимые данные")

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.salary < other
        raise ValueError("Переданы несравнимые данные")

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        elif isinstance(other, int) or isinstance(other, float):
            return self.salary <= other
        raise ValueError("Переданы несравнимые данные")

    @staticmethod
    def __validate_title(title: str):
        if not isinstance(title, str) or not title:
            title = "Без названия"
        else:
            title = title
        return title

    @staticmethod
    def __validate_salary(salary: int | float):
        if salary is None:
            salary = "Не указано"
        else:
            salary = salary
        return salary