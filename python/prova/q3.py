def inva(dct):
    inv_dct = {}
    for k, v in dct.iteritems():
        if v in inv_dct:
            inv_dct[v].append(k)
        else:
            inv_dct[v] = [k]
    return inv_dct
