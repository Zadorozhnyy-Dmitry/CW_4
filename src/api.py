from abc import ABC, abstractmethod
from json import JSONDecodeError

import requests

from requests import Response

from config import HH_URL
from src.exceptions import HhAPIException


class API(ABC):
    """
    Абстрактный класс для взаимодействия с интерфейсом API
    """

    @abstractmethod
    def _get_response(self) -> Response:
        """
        Абстрактный метод получает объект Response с помощью метода get из библиотеки request
        :return:
        """
        pass

    @staticmethod
    @abstractmethod
    def _check_status(response: Response) -> bool:
        """
        Абстрактный метод проверяет статус запроса метода get из библиотеки request
        :return:
        """
        pass

    @abstractmethod
    def get_response_data(self) -> dict:
        """
        Абстрактный метод преобразует Response в json
        :return:
        """
        pass


class HhAPI(API):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url: str = HH_URL
        self.__params: dict = {
            'page': 0,
            'per_page': 100,
            'search_field': 'name',
            'area': 113,
        }
        self.__text: str | None = None
        self.vacancies: list = []

    @property
    def text(self) -> str:
        """
        доступ к атрибуту text
        :return:
        """
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        """
        Сеттер для атрибута text
        :param text:
        :return:
        """
        if text != '':
            self.__text = text

    def _get_response(self) -> Response:
        """
        Метод получает объект Response со списком вакансий с ресурса hh
        :return:
        """
        if self.text is None:
            raise HhAPIException('Поисковый запрос не задан')

        self.__params['text'] = self.text
        return requests.get(self.__url, params=self.__params)

    @staticmethod
    def _check_status(response: Response) -> bool:
        """
        Метод проверяет статус запроса request
        :param response:
        :return: если код 200 возвращает True
        """
        return response.status_code == 200

    def get_response_data(self) -> dict:
        """
        Метод работает с Response:
        если статус соединения с сервером 200
        - проверяет полученный response и преобразует его в json
        :return:
        """
        response = self._get_response()
        is_connect = self._check_status(response)
        if not is_connect:
            raise HhAPIException('Ошибка соединения с сервером hh')
        try:
            return response.json()
        except JSONDecodeError:
            raise HhAPIException('Ошибка получения данных, получен не json объект')

    def load_vacancies(self) -> list[dict]:
        """
        Метод обрабатывает все страницы запроса по вакансиям и передает список вакансий в атрибут класса
        :return:
        """
        numbers_pages: int = self.get_response_data()['pages']
        for i in range(numbers_pages):
            self.__params['page'] = i
            vacancies = self.get_response_data()['items']
            self.vacancies.extend(vacancies)
        return self.vacancies
