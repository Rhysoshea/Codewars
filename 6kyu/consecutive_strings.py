'''
Instructions
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
'''


''' Solution '''
def longest_consec(strarr, k):
    max = 0
    index = 0
    if k <= 0 or k > len(strarr):
        return ""
    for i in range(len(strarr)-k+1):
        # print (strarr[i:i+k])
        if sum([len(n) for n in strarr[i:i+k]]) > max:
            max = sum([len(n) for n in strarr[i:i+k]])
            index = i
    return ''.join(strarr[index:index+k])

print (longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15))

''' Alternative Solution '''
def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s

    return result
