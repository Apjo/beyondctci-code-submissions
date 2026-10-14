# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def join(arr, s):
    if len(arr) == 0:
        return ""
    N = len(arr)
    res=[]
    for i in range(N):
        if i != N - 1:
            res.append(arr[i])
            res.append(s)
        else:
            res.append(arr[i])
    return "".join(res)
