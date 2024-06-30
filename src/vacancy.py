class Vacancy:
    """
    Класс обрабатывающий вакансию
    """
    __slots__ = ['__pk', '__name', '__area', '__salary_from', '__salary_to', '__link']

    def __init__(
            self,
            pk: str,
            name: str,
            area: str,
            salary_from: int,
            salary_to: int,
            link: str
    ):
        self.__pk = self.__validate_string_field(pk)
        self.__name = self.__validate_string_field(name)
        self.__area = self.__validate_string_field(area)
        self.__salary_from = self.__validate_salary(salary_from)
        self.__salary_to = self.__validate_salary(salary_to)
        self.__link = self.__validate_string_field(link)

    @property
    def pk(self):
        """
        Доступ к атрибуту ID
        :return:
        """
        return self.__pk

    @property
    def name(self) -> str:
        """
        Доступ к атрибуту name
        :return:
        """
        return self.__name

    @property
    def salary_from(self) -> int:
        """
        Доступ к атрибуту зарплаты
        :return:
        """
        return self.__salary_from

    @property
    def salary_to(self) -> int:
        """
        Доступ к атрибуту зарплаты
        :return:
        """
        return self.__salary_to

    def __str__(self) -> str:
        return (f'Вакансия: {self.__name}\n'
                f'Местоположение: {self.__area}\n'
                f'Зарплата от: {self.__salary_from} '
                f'Ссылка: {self.__link}\n')

    def __repr__(self) -> str:
        return (f'Вакансия ID: {self.__pk} ,name: {self.__name}\n'
                f'Местоположение: {self.__area} Зарплата {self.__salary_from}-{self.salary_to}\n'
                f'Ссылка: {self.__link}\n')

    def __lt__(self, other) -> bool:
        return self.salary_from < other.salary_from

    def __gt__(self, other) -> bool:
        return self.salary_from > other.salary_from

    def __hash__(self):
        return hash(self.__pk)

    @staticmethod
    def __validate_string_field(field: str) -> str:
        """
        Метод проверки строковых значений
        :param field:
        :return:
        """
        return field if field else '----------'

    @staticmethod
    def __validate_salary(salary: int) -> int:
        """
        Метод проверки атрибута зарплаты
        :param salary:
        :return:
        """
        return salary if salary else 0

    @classmethod
    def new_vacancy(cls, vacancy_data: dict):
        """
        Метод для создания экземпляра класса
        :param vacancy_data:
        :return:
        """
        return cls(
            pk=vacancy_data.get('id'),
            name=vacancy_data.get('name'),
            area=vacancy_data.get('area').get('name') if vacancy_data.get('area') else None,
            salary_from=vacancy_data.get('salary').get('from') if vacancy_data.get('salary') else None,
            salary_to=vacancy_data.get('salary').get('to') if vacancy_data.get('salary') else None,
            link=vacancy_data.get('url'),
        )
