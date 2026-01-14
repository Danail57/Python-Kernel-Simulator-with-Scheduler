from abc import ABC, abstractmethod

class AbstractScheduler(ABC):
    @abstractmethod
    def schedule(self, process_table, cycles, time_slice):
        pass

class RoundRobinScheduler(AbstractScheduler):
    def schedule(self, process_table, cycles = 3, time_slice = 0.2):
        if not process_table:
            print("No processes to schedule")
            return
        print("Scheduler started")
        for _ in range(cycles):
            for pid, process in process_table.items():
                if process.state == "ready":
                    process.run(time_slice)
        print("Scheduler finished")