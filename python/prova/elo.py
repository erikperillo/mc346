#!/usr/bin/env python2.7

import sys

def reps(lst):
    return filter(lambda x: lst.count(x) > 1, set(lst))

def sort_ivals(ivals):
    return sorted(ivals, key=lambda x: x.x_min)

def separate(ivals):
    inside = []
    outside = [] 
    for k, ival in enumerate(ivals):
        same_x_min = []
        max_rng = k
        min_rng = k
        for i in xrange(k+1, len(ivals)):
            if ivals[i].x_min == ival.x_min:
                max_rng += 1
            else:
                break
        #if any(ival.inside(i) for i in ivals[:k] + same_x_min):
        ins = False
        for i in xrange(max_rng, -1, -1):
            if ival.inside(ivals[i]) and i != k:
                ins = True
                inside.append(ival)
                break
        if not ins:
            outside.append(ival)
    return inside, outside

def error(msg, ret_code=0):
    print "erro;", msg
    exit(ret_code)

class Interval:
    def __init__(self, uniq_num, x_min, x_max):
        self.uniq_num = uniq_num
        self.x_min = x_min
        self.x_max = x_max

    #Intervalo cruza pela esquerda de ival. Pode estar dentro dele ou nao.
    def left_crosses(self, ival):
        return self.x_max >= ival.x_min and self.x_max <= ival.x_max

    #Tamanho da intersecao caso haja um cruzamento pela esquerda de ival.
    def left_cross_size(self, ival):
        return self.x_max - ival.x_min - max(0, self.x_min - ival.x_min)

    def inside(self, ival):
        return self.left_crosses(ival) and self.x_min >= ival.x_min

    #Distancia minima entre os intervalos caso nao haja cruzamento.
    def no_cross_dist(self, ival):
        return min(abs(self.x_min - ival.x_max), abs(ival.x_min - self.x_max))

    def size(self):
        return self.x_max - self.x_min

    def __repr__(self):
        return "Interval #%d [%d, %d]" % (self.uniq_num, self.x_min, self.x_max)

    def link(self, ival):
        if self.left_crosses(ival):
            return self.left_cross_size(ival)
        if ival.left_crosses(self):
            return ival.left_cross_size(self)
        else:
            return -self.no_cross_dist(ival)

def min_link(ivals):
    #print [ival.x_min for ival in ivals]
    ivals = sort_ivals(ivals)
    inside, outside = separate(ivals)
    min_out = min(outside[i].link(outside[i+1]) for i in range(len(outside)-1))
    if inside:
        min_in = min(i.size() for i in inside)
        return min(min_in, min_out)
    return min_out
    #print [ival.x_min for ival in ivals]

def main():
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
        ivals.append(Interval(uniq_num, x_min, x_max))
    #sys.stdout.write("bss\n")
    #sys.stdout.flush()

    if len(ivals) < 2:
        error("not enough intervals")

    print min_link(ivals)

if __name__ == "__main__":
    main()
