# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def palindrome(s):
    s = s.strip()
    lo, hi = 0, len(s) - 1
    while lo <= hi:
        if s[lo] != s[hi]:
            return False
        lo+=1
        hi-=1
    return True
