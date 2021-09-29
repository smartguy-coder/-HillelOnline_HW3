import os

from work_module import result_output

# in some IDE like VS Code current working directory can be anywhere
# so we must handle it
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def run_test():
    run_times = int(input('\033[1;31mInput the number of tests you want to run (int, > 0) --> \033[0m'))

    for _ in range(run_times):
        print(f"test №{_ + 1} started {'*' * 50}")
        result_output()
        print('\n'+f"test №{_+1} completed {'*'*48}", end='\n\n')
    print("ALL TESTS COMPLETED")
        

if __name__ == "__main__":
    run_test()

