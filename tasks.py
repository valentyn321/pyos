class Task:
    """A simple wrapper around coroutine"""
    task_id = 0
    def __init__(self, target):
        Task.task_id += 1
        self.tid = Task.task_id
        self.target = target
        self.value_to_send = None

    def run(self):
        return self.target.send(self.value_to_send)