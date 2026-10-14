# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def smaller_prefixes(arr):
    if not arr:
        return True
    N = len(arr)
    # ps=[0]*(N)
    ps=[]
    ps.append(arr[0])
    
    k = N // 2
    for i in range(1, N):
        ps.append(ps[i - 1] + arr[i])
    # print(ps)
    # if ps[k - 1] > ps[k - 2] and ps[k - 1] < ps[k]:
    #     return True
    # return False
    for kd in range(1, k+1):
            # print(f"curent k={kd}")
            first_k = ps[kd - 1]
            twice = kd*2
            first_2k = ps[twice - 1]
            # print(f"sum of first k={ps[kd-1]}, sum of first 2k={ps[2*kd-1]}")
            if first_k > first_2k:
                return False
        # return True
    return True
