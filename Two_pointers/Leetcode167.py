def twoSum(numbers, target):
    left = 0 
    right = len(numbers) - 1
    while left < right:
        current  = numbers[right] + numbers[left]
        if current == target:
            return [left,right]
        elif current < target:
            left += 1
        else:
            right -= 1


def main():
    numbers = [2, 7, 11, 15]
    target = 9

    result = twoSum(numbers, target)

    print("Numbers:", numbers)
    print("Target:", target)
    print("Result:", result)


if __name__ == "__main__":
    main()