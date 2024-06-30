from src.user_interaction import UserInteraction
from src.vacancy import Vacancy

list_for_test_empty = ['Python', None, None, None]

list_for_test_filter_1 = ['Python', None, ['Разрaботчик'], None]
list_for_test_filter_2 = ['Python', None, ['аналитик'], None]
list_for_test_filter_3 = ['Python', None, ['аналитик', 'Программист'], None]


def test_filter_vacancies_1(vac1: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_filter_1
    user.filter_vacancies(vac_list)
    assert user.vacancies_list == [vac1]


def test_filter_vacancies_2(vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_filter_2
    user.filter_vacancies(vac_list)
    assert user.vacancies_list == [vac2]


def test_filter_vacancies_3(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_filter_3
    user.filter_vacancies(vac_list)
    assert sorted(user.vacancies_list) == [vac1, vac2]


def test_filter_vacancies_4(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_empty
    user.filter_vacancies(vac_list)
    assert user.vacancies_list == [vac1, vac2]


def test_ranged_vacancies_1(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_empty
    user.filter_vacancies(vac_list)
    user.ranged_vacancies()
    assert user.vacancies_list == [vac1, vac2]


list_for_test_range_2 = ['Python', None, None, {'salary_from': 20_000, 'salary_to': 65_000}]


def test_ranged_vacancies_2(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_range_2
    user.filter_vacancies(vac_list)
    user.ranged_vacancies()
    assert user.vacancies_list == [vac1, vac2]


list_for_test_range_3 = ['Python', None, None, {'salary_from': 60_000, 'salary_to': 100_000}]


def test_ranged_vacancies_3(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_range_3
    user.filter_vacancies(vac_list)
    user.ranged_vacancies()
    assert user.vacancies_list == []


list_for_test_range_4 = ['Python', None, None, {'salary_from': 29_000, 'salary_to': 49_000}]


def test_ranged_vacancies_4(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_range_4
    user.filter_vacancies(vac_list)
    user.ranged_vacancies()
    assert user.vacancies_list == [vac1]


list_for_test_range_5 = ['Python', None, None, {'salary_from': 31_000, 'salary_to': 89_000}]


def test_ranged_vacancies_5(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_range_5
    user.filter_vacancies(vac_list)
    user.ranged_vacancies()
    assert user.vacancies_list == [vac2]


list_for_test_range_6 = ['Python', None, None, {'salary_from': 31_000, 'salary_to': 0}]


def test_ranged_vacancies_6(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_range_6
    user.filter_vacancies(vac_list)
    user.ranged_vacancies()
    assert user.vacancies_list == [vac2]


def test_get_top_vacancies(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_empty
    user.filter_vacancies(vac_list)
    user.ranged_vacancies()
    user.get_top_vacancies()
    assert user.vacancies_list == [vac2, vac1]


list_for_test_top = ['Python', 1, None, None]


def test_get_top_vacancies_1(vac1: Vacancy, vac2: Vacancy, vac_list: list[Vacancy]):
    user = UserInteraction()
    user.answer_dict = list_for_test_top
    user.filter_vacancies(vac_list)
    user.ranged_vacancies()
    user.get_top_vacancies()
    assert user.vacancies_list == [vac2]
