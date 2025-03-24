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

    # C-SCAN moves in one direction, reaching the disk end, then jumps to start
    seek_sequence = [head] + right + [disk_size] + [0] + left

    for i in range(1, len(seek_sequence)):
        seek_time += abs(seek_sequence[i] - seek_sequence[i - 1])

    print("\nC-SCAN Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)

# Example usage (Remove this if using main.py to import the function)
if _name_ == "_main_":
    requests = list(map(int, input("Enter disk requests separated by spaces: ").split()))
    head = int(input("Enter the initial head position: "))
    disk_size = int(input("Enter the disk size: "))
    c_scan(requests, head, disk_size)
