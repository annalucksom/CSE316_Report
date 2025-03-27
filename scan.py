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

    if direction == "left":
        sequence = left[::-1] + right
    else:
        sequence = right + left[::-1]

    for req in sequence:
        seek_time += abs(head - req)
        head = req
        seek_sequence.append(head)

    print("\nSCAN Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)

if _name_ == "_main_":
    requests = list(map(int, input("Enter disk requests separated by spaces: ").split()))
    head = int(input("Enter the initial head position: "))
    disk_size = int(input("Enter the disk size: "))
    direction = input("Enter the initial direction (left/right): ").strip().lower()
    scan(requests, head, disk_size, direction)
