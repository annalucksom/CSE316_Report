def fcfs(requests, head):
    seek_time = 0
    seek_sequence = [head]
    
    for req in requests:
        seek_time += abs(head - req)
        head = req
        seek_sequence.append(head)
    
    print("\nFCFS Seek Sequence:", " → ".join(map(str, seek_sequence)))
    print("Total Seek Time:", seek_time)
