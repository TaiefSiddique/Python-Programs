def priority_scheduling():
    print("Priority Scheduling Algorithm")

    n = int(input("Enter the number of processes: "))
    burst_time = []
    priority = []
    waiting_time = [0] * n
    turnaround_time = [0] * n
    process_number = list(range(1, n + 1))

    for i in range(n):
        bt = int(input(f"Enter the burst time for process {i + 1}: "))
        burst_time.append(bt)
        pr = int(input(f"Enter the priority for process {i + 1}: "))
        priority.append(pr)

    # Sort processes by priority, and in case of a tie, by burst time
    for i in range(n):
        for j in range(i + 1, n):
            if priority[i] > priority[j] or (priority[i] == priority[j] and burst_time[i] > burst_time[j]):
                priority[i], priority[j] = priority[j], priority[i]
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
                process_number[i], process_number[j] = process_number[j], process_number[i]

    # Calculate waiting and turnaround times
    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    # Print the results in the original order
    print("Process | Burst Time | Priority | Waiting Time | Turnaround Time")
    print("------- | ---------- | -------- | ------------ | --------------")
    for i in range(n):
        print(f"P{process_number[i]} | {burst_time[i]} | {priority[i]} | {waiting_time[i]} | {turnaround_time[i]}")

    # Calculate the average waiting time and turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


def sjf_scheduling():
    print("SJF Scheduling Algorithm")

    n = int(input("Enter the number of processes: "))
    burst_time = []
    waiting_time = [0] * n
    turnaround_time = [0] * n
    process_number = list(range(1, n + 1))

    for i in range(n):
        bt = int(input(f"Enter the burst time for process {i + 1}: "))
        burst_time.append(bt)

    # Sort processes by burst time
    for i in range(n):
        for j in range(i + 1, n):
            if burst_time[i] > burst_time[j]:
                burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
                process_number[i], process_number[j] = process_number[j], process_number[i]

    # Calculate waiting and turnaround times
    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    # Print the results in the original order
    print("Process | Burst Time | Waiting Time | Turnaround Time")
    print("------- | ---------- | ------------ | --------------")
    for i in range(n):
        print(f"P{process_number[i]} | {burst_time[i]} | {waiting_time[i]} | {turnaround_time[i]}")

    # Calculate the average waiting time and turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


def fcfs_scheduling():
    print("FCFS Scheduling Algorithm")

    n = int(input("Enter the number of processes: "))
    burst_time = []
    waiting_time = [0] * n
    turnaround_time = [0] * n
    process_number = list(range(1, n + 1))

    for i in range(n):
        bt = int(input(f"Enter the burst time for process {i + 1}: "))
        burst_time.append(bt)

    # Calculate waiting and turnaround times
    waiting_time[0] = 0
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    # Print the results in the original order
    print("Process | Burst Time | Waiting Time | Turnaround Time")
    print("------- | ---------- | ------------ | --------------")
    for i in range(n):
        print(f"P{process_number[i]} | {burst_time[i]} | {waiting_time[i]} | {turnaround_time[i]}")

    # Calculate the average waiting time and turnaround time
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


def fifo_page_replacement():
    print("FIFO Page Replacement Algorithm")

    frames = int(input("Enter the number of frames: "))
    pages = int(input("Enter the number of pages: "))
    page_array = []

    for i in range(1, pages + 1):
        page = int(input(f"Enter the page number for reference {i}: "))
        page_array.append(page)

    fifo_replace = [-1] * frames
    page_faults = 0

    for i in range(pages):
        page_number = page_array[i]
        page_found = False

        for j in range(frames):
            if fifo_replace[j] == page_number:
                page_found = True
                break

        if not page_found:
            replace_index = i % frames
            fifo_replace[replace_index] = page_number
            page_faults += 1

    print(f"Page Faults using FIFO: {page_faults}")


def lru_page_replacement():
    print("LRU Page Replacement Algorithm")

    frames = int(input("Enter the number of frames: "))
    pages = int(input("Enter the number of pages: "))
    page_array = []

    for i in range(1, pages + 1):
        page = int(input(f"Enter the page number for reference {i}: "))
        page_array.append(page)

    lru_replace = [-1] * frames
    page_faults = 0

    for i in range(pages):
        page_number = page_array[i]
        page_found = False

        for j in range(frames):
            if lru_replace[j] == page_number:
                page_found = True
                del lru_replace[j]
                lru_replace.append(page_number)
                break

        if not page_found:
            if len(lru_replace) == frames:
                del lru_replace[0]
                lru_replace.append(page_number)
                page_faults += 1
            else:
                lru_replace.append(page_number)
                page_faults += 1

    print(f"Page Faults using LRU: {page_faults}")


