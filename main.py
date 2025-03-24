from fcfs import fcfs
from sstf import sstf
from scan import scan
from c_scan import c_scan
from look import look
from c_look import c_look

def main():
    requests = list(map(int, input("Enter disk requests separated by spaces: ").split()))
    head = int(input("Enter the initial head position: "))
    disk_size = int(input("Enter disk size (for SCAN & C-SCAN): "))

    print("\n--- Disk Scheduling Algorithms ---")
    fcfs(requests, head)
    sstf(requests, head)
    scan(requests, head, disk_size, "left")
    c_scan(requests, head, disk_size)
    look(requests, head, "left")
    c_look(requests, head)

if __name__ == "__main__":
    main()
