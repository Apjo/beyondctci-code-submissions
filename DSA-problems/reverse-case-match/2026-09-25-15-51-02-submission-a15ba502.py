# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def reverse_case_match(s):
  if not s:
    return True
  s2 = []
  N = len(s)
  s1=""
  for i in range(N):
    if s[i].islower():
      s1+=s[i]
    else:
      s2.insert(0, s[i])
  ss2 = "".join(s2)
  return s1 == ss2.lower()