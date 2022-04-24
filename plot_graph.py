from memory_profiler import memory_usage
from cProfile import label
import basic3
import efficient3
import glob
import re
import os
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    files = glob.glob(os.path.join('*.txt'))
    files.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])
    time_list = []
    time_list_efficient = []
    mem_list = []
    mem_list_efficient = []
    problem_size = []
    for infile in files:
        # problem size vs time basic
        s = basic3.SequenceAlignment()
        str1, str2 = basic3.generateStringWithInputFile(infile)
        size = len(str1) + len(str2)

        start_time = time.time()
        str1, str2 = s.basicProcessing(str1,str2)
        end_time = time.time()
        time_taken = (end_time - start_time)
        cost = s.calculateScoreAfterProcessing(str1, str2)
        mem = s.process_memory()
        mem_list.append(mem)
        problem_size.append(size)
        time_list.append(time_taken * 1000)
        del s
        # problem size vs time efficient
        s = efficient3.SequenceAlignment()
        str1, str2 = efficient3.generateStringWithInputFile(infile)
        size = len(str1) + len(str2)
        start_time = time.time()
        str1, str2 = s.efficientProcessing(str1,str2)
        end_time = time.time()
        time_taken = (end_time - start_time)
        cost = s.calculateScoreAfterProcessing(str1, str2)
        mem = s.process_memory()
        mem_list_efficient.append(mem)
        time_list_efficient.append(time_taken * 1000)
        del s

    plt.plot(problem_size, time_list, label="basic_algo")
    plt.plot(problem_size, time_list_efficient, label="efficient_algo")
    plt.xlabel("problem_size (M + N)")
    plt.ylabel("time (ms)")
    plt.title("Problem_size vs Time")
    plt.legend()
    plt.show()

    plt.plot(problem_size, mem_list, label="basic_algo")
    plt.plot(problem_size, mem_list_efficient, label="efficient_algo")
    plt.xlabel("problem_size (M + N)")
    plt.ylabel("memory_usage (KB)")
    plt.title("Problem_size vs Memory")
    plt.legend()
    plt.show()