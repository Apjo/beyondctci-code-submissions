# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def reverse_case_match(s):
  if not s:
    return True
  N = len(s)
  lo, hi = 0, N - 1
  while lo < hi:
    if not s[lo].islower():
      lo+=1
    if not s[hi].isupper():
      hi-=1
    else:
      if s[lo] != s[hi].lower():
        return False
      lo+=1
      hi-=1
  return True