def lfu_page_replacement():
    print("LFU Page Replacement Algorithm")

    frames = int(input("Enter the number of frames: "))
    pages = int(input("Enter the number of pages: "))
    page_array = []

    for i in range(1, pages + 1):
        page = int(input(f"Enter the page number for reference {i}: "))
        page_array.append(page)

    lfu_count = [0] * frames
    lfu_replace = [-1] * frames
    page_faults = 0

    for i in range(pages):
        page_number = page_array[i]
        page_found = False

        for j in range(frames):
            if lfu_replace[j] == page_number:
                page_found = True
                lfu_count[j] += 1
                break

        if not page_found:
            replace_index = 0
            min_count = lfu_count[0]

            for j in range(1, frames):
                if lfu_count[j] < min_count:
                    min_count = lfu_count[j]
                    replace_index = j

            lfu_replace[replace_index] = page_number
            lfu_count[replace_index] = 1
            page_faults += 1

    print(f"Page Faults using LFU: {page_faults}")


def opr_page_replacement():
    print("OPR (Optimal Page Replacement) Algorithm")

    frames = int(input("Enter the number of frames: "))
    pages = int(input("Enter the number of pages: "))
    page_array = []

    for i in range(1, pages + 1):
        page = int(input(f"Enter the page number for reference {i}: "))
        page_array.append(page)

    opr_replace = [-1] * frames
    page_faults = 0

    for i in range(pages):
        page_number = page_array[i]
        page_found = False

        for j in range(frames):
            if opr_replace[j] == page_number:
                page_found = True
                break

        if not page_found:
            if len(opr_replace) == frames:
                max_future_distance = -1
                replace_index = 0

                for j in range(frames):
                    current_page = opr_replace[j]
                    future_distance = page_array[i:].index(current_page) if current_page in page_array[i:] else -1

                    if future_distance == -1:
                        replace_index = j
                        break

                    if future_distance > max_future_distance:
                        max_future_distance = future_distance
                        replace_index = j

                opr_replace[replace_index] = page_number
                page_faults += 1
            else:
                opr_replace.append(page_number)
                page_faults += 1

    print(f"Page Faults using OPR: {page_faults}")


def first_fit_contiguous_allocation():
    print("First Fit Contiguous Memory Allocation Algorithm")

    total_memory = int(input("Enter the total memory size: "))
    num_processes = int(input("Enter the number of processes: "))
    process_sizes = []

    for i in range(1, num_processes + 1):
        size = int(input(f"Enter the size of process {i}: "))
        process_sizes.append(size)

    current_position = 0
    allocated_blocks = []

    for i in range(num_processes):
        if current_position + process_sizes[i] <= total_memory:
            allocated_blocks.append(current_position)
            current_position += process_sizes[i]
            print(f"Process {i + 1} allocated at position {current_position}")
        else:
            print(f"Insufficient memory for Process {i + 1}")


def best_fit_contiguous_allocation():
    print("Best Fit Contiguous Memory Allocation Algorithm")

    total_memory = int(input("Enter the total memory size: "))
    num_processes = int(input("Enter the number of processes: "))
    process_sizes = []

    for i in range(1, num_processes + 1):
        size = int(input(f"Enter the size of process {i}: "))
        process_sizes.append(size)

    allocated_blocks = []

    for i in range(num_processes):
        best_fit = -1
        best_fit_index = -1

        for j in range(len(allocated_blocks)):
            if allocated_blocks[j] >= process_sizes[i]:
                if best_fit == -1 or allocated_blocks[j] < best_fit:
                    best_fit = allocated_blocks[j]
                    best_fit_index = j

        if best_fit_index != -1:
            allocated_blocks[best_fit_index] -= process_sizes[i]
            print(f"Process {i + 1} allocated at position {best_fit}")
        else:
            print(f"Insufficient memory for Process {i + 1}")


