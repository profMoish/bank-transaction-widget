from datetime import datetime


def log(_func=None, filename: str = ""):
    """ Decorator for logging functions """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            try:
                result = func(*args, **kwargs)
                msg = f"{func.__name__} ok\nResult: {result}\n"

            except Exception as e:
                result = None
                msg = f"{func.__name__} error: {e}\nInputs: {args} {kwargs}\n"

            msg += f'Start: {start}\nEnd: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}\n\n'

            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(msg)
            else:
                print()
                print(msg)
            return result

        return wrapper

    if _func is None:
        return decorator
    return decorator(_func)
