class TaskHelper():
    def __init__(self, value, index):
        self.value = value
        self.index = index

def taskAssignment(k, tasks):
    task_helpers = []
    res = []
    for index, task in enumerate(tasks):
        task_helpers.append(TaskHelper(task, index))

    task_helpers.sort(key = lambda task: task.value)

    n = 2 * k - 1
    for i in range(k):
        res.append([task_helpers[i].index, task_helpers[n - i].index])

    return res