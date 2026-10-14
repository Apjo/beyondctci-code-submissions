# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_substrings_without_letter(s):
    if not s:
        return 0
    new_str = s.split("a")
    k=0
    for ss in new_str:
        N = len(ss)
        m = (N*(N+1))// 2
        k+=m
    return k
    