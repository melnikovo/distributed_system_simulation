
class Server:
    def __init__(self, performance, name):
        self.performance = performance
        self.load = 0    # Текущая загрузка сервера
        self.task_queue = []  # Очередь заданий для сервера
        self.name = name

    def start_task(self, task):
        task_time = task.duration * task.complexity/self.performance
        if self.load == 0: # Если сервер свободен, сразу начать выполнение задания
            self.load += task_time
            print(f"Начало выполнения задачи. Ожидание {task_time:.2f} секунд.")
        self.task_queue.append(task)     # Иначе задание попадает в очередь
        print(f"Задача направлена в очередь. Ожидаемое время на решение задачи {task_time:.2f} секунд.")

    def process_task(self, time):
        if self.load > 0:
            self.load = max(0, self.load - time)
        #Если загрузка нулевая:
        if self.load == 0 and self.task_queue:
            # Следующее задание удаляется из списка task_queue и попадает в очередь
            next_task = self.task_queue.pop(0)
            task_duration = next_task.duration * next_task.complexity / self.performance
            self.load = task_duration
            print(f"Сервер {self.name} обработал отчёт для {next_task.employee_name} за {task_duration:.2f} секунд.")

    def report_status(self):
        if self.load > 0:
            print(f"Сервер {self.name} занят очень важной задачей")

        print(f"Сервер {self.name} свободен")