def worst_fit_contiguous_allocation():
    print("Worst Fit Contiguous Memory Allocation Algorithm")

    total_memory = int(input("Enter the total memory size: "))
    num_processes = int(input("Enter the number of processes: "))
    process_sizes = []

    for i in range(1, num_processes + 1):
        size = int(input(f"Enter the size of process {i}: "))
        process_sizes.append(size)

    allocated_blocks = []

    for i in range(num_processes):
        worst_fit = -1
        worst_fit_index = -1

        for j in range(len(allocated_blocks)):
            if allocated_blocks[j] >= process_sizes[i]:
                if worst_fit == -1 or allocated_blocks[j] > worst_fit:
                    worst_fit = allocated_blocks[j]
                    worst_fit_index = j

        if worst_fit_index != -1:
            allocated_blocks[best_fit_index] -= process_sizes[i]
            print(f"Process {i + 1} allocated at position {worst_fit}")
        else:
            print(f"Insufficient memory for Process {i + 1}")


def next_fit_contiguous_allocation():
    print("Next Fit Contiguous Memory Allocation Algorithm")

    total_memory = int(input("Enter the total memory size: "))
    num_processes = int(input("Enter the number of processes: "))
    process_sizes = []

    for i in range(1, num_processes + 1):
        size = int(input(f"Enter the size of process {i}: "))
        process_sizes.append(size)

    current_position = 0
    allocated_blocks = []

    for i in range(num_processes):
        if current_position + process_sizes[i] <= total_memory:
            allocated_blocks.append(current_position)
            current_position += process_sizes[i]
            print(f"Process {i + 1} allocated at position {current_position}")
        else:
            print(f"Insufficient memory for Process {i + 1}")


def contiguous_allocation_with_paging():
    print("Contiguous Memory Allocation with Paging Algorithm")

    total_memory = int(input("Enter the total memory size: "))
    page_size = int(input("Enter the page size: "))
    num_processes = int(input("Enter the number of processes: "))
    process_sizes = []

    for i in range(1, num_processes + 1):
        size = int(input(f"Enter the size of process {i}: "))
        process_sizes.append(size)

    pages_per_process = [size // page_size for size in process_sizes]
    total_frames = total_memory // page_size
    allocated_frames = []

    for i in range(num_processes):
        if total_frames >= pages_per_process[i]:
            allocated_frames.append(pages_per_process[i])
            total_frames -= pages_per_process[i]
            print(f"Process {i + 1} allocated {pages_per_process[i]} frames")
        else:
            print(f"Insufficient memory for Process {i + 1}")


def main():
    while True:
        print("\nOperating System Services Simulation Using Python")
        print("1. CPU Scheduling Algorithms")
        print("2. Page Replacement Algorithms")
        print("3. Contiguous Memory Allocation Algorithms")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            while True:
                print("\nCPU Scheduling Algorithms")
                print("1. Priority Scheduling")
                print("2. SJF Scheduling")
                print("3. FCFS Scheduling")
                print("4. Back to Main Menu")

                cpu_choice = int(input("Enter your choice (1-4): "))

                if cpu_choice == 1:
                    priority_scheduling()
                elif cpu_choice == 2:
                    sjf_scheduling()
                elif cpu_choice == 3:
                    fcfs_scheduling()
                elif cpu_choice == 4:
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif choice == 2:
            while True:
                print("\nPage Replacement Algorithms")
                print("1. FIFO")
                print("2. LRU")
                print("3. LFU")
                print("4. OPR")
                print("5. Back to Main Menu")

                page_choice = int(input("Enter your choice (1-5): "))

                if page_choice == 1:
                    fifo_page_replacement()
                elif page_choice == 2:
                    lru_page_replacement()
                elif page_choice == 3:
                    lfu_page_replacement()
                elif page_choice == 4:
                    opr_page_replacement()
                elif page_choice == 5:
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif choice == 3:
            while True:
                print("\nContiguous Memory Allocation Algorithms")
                print("1. First Fit")
                print("2. Best Fit")
                print("3. Worst Fit")
                print("4. Next Fit")
                print("5. Contiguous Memory Allocation with Paging")
                print("6. Back to Main Menu")

                mem_choice = int(input("Enter your choice (1-6): "))

                if mem_choice == 1:
                    first_fit_contiguous_allocation()
                elif mem_choice == 2:
                    best_fit_contiguous_allocation()
                elif mem_choice == 3:
                    worst_fit_contiguous_allocation()
                elif mem_choice == 4:
                    next_fit_contiguous_allocation()
                elif mem_choice == 5:
                    contiguous_allocation_with_paging()
                elif mem_choice == 6:
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif choice == 4:
            print("Exiting the simulation. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
