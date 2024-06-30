import logging

from src.api import HhAPI
from src.exceptions import APIException
from src.saver import JSONSaver
from src.user_interaction import UserInteraction
from src.utils import get_vacancies_list

logger = logging.getLogger(__name__)


def main():
    # взаимодействие с пользователем
    user = UserInteraction()
    user.list_questions()
    # инициализирую экземпляр класса работы с API
    hh = HhAPI()
    # присваивание ключевого слова в запрос get
    hh.text = user.answer_dict['text']
    # запрос на сайт и проверка обмена данными
    try:
        hh.get_response_data()
    except APIException as e:
        logger.exception(f'Ошибка обращения к HhAPI. {e}')
        print('Сервис временно не доступен')
    # загрузка найденных вакансий в список
    hh.load_vacancies()

    # преобразую словарь вакансий в словарь с экземплярами класса
    list_vac = get_vacancies_list(hh.vacancies)

    # фильтрация по ключевым словам, если они есть
    user.filter_vacancies(list_vac)

    # фильтрация по диапазону зарплат
    user.ranged_vacancies()
    # сортировка по убыванию з/п и выдача запрошенного кол-ва вакансий
    user.get_top_vacancies()
    # сохраняю список вакансий в файл
    saver = JSONSaver()
    saver.write_to_file(hh.vacancies)
    # вывод вакансий в терминал
    for i in user.vacancies_list:
        print(i)


if __name__ == '__main__':
    main()
