import sys
import time
import psutil

def genString(string, nums):
    for num in nums:
        string = string[:num+1]+string+string[num+1:]
        #print(string)
    return string



# readfile part
def generateStringWithInputFile(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        input_str = ""
        str1 = ""
        str2 = ""
        nums = []
        for line in lines:
            try:
                num = int(line)
                nums.append(num)
            except ValueError:
                if input_str == "":
                    input_str = line.rstrip('\n') 
                else:
                    str1 = genString(input_str,nums)
                    nums = []
                    input_str = line.rstrip('\n') 
        str2 = genString(input_str,nums)
    
    return str1, str2


class SequenceAlignment:
    # default parameter
    delta = 30
    alpha = [[0,110,48,94],[110,0,118,48],[48,118,0,110],[94,48,110,0]]
    h = {'A': 0, 'C': 1 , 'G': 2,'T': 3}
    
    def __init__(self):
        pass
    
    def process_memory(self):
        process = psutil.Process()
        memory_info = process.memory_info()
        memory_consumed = int(memory_info.rss/1024)
        return memory_consumed

    def calculateScoreAfterProcessing(self, *args):
        if len(args) == 1 and isinstance(args[0], tuple):
            str1 = args[0][0]
            str2 = args[0][1]
        if len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
            str1 = args[0]
            str2 = args[1]
        if len(str1) != len(str2):
            print("Cannot compare two string with differnet length\n")
        score = 0
        for i in range(len(str1)):
            if str1[i] == '_' or str2[i]== '_':
                score += self.delta
            else:
                score += self.alpha[self.h[str1[i]]][self.h[str2[i]]]
        return score
    
    # 2-d array dynamic porgramming 
    def basicProcessing(self, str1, str2):
        size_str1 = len(str1)
        size_str2 = len(str2)
        dp = [[0]*(size_str2+1) for _ in range(size_str1+1)]
        for i in range(size_str1+1):
            dp[i][0] =  self.delta * i
        for i in range(size_str2+1):
            dp[0][i] =  self.delta * i
        for i in range(1,size_str1+1):
            for j in range(1,size_str2+1):
                dp[i][j] = min(dp[i][j-1] + self.delta,
                                dp[i-1][j] + self.delta,
                                dp[i-1][j-1] + self.alpha[self.h[str1[i-1]]][self.h[str2[j-1]]])
                
        #print(dp[size_str1][size_str2])
        
        i = size_str1
        j = size_str2
        while not(i == 0 or j == 0):
            if dp[i][j] == dp[i-1][j-1] + self.alpha[self.h[str1[i-1]]][self.h[str2[j-1]]]:
                i-=1
                j-=1
            elif dp[i][j] == dp[i][j-1] + self.delta:
                str1 = str1[:i] + '_' + str1[i:]
                j-=1
            elif dp[i][j] == dp[i-1][j] + self.delta:
                str2 = str2[:j] + '_' + str2[j:]
                i-=1
        while i!= 0:
            str2 = str2[:j] + '_' + str2[j:]
            i-=1
        while j!= 0:
            str1 = str1[:i] + '_' + str1[i:]
            j-=1
        return str1, str2
    
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
    elif len(sys.argv) == 2:
        input_file_path = sys.argv[1]
        output_file_path = "output.txt"
    else:
        print("Please check the input file parameter")
        exit()
    
    s = SequenceAlignment()
    str1, str2 = generateStringWithInputFile(input_file_path)
    start_time = time.time()
    str1, str2 = s.basicProcessing(str1,str2)
    end_time = time.time()
    time_taken = (end_time - start_time)
    cost = s.calculateScoreAfterProcessing(str1, str2)
    
    with open(output_file_path, "w") as f:
        f.write(str(cost))
        f.write("\n")
        f.write(str1)
        f.write("\n")
        f.write(str2)
        f.write("\n")
        f.write(str(time_taken * 1000))
        f.write("\n")
        f.write(str(s.process_memory()))



