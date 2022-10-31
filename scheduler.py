from queue import Queue
from unittest import result

from tasks import Task


class Scheduler:
    def __init__(self):
        self.ready = Queue()
        self.task_map = {}

    def new(self, target):
        new_task = Task(target=target)
        self.task_map[new_task.tid] = new_task
        self.schedule(new_task)
        return new_task.id

    def schedule(self, task):
        self.ready.put(task)

    def main_loop(self):
        while self.task_map:
            task = self.ready.get()
            try:
                result = task.run()
            except StopIteration:
                self.exit()
                continue
            self.schedule(task)

    def exit(self, task):
        print(f"Task {task.tid} terminated.")
        del self.task_map[task.tid]