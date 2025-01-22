import heapq

class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority > other.priority  # Max-heap based on priority

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        heapq.heappush(self.heap, task)

    def extract_max(self):
        return heapq.heappop(self.heap) if not self.is_empty() else None

    def increase_key(self, task_id, new_priority):
        for i, task in enumerate(self.heap):
            if task.task_id == task_id:
                self.heap[i].priority = new_priority
                heapq.heapify(self.heap)
                break

    def is_empty(self):
        return len(self.heap) == 0

# Example Usage
if __name__ == "__main__":
    pq = PriorityQueue()

    tasks = [
        Task(task_id=1, priority=5, arrival_time=0, deadline=10),
        Task(task_id=2, priority=3, arrival_time=2, deadline=8),
        Task(task_id=3, priority=8, arrival_time=1, deadline=7)
    ]

    for task in tasks:
        pq.insert(task)

    print("Tasks in Priority Queue:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Task ID: {task.task_id}, Priority: {task.priority}")