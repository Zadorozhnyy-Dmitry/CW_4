import logging

from src.exceptions import UserIneractionException
from src.vacancy import Vacancy

logger = logging.getLogger(__name__)


class UserInteraction:
    """
    Класс для взаимодействия с юзером
    """

    def __init__(self):
        self.__vacancies_list: list[Vacancy] = []
        self.__answer_dict: dict = {}

    @property
    def vacancies_list(self):
        """
        Доступ к атрибуту списка вакансий
        :return:
        """
        return self.__vacancies_list

    @property
    def answer_dict(self):
        """
        Доступ к словарю ответов юзера
        :return:
        """
        return self.__answer_dict

    @answer_dict.setter
    def answer_dict(self, values: list):
        """
        Сеттер для словаря ответов, для проведения тестов
        :param values:
        :return:
        """
        self.__answer_dict['text'] = values[0]
        self.__answer_dict['top_n'] = values[1]
        self.__answer_dict['filter_words'] = values[2]
        self.__answer_dict['salary_range'] = values[3]

    def list_questions(self) -> dict:
        """
        Метод задает вопросы пользователю и создает словарь с параметрами запроса
        :return:
        """
        print('Поисковый запрос ввести обязательно, остальные параметры можно пропустить нажав клавишу "Enter"')
        search_query: str = input("Введите поисковый запрос: ")
        top_n: str = input("Введите количество вакансий для вывода в топ N: ").strip()
        filter_words: list[str] = input("Введите ключевые слова для фильтрации вакансий: ").split()
        salary_range: str = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")
        print()

        if search_query:
            self.__answer_dict['text'] = search_query
        else:
            self.__answer_dict['text'] = None

        if top_n.isnumeric():
            self.__answer_dict['top_n'] = int(top_n)
        else:
            self.__answer_dict['top_n'] = None

        if filter_words:
            self.__answer_dict['filter_words'] = filter_words
        else:
            self.__answer_dict['filter_words'] = None

        if salary_range and salary_range.find('-') != -1:
            salary_from, salary_to = salary_range.split('-')
            if salary_from.strip().isnumeric() and salary_to.strip().isnumeric():
                salary_from = int(salary_from)
                salary_to = int(salary_to)
                self.__answer_dict['salary_range'] = {'salary_from': salary_from, 'salary_to': salary_to}
            else:
                self.__answer_dict['salary_range'] = None
        else:
            self.__answer_dict['salary_range'] = None

        return self.__answer_dict

    def filter_vacancies(self, vacancies: list[Vacancy]) -> list[Vacancy]:
        """
        Метод фильтрует вакансии по ключевым словам
        :param vacancies:
        :return:
        """
        set_vac = ()
        if self.__answer_dict['filter_words']:
            for word in self.__answer_dict['filter_words']:
                for vacancy in vacancies:
                    if vacancy.name.lower().find(word.lower()) != -1:
                        self.__vacancies_list.append(vacancy)
            set_vac = set(self.__vacancies_list)
            self.__vacancies_list = list(set_vac)
            return self.__vacancies_list
        else:
            self.__vacancies_list = vacancies
            return self.__vacancies_list

    def ranged_vacancies(self) -> list[Vacancy]:
        """
        Метод фильтрует вакансии по диапазону зарплат
        :return:
        """
        if self.__answer_dict['salary_range'] and self.__vacancies_list:
            ranges_vacancies = []
            salary_from = self.__answer_dict['salary_range']['salary_from']
            salary_to = self.__answer_dict['salary_range']['salary_to']

            for vacancy in self.__vacancies_list:
                if salary_to == 0:
                    if salary_from <= vacancy.salary_from:
                        ranges_vacancies.append(vacancy)
                else:
                    if salary_from <= vacancy.salary_from <= salary_to:
                        ranges_vacancies.append(vacancy)
            self.__vacancies_list = []
            self.__vacancies_list = ranges_vacancies
            return self.__vacancies_list
        else:
            return self.__vacancies_list

    def get_top_vacancies(self) -> list[Vacancy]:
        """
        Метод сортирует вакансии по величине зарплаты и выводит топ N вакансий
        :return:
        """
        if self.__answer_dict['top_n'] and self.__vacancies_list:
            sorted_list = sorted(self.__vacancies_list, reverse=True)[:self.__answer_dict['top_n']]
        else:
            sorted_list = sorted(self.__vacancies_list, reverse=True)

        self.__vacancies_list = sorted_list
        return self.__vacancies_list
