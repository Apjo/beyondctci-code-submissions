# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Wrong Answer: Submission produced output that did not match the expected output.
def common_elements(arr1, arr2):
    c = []
    M,N = len(arr1), len(arr2)
    i,j=0,0
    while i < M:
        j=0
        while j < N:
            print(f"current i={i}, j={j}")
            if i < N and arr1[i] == arr2[j]:
                print(f"found common element at i={i}, j={j}")
                c.append(arr1[i])
                i+=1
            j+=1
        i+=1
    return c
