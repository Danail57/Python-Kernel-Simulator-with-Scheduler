from .process import Process
from .scheduler import RoundRobinScheduler
from . import syscall
from .memory_manager import MemoryManager

class KernelSimulator:
    def __init__(self):
        self.process_table = {}
        self.next_pid = 1
        self.scheduler = RoundRobinScheduler()
        self.memory_manager = MemoryManager()

    def create_process(self, name):
        pid = self.next_pid
        self.next_pid += 1
        process = Process(pid, name)
        self.process_table[pid] = process
        print(f"Created process {pid}: {name}")
        return pid

    def kill_process(self, pid):
        if pid in self.process_table:
            self.memory_manager.free(pid)
            print(f"Killing process {pid} ({self.process_table[pid].name})")
            del self.process_table[pid]

    def list_processes(self):
        print("PID\tName\tState")
        for pid, process in self.process_table.items():
            print(f"{pid}\t{process.name}\t{process.state}")

    def allocate_memory(self, pid, size):
        return self.memory_manager.allocate(pid, size)

    def free_memory(self, pid):
        self.memory_manager.free(pid)

    def block_process(self, pid):
        self.process_table[pid].block()

    def unblock_process(self, pid):
        self.process_table[pid].unblock()

    def block_memory(self, pid, size):
        return self.memory_manager.allocate(pid, size)

    def run_scheduler(self, cycles = 3, time_slice = 0.2):
        self.scheduler.schedule(self.process_table, cycles, time_slice)