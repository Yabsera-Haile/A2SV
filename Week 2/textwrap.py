import textwrap


def wrap(string, max_width):
    result = ""
    for i in range(len(string)//max_width+1):
        current = i*max_width
        result += string[current:current+max_width]+"\n"

    return result


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
