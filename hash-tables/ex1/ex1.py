def get_indices_of_item_weights(weights, limit):
    hash_table = {}
    for i in range(len(weights)):
        weight = weights[i]
        if (limit - weight) in hash_table:
            return (i, hash_table[(limit - weight)])
        else:
            hash_table[weight] = i
    return ()


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
