def nfruits(d, pattern):
    # Throw an error if my assumptions are not met
    assert len(d) > 0 and len(d) < 10, "The elements are not right"
    assert len(pattern) > 0, "He didn't eat any fruit"
    # Otherwise reduce fruit count for every element in the pattern except the last one
    # because he will not buy anymore fruits after that
    for i in pattern[:-1]:
        # Eat the fruit thus reduce the count
        d[i] -= 1
        # Post assert that he didn't actually eat a fruit he no more has
        assert d[i] >= 0, "He ran out of the fruit"
        # Buy each type of fruit except the one eaten
        for key, value in d.items():
            if i != key:
                d[key] += 1
    # Eat the last fruit but don't buy anymore            
    d[pattern[-1]] -= 1            
    return max(d.values())

# Test
print nfruits({'H': 7, 'S': 6, 'P': 8, 'W': 8, 'X': 7}, 'PSW')
