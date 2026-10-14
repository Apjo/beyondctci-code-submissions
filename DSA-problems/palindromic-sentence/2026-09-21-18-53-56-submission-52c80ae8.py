# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Wrong Answer: Submission produced output that did not match the expected output.
def palindromic_sentence(s):
    '''
    iterate from front and back at the same time
    -while s[lo] is not char, increment lo, else if s[hi] is not a char decrement hi
    -if s[lo] and s[hi] is a char, and they match continue moving inwards
    -else return false
    '''
    s=s.lower()
    s=s.strip()
    # print(s)
    lo, hi = 0, len(s) - 1
    while lo < hi:
        while not s[lo].isalpha():
            lo+=1
        while not s[hi].isalpha():
            hi-=1
        if s[lo].isalpha() and s[hi].isalpha():
            if s[lo] != s[hi]:
                return False
        
        lo+=1
        hi-=1
    return True

