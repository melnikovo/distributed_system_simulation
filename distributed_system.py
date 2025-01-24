from server import Server
from task import Task
import time

class DistributedSystem:
    def __init__(self):

        self.servers = [
            Server(performance=0.9, name="Алёша Попович"),
            Server(performance =0.5, name="Добрыня Никитич"),
            Server(performance =0.1, name="Илья Муромец")
        ]
        self.tasks = []

    def create_task(self):
        last_name = input("Введите фамилию сотрудника (латиницей): ")
        employee_id = input("Введите двухзначный ID сотрудника: ")
        #Проверка на двузначность не проводится, так как это симуляция
        employee_name = f"{last_name}_{employee_id}"

        task = Task(employee_name)
        self.tasks.append(task)
        print(task.description)
        return task

    def distribute_tasks(self):
        for task in self.tasks:
            available_server = min(self.servers, key=lambda s: s.load)
            print(f"Задача {task.description} назначена серверу {available_server.name} с производительностью {available_server.performance}.")
            available_server.start_task(task)
            print(f"Задача {task.description} отправлена на сервер.")

    def run_system(self):
            current_time = 0
            time_step = 0.3
            task_index = 0

            while task_index < len(self.tasks) or any(server.load > 0 for server in self.servers):
                for server in self.servers:
                    server.process_task(time_step)

                if task_index < len(self.tasks):
                    task = self.tasks[task_index]
                    """пока task_index не будет равен количеству задач в self.tasks, цикл продолжит свою работу. 
                    То есть на каждом шаге цикла будет извлекаться следующая задача из списка и передаваться серверу, 
                    пока все задачи не будут выполнены.
                    Так что индекс изменяется с каждым шагом, а не остаётся равным 0."""
                    for server in self.servers:
                        if server.load == 0:
                            server.start_task(task)
                            task_index += 1
                            break

                for server in self.servers:
                    server.report_status()

                current_time += time_step
                time.sleep(time_step)

