def generate_permutations(n):
    if n == 1:
        return [[1]]

    permutations = generate_permutations(n - 1)
    result = []
    for perm in permutations:
        for i in range(n):
            new = perm[i:] + [n] + perm[:i]
            result.append(new)
    return result

result = generate_permutations(3)
print(result)

