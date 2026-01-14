class MemoryManager:
    def __init__(self, size = 100):
        self.memory = [0] * size

    def allocate(self, pid, size):
        free_blocks = [i for i, v in enumerate(self.memory) if v == 0]
        if len(free_blocks) < size:
            print(f"Not enough memory for process: {pid}")
            return False

        for i in free_blocks[:size]:
            self.memory[i] = pid
        print(f"Allocated {size} memory blocks for process: {pid}")
        return True

    def free(self, pid):
        for i in range(len(self.memory)):
            if self.memory[i] == pid:
                self.memory[i] = 0
        print(f"Free {pid} memory blocks for process: {pid}")

    def dump(self):
        print("memory state: ")
        print(self.memory)