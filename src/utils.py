from src.vacancy import Vacancy


def get_vacancies_list(vacancies: list[dict]) -> list[Vacancy]:
    """
    Функция преобразует список вакансий из json в список экземпляров класса Vacancy
    :param vacancies:
    :return:
    """
    return [Vacancy.new_vacancy(vacancy) for vacancy in vacancies]
