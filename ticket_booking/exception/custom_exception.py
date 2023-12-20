class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


if __name__ == "__main__":
    try:
        raise CustomException("This is a custom exception.")
    except CustomException as e:
        print(f"Caught custom exception: {e}")
