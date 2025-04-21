def fcfs(requests, head):
    seek_time = 0
    seek_sequence = [head]
    for req in requests:
        seek_time += abs(head - req)
        head = req
        seek_sequence.append(head)
    print("\nFCFS Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)

def sstf(requests, head):
    seek_time = 0
    seek_sequence = [head]
    requests = requests[:]
    while requests:
        closest = min(requests, key=lambda x: abs(x - head))
        seek_time += abs(head - closest)
        head = closest
        seek_sequence.append(head)
        requests.remove(closest)
    print("\nSSTF Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)

def scan(requests, head, disk_size, direction="left"):
    seek_time = 0
    left, right = [], []
    for req in requests:
        if req < head:
            left.append(req)
        else:
            right.append(req)
    left.append(0)
    left.sort()
    right.sort()
    seek_sequence = [head]
    sequence = left[::-1] + right if direction == "left" else right + left[::-1]
    for req in sequence:
        seek_time += abs(head - req)
        head = req
        seek_sequence.append(head)
    print("\nSCAN Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)

def c_scan(requests, head, disk_size):
    seek_time = 0
    left, right = [], []
    for req in requests:
        if req >= head:
            right.append(req)
        else:
            left.append(req)
    right.sort()
    left.sort()
    seek_sequence = [head] + right + [disk_size] + [0] + left
    for i in range(1, len(seek_sequence)):
        seek_time += abs(seek_sequence[i] - seek_sequence[i - 1])
    print("\nC-SCAN Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)

def look(requests, head, direction="left"):
    seek_time = 0
    left, right = [], []
    for req in requests:
        if req < head:
            left.append(req)
        else:
            right.append(req)
    left.sort()
    right.sort()
    seek_sequence = [head]
    sequence = left[::-1] + right if direction == "left" else right + left[::-1]
    for req in sequence:
        seek_time += abs(head - req)
        head = req
        seek_sequence.append(head)
    print("\nLOOK Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)

def c_look(requests, head):
    seek_time = 0
    left, right = [], []
    for req in requests:
        if req >= head:
            right.append(req)
        else:
            left.append(req)
    right.sort()
    left.sort()
    seek_sequence = [head] + right + left
    for i in range(1, len(seek_sequence)):
        seek_time += abs(seek_sequence[i] - seek_sequence[i - 1])
    print("\nC-LOOK Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)

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
