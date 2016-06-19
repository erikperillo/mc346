class Interval:
    """
    Class representing an integer and closed interval.
    """

    def __init__(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max

    def left_crosses(self, ival):
        """Interval crosses ival from left. It may be inside it or not."""
        return self.x_max >= ival.x_min and self.x_max <= ival.x_max

    def left_cross_size(self, ival):
        """Crossing size in the case there is a left crossing."""
        return self.x_max - ival.x_min - max(0, self.x_min - ival.x_min)

    def inside(self, ival):
        """Returns true if interval is inside if ival."""
        return self.left_crosses(ival) and self.x_min >= ival.x_min

    def no_cross_dist(self, ival):
        """Minimum distance between intervals in case there is no crossing."""
        return min(abs(self.x_min - ival.x_max), abs(ival.x_min - self.x_max))

    def size(self):
        """Size of interval."""
        return self.x_max - self.x_min

    def __repr__(self):
        """To be used in print etc."""
        return "Interval [%d, %d]" % (self.x_min, self.x_max)

    def link(self, ival):
        """Gets the link size between two intervals."""
        if self.left_crosses(ival):
            return self.left_cross_size(ival)
        if ival.left_crosses(self):
            return ival.left_cross_size(self)
        else:
            return -self.no_cross_dist(ival)

def sort(ivals):
    """Sorts a list of intervals by x_min."""
    return sorted(ivals, key=lambda x: x.x_min)

def separate(ivals):
    """
    Separates a list of intervals in a list of intervals that are inside
    other intervals and a list of intervals that are not.
    Assumes intervals list is sorted by x_min.
    """
    inside = []
    outside = [] 

    for k, ival in enumerate(ivals):
        same_x_min = []
        max_k = k
        #intervals with same x_min may also contain ival
        for i in xrange(k+1, len(ivals)):
            if ivals[i].x_min == ival.x_min:
                max_k += 1
            else:
                break
        #finding out whether ival is inside some interval
        outside.append(ival)
        for i in xrange(max_k, -1, -1):
            if ival.inside(ivals[i]) and i != k:
                inside.append(outside.pop())
                break

    return inside, outside

def min_link(ivals):
    """Gets minimum link of a list of intervals."""
    sorted_ivals = sort(ivals)
    inside, outside = separate(sorted_ivals)

    min_out = min(outside[i].link(outside[i+1]) for i in range(len(outside)-1))

    if inside:
        return min(min(i.size() for i in inside), min_out)
    return min_out
