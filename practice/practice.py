# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def practice():
    # read in the file, store as string, split into list of numbers
    with open('input.txt', 'r') as file:
        data = file.read().rstrip()
    numbers = [int(i) for i in data]

    print(len(numbers))

    # loop through the list, compare each number to the next number
    # if they are the same, add to the sum
    total = 0
    for i in range(len(numbers)):
        if numbers[i] == numbers[(i + 1) % len(numbers)]:
            total += numbers[i]

    print(total)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    practice()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
