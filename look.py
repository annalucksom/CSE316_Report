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

    if direction == "left":
        sequence = left[::-1] + right
    else:
        sequence = right + left[::-1]

    for req in sequence:
        seek_time += abs(head - req)
        head = req
        seek_sequence.append(head)

    print("\nLOOK Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)

if _name_ == "_main_":
    requests = list(map(int, input("Enter disk requests separated by spaces: ").split()))
    head = int(input("Enter the initial head position: "))
    direction = input("Enter direction (left/right): ").strip().lower()
    look(requests, head, direction)
