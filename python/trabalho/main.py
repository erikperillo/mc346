#!/usr/bin/env python2.7

import sys
import interval as iv

def error(msg, ret_code=0):
    print "erro;", msg
    exit(ret_code)

def main():
    """
    Main routine. 
    Reads intervals from stdin, builds intervals list and returns min_link.
    """
    ivals = []
    ids = {}

    for line in sys.stdin:
        try:
            uniq_num, x_min, x_max = map(int, line.strip().split())
        except ValueError:
            error("str to int conversion error")

        #checking validity of interval
        if x_max - x_min < 1:
            error("invalid interval: [%d, %d]" % (x_min, x_max))
        #checking validity of id
        if uniq_num in ids:
            error("id %d is not unique" % uniq_num)
        else:
            ids[uniq_num] = True

        #appending interval to list
        ivals.append(iv.Interval(x_min, x_max))

    if len(ivals) < 2:
        error("not enough intervals")

    print iv.min_link(ivals)

if __name__ == "__main__":
    main()
