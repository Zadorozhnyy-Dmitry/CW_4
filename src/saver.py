import json
from abc import ABC, abstractmethod

from config import FILE_PATH


class Saver(ABC):
    """
    Абстрактный класс для сохранения данных в файл
    """

    @abstractmethod
    def load_from_file(self):
        """
        Метод загружает данные из файла
        :return:
        """
        pass

    @abstractmethod
    def write_to_file(self, data):
        """
        Метод записывает данные в файл
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def delite_vacancy_from_file(self):
        """
        Метод удаляет данные из файла
        :return:
        """
        pass


class JSONSaver(Saver):
    """
    Класс для работы с файлом данных json
    """

    def __init__(self):
        self.__path = FILE_PATH

    def load_from_file(self) -> list[dict]:
        """
        Метод читает json файл
        :return:
        """
        with open(self.__path, 'r', encoding='utf-8') as data:
            return json.load(data)

    def write_to_file(self, data: list[dict]) -> None:
        """
        Метод записывает вакансии в json файл
        :param data:
        :return:
        """
        with open(self.__path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delite_vacancy_from_file(self):
        pass
