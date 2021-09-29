from time import time
from datetime import datetime
import os

# in some IDE like VS Code current working directory can be anywhere
# so we must handle it
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def my_generator():
    start_point = input("Enter the start point for printing --> ")
    end_point = input("Enter the end point for printing --> ")

    if all([start_point.isdigit(), end_point.isdigit()]):
        start_point = int(start_point)
        end_point = int(end_point)

        if start_point < end_point:
            cursor = start_point

            while cursor < end_point:
                yield cursor
                cursor += 1
        else:
            raise ValueError

    else:
        raise TypeError
    

class CustomTimerContexManager:
    def __init__(self, name: str = 'HW3', flags='a+'):
        self.my_file = open(f'{name}.csv', flags)

    def __enter__(self):
        self.starttime = time()
        return self.my_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        running_time = time()-self.starttime
        base_str = f'Time the script was executed:;{datetime.now()};Execution time (sec):;{running_time};status:;'

        if exc_type is None:
            self.my_file.write(f'{base_str}success' + '\n')
        elif exc_type is ValueError:
            self.my_file.write(f'{base_str}Error: start must be lover then end' + '\n')
        elif exc_type is TypeError:
            self.my_file.write(f'{base_str}Error: start and end must be integer' + '\n')
        else:
            self.my_file.write(f'{base_str}Error: there was unexpected error (like exit code 130 or \
            137 (interrupted by signal 2 or 9: SIGKILL) -> KeyboardInterrupt)' + '\n')

        self.my_file.close()

        ''' if function returns False (or without return at all), than processing is transferred to the \
        highest level and errors can destroy the running of the program. In case if it returns True \
        we do not transfer errors to another level \
        here we are catching KeyboardInterrupt'''
        return True


def result_output():
    with CustomTimerContexManager():
        for _ in my_generator():
            print(_)


if __name__ == "__main__":
    print('work module')
