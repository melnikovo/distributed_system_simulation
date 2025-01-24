from server import Server
from task import Task
from distributed_system import DistributedSystem


if __name__ == "__main__":
    system = DistributedSystem()
    while True:
        system.create_task()
        more_tasks = input("Задать новую задачу? y/n: ")
        if more_tasks.lower() != 'y':
            break
    system.distribute_tasks()
    system.run_system()


