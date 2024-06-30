import logging
from pathlib import Path

HH_URL = 'https://api.hh.ru/vacancies'

FORMAT = "%(asctime)-30s %(filename)-20s %(message)s"

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w", format=FORMAT)

FILE_PATH = Path(__file__).parent.joinpath("data/vacancies.json")
