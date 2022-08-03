def dna_min(s, p, q):
    ref = {'a': 1, 'c': 2, 'g': 3, 't': 4}
    zipped = list(zip(p, q))
    # print(zipped)

    final = []
    for pair in zipped:
        covered = s[pair[0]:(pair[1] + 1)]
        covered_list = [x for x in covered]
        values = []
        for char in covered_list:
            for key in ref:
                if char == key:
                    values.append(ref[key])
        final.append(min(values))

    return final


print(dna_min('cagccta', [2, 5, 0], [4, 5, 6]))
