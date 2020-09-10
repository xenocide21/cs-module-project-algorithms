'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, jar=None):
    # Your code here
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif jar and jar[n] > 0:
        return jar[n]
    else:
        if not jar:
            jar = [0 for _ in range(n + 1)]
        jar[n] = eating_cookies(n - 1, jar) + eating_cookies(n - 2, jar) + eating_cookies(n - 3, jar)
    return jar[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
