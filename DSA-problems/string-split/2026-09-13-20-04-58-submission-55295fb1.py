# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Wrong Answer: Submission produced output that did not match the expected output.
def split(s, c):
  if not s and not c:
        return []
  if s=="" and c == " ":
        return []
  if s == "" and c != " ":
        return []
  
  res=[]
  i=0
  N = len(s)
  print(f'N={N}')
  seen=False
  last=-1
  while i < N:
      if i < N and s[i]==c:
          if i == 0:
              last=i
              seen=False
              res.append("")
              i+=1
          elif i > 0:
              if seen:
                  if i - last == 1:
                      # print(f"seeing c={c} consecutively again at i={i}, last seen={last}")
                      res.append("")
                      seen=False
                      i+=1
                  else:
                      # print(f"Not seen c consecutively at i={i}, last seen={last}")
                      last=i
                      i+=1
              else:
                  # print(f"seeing c={c} FIRST TIME at i={i}")
                  if i == N - 1:
                      res.append("")
                      i+=1
                  else:
                      seen=True
                      last=i
                      i+=1
      else:
          temp_str=""
          while i < N and s[i]!=c:
              temp_str+=s[i]
              i+=1
          res.append(temp_str)
  if last == N - 1:
      res.append("")
  return res
