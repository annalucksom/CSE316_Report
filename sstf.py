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

if _name_ == "_main_":
    requests = list(map(int, input("Enter disk requests separated by spaces: ").split()))
    head = int(input("Enter the initial head position: "))
    sstf(requests, head)
