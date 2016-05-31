from multiprocessing import Array, Value, Lock
from multiprocessing.context import Process
import time
# function to check for palindrome
def palindrome(n):
    # replace all new lines
    n = n.replace('\n', "")
    # replace all spaces
    # THIS ASSUMES ONLY ONE SPACE BETWEEN WORDS
    n = n.replace(" ", "")
    # put all letters as lowercase
    n = n.lower()
    # return if the word front and back match
    return n == n[::-1]
# function to check for palindrome for all words
def checkPalindrome(index, words, pali, k):
    # using cyclic partitioning
    for i in range(index, len(words), k):
        # get current word and check if it is a palindrome
        # result will be a bool
        palinOrNot = palindrome(words[i])
        # if result is true, set result array as 1
        # 1 means palindrome, 0 means not
        if (palinOrNot == True):
            pali[i] = 1
# main
if __name__ == '__main__':
    # get processor count
    n = int(input("Enter number of processes"))
    # take start time of entire program
    program_start = time.time()
    # create array
    array = []
    # open file
    with open("Palindromes.txt", "r") as f:
        # read each line from file (each word)
        for line in f:
            # append word to array
            array.append(line)
    # check palindrome of each word
    palindromeArray = Array('i', len(array))
    # create processor array
    p = []
    # loop creating processing
    for i in range(n):
        p.append(Process(target=checkPalindrome, args=(i, array, palindromeArray, n)))
    # take start time of the actually work
    function_start = time.time()
    # start and join each process
    for i in range(n):
        p[i].start()
        p[i].join()
    # take start time of the actually work
    function_end = time.time()
    # take end time of program
    program_end = time.time()
    # print results
    for i in range(len(array)):
        # if word is not palindrome
        # if result is 1
        if palindromeArray[i] != 1:
            # print word
            print(array[i])
    # display time of entire program
    print("Time elapsed of entire program: ", (program_end-program_start))
    # display time of function
    print("Time elapsed of the function: ", (function_end-function_start))

