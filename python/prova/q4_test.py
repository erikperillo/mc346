import q4

def test():
    a = q4.Intervalo(1, 0, 2)
    b = q4.Intervalo(2, 2, 5)
    print "a = [%d, %d]" % (a.xmin, a.xmax)
    print "b = [%d, %d]" % (b.xmin, b.xmax)
    print "a.elo(b):", a.elo(b)
    assert(a.elo(b) == b.elo(a))
    print

    a = q4.Intervalo(1, 0, 2)
    b = q4.Intervalo(2, 1, 5)
    print "a = [%d, %d]" % (a.xmin, a.xmax)
    print "b = [%d, %d]" % (b.xmin, b.xmax)
    print "a.elo(b):", a.elo(b)
    assert(a.elo(b) == b.elo(a))
    print

    a = q4.Intervalo(1, 2, 4)
    b = q4.Intervalo(2, -1, 5)
    print "a = [%d, %d]" % (a.xmin, a.xmax)
    print "b = [%d, %d]" % (b.xmin, b.xmax)
    print "a.elo(b):", a.elo(b)
    assert(a.elo(b) == b.elo(a))
    print

    a = q4.Intervalo(1, -2, 6)
    b = q4.Intervalo(2, -2, 6)
    print "a = [%d, %d]" % (a.xmin, a.xmax)
    print "b = [%d, %d]" % (b.xmin, b.xmax)
    print "a.elo(b):", a.elo(b)
    assert(a.elo(b) == b.elo(a))
    print

    a = q4.Intervalo(1, 3, 6)
    b = q4.Intervalo(2, 1, 6)
    print "a = [%d, %d]" % (a.xmin, a.xmax)
    print "b = [%d, %d]" % (b.xmin, b.xmax)
    print "a.elo(b):", a.elo(b)
    assert(a.elo(b) == b.elo(a))
    print

    a = q4.Intervalo(1, 1, 3)
    b = q4.Intervalo(2, 1, 6)
    print "a = [%d, %d]" % (a.xmin, a.xmax)
    print "b = [%d, %d]" % (b.xmin, b.xmax)
    print "a.elo(b):", a.elo(b)
    assert(a.elo(b) == b.elo(a))
    print

    a = q4.Intervalo(1, 3, 4)
    b = q4.Intervalo(2, 8, 15)
    print "a = [%d, %d]" % (a.xmin, a.xmax)
    print "b = [%d, %d]" % (b.xmin, b.xmax)
    print "a.elo(b):", a.elo(b)
    assert(a.elo(b) == b.elo(a))
    print

if __name__ == "__main__":
    test()
