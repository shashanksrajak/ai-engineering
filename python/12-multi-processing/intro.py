from time import perf_counter, time, sleep
from multiprocessing import Process, cpu_count

def square(num):
    sleep(1)
    return num*num

def calc_sqaure(nums):
    squares_nums = [square(num) for num in nums]
    print(squares_nums)

def cube(num):
    sleep(1)
    return num*num*num

def calc_cubes(nums):
    cubes_nums = [cube(num) for num in nums]
    print(cubes_nums)


def sleeping():
    sleep(30)

def sequential_example():
    nums = [i for i in range(51)]

    time_start = perf_counter()
    calc_sqaure(nums)
    calc_cubes(nums)
    time_end = perf_counter()
    print("Total time taken: ", time_end - time_start)


def multi_processing_example():
    nums = [i for i in range(51)]

    time_start = perf_counter()
    # create a new process
    process_sqaure = Process(target=calc_sqaure, args=(nums,))
    process_cube = Process(target=calc_cubes, args=(nums,))

    # start the new process
    process_sqaure.start()
    process_cube.start()
    

    process_sqaure.join()
    process_cube.join()

    time_end = perf_counter()

    print("Total time taken: ", time_end - time_start)


    # we can check if process is running
    # if new_process.is_alive():
    #     print("Process is running", new_process.pid)
        


if __name__ == "__main__":
    print(f"CPU count in this system is : {cpu_count()}")

    sequential_example()

    # multi_processing_example()
