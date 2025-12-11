from src.connector import Connector, HeadHunterApi

hh_api = HeadHunterApi("https://api.hh.ru/vacancies", {"User-Agent" : "test for skypro"})
vacancies = hh_api.get_vacancies()


def main():
    filted_words = input("Введите ключевые слова для поиска: ")
    top_n = input("Введите количество вакансий для вывода в топе зарплат: ")
    salary_range = input("Введите диапазон зарплат(Формат 50000-10000): ")

if __name__ == "__main__":
    pass