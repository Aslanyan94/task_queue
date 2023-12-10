import unittest

from models import Resources, Task


class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        """
        Add a task to the queue.
        """
        self.tasks.append(task)

    def get_task(self, available_resources: Resources) -> Task:
        """
        Get the highest priority task that satisfies available resources.
        """
        eligible_tasks = [task for task in self.tasks if self._has_sufficient_resources(task.resources, available_resources)]

        if not eligible_tasks:
            return None

        # Sort eligible tasks by priority in descending order
        sorted_tasks = sorted(eligible_tasks, key=lambda x: x.priority, reverse=True)

        # Retrieve and remove the task with the highest priority
        if sorted_tasks:
            highest_priority_task = sorted_tasks[0]
            self.tasks.remove(highest_priority_task)
            return highest_priority_task

    @staticmethod
    def _has_sufficient_resources(task_resources: Resources, available_resources: Resources) -> bool:
        """
        Check if available resources are sufficient for the task.
        """
        return (
            task_resources.ram <= available_resources.ram
            and task_resources.cpu_cores <= available_resources.cpu_cores
            and task_resources.gpu_count <= available_resources.gpu_count
        )


def main():
    task_queue = TaskQueue()
    available_resources = Resources(ram=6, cpu_cores=2, gpu_count=1)
    task = Task(id=1, priority=3, resources=Resources(ram=4, cpu_cores=2, gpu_count=1), content="Task 1", result="")

    task_queue.add_task(task)
    a_task = task_queue.get_task(available_resources)
    print(a_task)


if __name__ == "__main__":
    main()
