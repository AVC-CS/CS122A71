def getFarNumber(numbers):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    avg = sum(numbers) / len(numbers)
    deviations = [abs(x - avg) for x in numbers]
    max_deviation = max(deviations)
    max_index = deviations.index(max_deviation)
    return numbers[max_index]

def main():
    numbers = [10, 5, 20, 0, 40, 45, 50, 55, 9, 10]
    print(f'\n################ Test 1 ########################')
    print(f'Original numbers: {numbers}')
    ret = getFarNumber(numbers)
    print(f'Your return value is {ret}, expected value is 55')

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]
    print(f'\n################ Test 2 ########################')
    print(f'Original numbers: {numbers}')
    ret = getFarNumber(numbers)
    print(f'Your return value is {ret}, expected value is 20')

if __name__ == '__main__':
    main()
