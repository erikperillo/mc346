class Intervalo:
    def __init__(self, id, xmin, xmax):
        self.id = id
        self.xmin = xmin
        self.xmax = xmax

    #Intervalo cruza pela esquerda de ival. Pode estar dentro dele ou nao.
    def left_crosses(self, ival):
        return self.xmax >= ival.xmin and self.xmax <= ival.xmax

    #Tamanho da intersecao caso haja um cruzamento pela esquerda de ival.
    def left_cross_size(self, ival):
        return self.xmax - ival.xmin - max(0, self.xmin - ival.xmin)

    #Distancia minima entre os intervalos caso nao haja cruzamento.
    def no_cross_dist(self, ival):
        return min(abs(self.xmin - ival.xmax), abs(ival.xmin - self.xmax))

    def elo(self, ival):
        if self.left_crosses(ival):
            return self.left_cross_size(ival)
        if ival.left_crosses(self):
            return ival.left_cross_size(self)
        else:
            return -self.no_cross_dist(ival)
