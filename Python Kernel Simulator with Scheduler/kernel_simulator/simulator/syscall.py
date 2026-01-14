def read(pid):
    print(f"Process {pid} is performing syscall")

def write(pid, data):
    print(f"Process {pid} is performing write syscall: {data}")