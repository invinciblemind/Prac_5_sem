def walk2d():
    base = (0, 0)
    what = yield base
    while what:
        tup = yield what
        what = (what[0] + tup[0], what[1] + tup[1])
