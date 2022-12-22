def swap_case(s):
    result = ""
    for letter in s:
        result += letter.swapcase()
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
