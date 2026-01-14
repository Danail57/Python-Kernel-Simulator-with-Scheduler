from kernel_simulator.simulator.kernel import KernelSimulator
from kernel_simulator.simulator import syscall


kernel = KernelSimulator()

pid1 = kernel.create_process("Process 1")
pid2 = kernel.create_process("Process 2")
pid3 = kernel.create_process("Process 3")

kernel.allocate_memory(pid1, 10)
kernel.allocate_memory(pid2, 5)
kernel.allocate_memory(pid3, 8)

kernel.list_processes()

syscall.write(pid1, "Hello World")
syscall.read(pid2)
kernel.run_scheduler(cycles=2, time_slice=0.2)

kernel.free_memory(pid1)
kernel.kill_process(pid2)

kernel.list_processes()