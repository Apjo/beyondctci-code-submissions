# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def split(s, c):
  if not s:
    return []

  res=[]
  i=0
  N = len(s)
  curr_word=[]
  while i < N:
      if s[i]==c:
          res.append("".join(curr_word))
          curr_word=[]
      else:
          curr_word.append(s[i])
      i+=1
  res.append("".join(curr_word))
  return res
