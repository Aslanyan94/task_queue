import unittest

from models import Task, Resources
from queues import TaskQueue


class TestPriorityQueues(unittest.TestCase):
    def setUp(self):
        self.task_queue = TaskQueue()
        self.available_resources = Resources(ram=12, cpu_cores=4, gpu_count=2)

    def test_integration(self):
        # commensurate with available resources
        task1 = Task(id=1, priority=3, resources=Resources(ram=4, cpu_cores=2, gpu_count=1), content="Task 1", result="")
        task2 = Task(id=2, priority=1, resources=Resources(ram=8, cpu_cores=4, gpu_count=2), content="Task 2", result="")
        task3 = Task(id=3, priority=2, resources=Resources(ram=6, cpu_cores=3, gpu_count=1), content="Task 3", result="")

        # inconsistent with available resources
        task4 = Task(id=3, priority=2, resources=Resources(ram=13, cpu_cores=3, gpu_count=1), content="Task 3", result="")
        task5 = Task(id=3, priority=2, resources=Resources(ram=6, cpu_cores=13, gpu_count=1), content="Task 3", result="")
        task6 = Task(id=3, priority=2, resources=Resources(ram=6, cpu_cores=3, gpu_count=51), content="Task 3", result="")
        task7 = Task(id=3, priority=2, resources=Resources(ram=16, cpu_cores=13, gpu_count=1), content="Task 3", result="")
        task8 = Task(id=3, priority=2, resources=Resources(ram=16, cpu_cores=3, gpu_count=5), content="Task 3", result="")
        task9 = Task(id=3, priority=2, resources=Resources(ram=6, cpu_cores=13, gpu_count=5), content="Task 3", result="")
        task10 = Task(id=3, priority=2, resources=Resources(ram=16, cpu_cores=10, gpu_count=5), content="Task 3", result="")

        self.task_queue.add_task(task1)
        self.task_queue.add_task(task2)
        self.task_queue.add_task(task3)
        self.task_queue.add_task(task4)
        self.task_queue.add_task(task5)
        self.task_queue.add_task(task6)
        self.task_queue.add_task(task7)
        self.task_queue.add_task(task8)
        self.task_queue.add_task(task9)
        self.task_queue.add_task(task10)

        # assertion
        self.assertEqual(self.task_queue.get_task(self.available_resources), task1)
        self.assertEqual(self.task_queue.get_task(self.available_resources), task3)
        self.assertEqual(self.task_queue.get_task(self.available_resources), task2)
        self.assertEqual(self.task_queue.get_task(self.available_resources), None)
