from my_module.operations import do_add

def main():
    inputs = [
        '4 5',
        '10 20',
        '0 0',
        '-1 -2',
        '4',
        '4 5 6',
        '',
        'four five',
        '4 five',
        'five 5',
        '2147483647 1',
        '-2147483648 -1',
        '   '
    ]

    for input_str in inputs:
        result = do_add(None, input_str)
        if result is not None:
            print(f"Result of '{input_str}': {result}")
        else:
            print(f"Invalid input: '{input_str}'")

if __name__ == "__main__":
    main()