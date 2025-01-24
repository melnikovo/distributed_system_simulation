import random

class Task:
    def __init__(self, employee_name):
        self.employee_name = employee_name
        self.num_reports = random.randint(10, 20) # Количество отчётов
        self.complexity = random.randint(1, 10) #Сложность задания
        self.duration = self.num_reports * 0.1 # Время обработки одного отчёта равно 0.56 сек
        self.description = f"Обработка отчётов для {employee_name} ({self.num_reports} отчётов)"
