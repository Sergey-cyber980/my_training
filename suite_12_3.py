import unittest
from tests_12_3 import RunnerTest, TournamentTest  # Импортируйте ваши тестовые классы

# Создаем тестовый набор
test_suite = unittest.TestSuite()

# Добавляем тесты
test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))

# Запускаем тесты
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)

