


def merge_sort(l,r):

    if r -l == 0:
        return

    m = (l+r)//2
    merge_sort(l,m)
    merge_sort(m,r)

    