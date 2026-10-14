# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Wrong Answer: Submission produced output that did not match the expected output.
def common_elements(arr1, arr2):
    c = []
    M,N = len(arr1), len(arr2)
    i,j=0,0
    while i < M and j < N:
        # j=0
        print(f"starting with i={i}, j={j}")
        # while j <= N-1:
        if arr1[i]==arr2[j]:
            print(f"found common at i={i}, j={j}")
            c.append(arr2[j])
            i+=1
        j+=1
        i+=1
    return c
