def reconstruct_trip(tickets):
    hash_table = {ticket[0]: ticket[1] for ticket in tickets}
    trip = [''] * (len(tickets)-1)
    for ticket in tickets:
        hash_table[ticket[0]] = ticket[1]
        if ticket[0] is None:
            trip[0] = ticket[1]
    for i in range(1, len(trip)):
        if trip[i-1] in hash_table:
            trip[i] = hash_table[trip[i-1]]
        else:
            return []
    return trip


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
