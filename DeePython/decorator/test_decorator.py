from DeePython.decorator import log_start_end_time, log_func_with_args


@log_start_end_time
def foo():
    print('func execute')


@log_func_with_args
def bar(content):
    print(content)


if __name__ == '__main__':
    foo()

    bar('func with args execute')
