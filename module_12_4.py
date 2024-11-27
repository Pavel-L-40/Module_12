# ======================== test rt_with_exceptions =========================

import  rt_with_exceptions as modul
import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(name)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):
    def test_walk1(self):
        try:
            walk_test1 = modul.Runner('walk_test', -1)
            walk_test1.walk()
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner")
    def test_walk2(self) -> None:
        try:
            walk_test2 = modul.Runner('walk_test', 2)
            walk_test2.walk()
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner")

    def test_run1(self):
        try:
            run_test3 = modul.Runner('Ron', 5)
            run_test3.run()
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner")
    def test_run2(self):
        try:
            run_test3 = modul.Runner(5)
            run_test3.run()
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner")



