class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def generate_exception(value):
    if value < 0:
        raise InvalidDataException("Invalid data: value should be non-negative")
    elif value == 0:
        raise ProcessingException("Processing error: value is zero")
    else:
        return value


def main():
    try:
        result = generate_exception(-1)
        print("Returned value:", result)
    except InvalidDataException as e:
        print("Error occurred:", e)
    except ProcessingException as e:
        print("Error occurred:", e)

    try:
        result = generate_exception(0)
        print("Returned value:", result)
    except InvalidDataException as e:
        print("Error occurred:", e)
    except ProcessingException as e:
        print("Error occurred:", e)

    try:
        result = generate_exception(5)
        print("Returned value:", result)
    except InvalidDataException as e:
        print("Error occurred:", e)
    except ProcessingException as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    main()
