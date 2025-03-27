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

if _name_ == "_main_":
    requests = list(map(int, input("Enter disk requests separated by spaces: ").split()))
    head = int(input("Enter the initial head position: "))
    c_look(requests, head)
