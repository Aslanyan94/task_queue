# Task Queue with Priorities and Resource Limits

This project provides a Python implementation of a task queue with priorities and resource limits. The queue allows publishers to create tasks with specified resource requirements, and consumers receive the highest priority task that can be processed with the available resources. This is particularly useful in scenarios where tasks vary in priority and resource needs.

## Implementation

The implementation consists of three main components:

1. **Resources Class:**
   - Represents the resources required for a task, including RAM, CPU cores, and GPU count.
   - Defined using the `Resources` data class.

2. **Task Class:**
   - Represents a task with an ID, priority, required resources, content, and result.
   - Defined using the `Task` data class.

3. **TaskQueue Class:**
   - Manages the task queue, allowing publishers to add tasks and consumers to retrieve tasks based on available resources and priority.
   - The `add_task` method adds tasks to the queue, and the `get_task` method retrieves the highest priority task that satisfies the available resources.

## Usage

To use the task queue, follow these steps:

1. Create tasks using the `Task` class, specifying the task's ID, priority, required resources, content, and result.

   ```
   task = Task(id=1, priority=1, resources=Resources(ram=4, cpu_cores=2, gpu_count=1), content="Task Content", result="")``

2. Create a task queue instance.
    
   ``` 
   task_queue = TaskQueue()
3. Add tasks to the queue using the `add_task` method.

   ```
   task_queue.add_task(task)

4. Retrieve tasks based on available resources using the `get_task` method.
   ```
   available_resources = Resources(ram=4, cpu_cores=2, gpu_count=1)
   task_to_process = task_queue.get_task(available_resources)


## Unit Test
Included in the project is a unit test script (test_task_queue.py) that demonstrates the operation of the task queue. This test case covers the addition of tasks to the queue and the retrieval of tasks based on available resources and priority.

To run the unit test:
   ```
   python test_task_queue.py 
```






