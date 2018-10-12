def get_indices_of_item_weights(weights, limit):
    hash_table = {weight: weights.index(weight) for weight in weights}
    for weight in hash_table:
        weight2 = limit - weight
        if weight2 in hash_table.keys():
            return tuple([hash_table[weight], hash_table[weight2]])

    return tuple()


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass
