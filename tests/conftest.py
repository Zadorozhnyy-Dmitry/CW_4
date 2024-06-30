import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vac1():
    return Vacancy(
        pk='1',
        name='Разрaботчик программист Python',
        area='Москва',
        salary_from=30_000,
        salary_to=70_000,
        link='http/vac1',
    )


@pytest.fixture
def vac2():
    return Vacancy(
        pk='2',
        name='Аналитик программист Python',
        area='Москва',
        salary_from=50_000,
        salary_to=0,
        link='http/vac2',
    )


@pytest.fixture
def vac_list(vac1, vac2):
    return [vac1, vac2]


@pytest.fixture
def list_dict():
    return [
        {
            "id": "1",
            "name": "Разрaботчик программист Python",
            "area": {
                "name": "Москва",
            },
            "salary": {
                "from": 30_000,
                "to": 70_000,
            },
            "url": "http/vac1",
        },
    ]
