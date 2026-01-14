from abc import ABC, abstractmethod
import time, random

class AbstractProcess(ABC):
    def __init__(self, pid, name):
        self.name = name
        self.pid = pid
        self.state = "ready"

    @abstractmethod
    def run(self):
        pass

class Process(AbstractProcess):
    def run(self, time_slice = 0.2):
        self.state = "running"
        print(f"Process {self.pid} started at {self.state} is running...")
        time.sleep(random.uniform(0, time_slice))
        self.state = "ready"

    def block(self):
        self.state = "blocked"
        print(f"Process {self.pid} blocked at {self.state} is blocking...")

    def unblock(self):
        self.state = "unblocked"
        print(f"Process {self.pid} unblocked at {self.state} is unblocking...")