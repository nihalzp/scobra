from .matrix import matrix

class flux(dict):

    def __init__(self, *args, **kwargs):
        super(flux,self).__init__(*args, **kwargs)

    def __call__(self, string=''):
        rv = flux()
        for r in self:
            if string in r:
                rv[r] = self[r]
        return rv

    def Print(self, lo=0, hi=float('inf'), f=None, Sort="value",
              sortabs=True, reverse=True):
        if Sort == "value":
            if sortabs:
                function = lambda (k,v): (abs(v),k)
            else:
                function = lambda (k,v): (v,k)
            for key, value in sorted(self.iteritems(), key=function,
                                     reverse=reverse):
                if abs(value) >= lo and abs(value) <= hi:
                    print "%s: %s" % (key, value)
        elif Sort == "key":
            for key in sorted(self.iterkeys()):
                if abs(self[key]) >= lo and abs(self[key]) <= hi:
                    print "%s: %s" % (key, self[key])

    def Diff(self, fd, IncZeroes=False, AsMtx=False, tol=1e-10):
        rv = {}
        sol2only = list(set(fd.keys()).difference(self.keys()))
        for reac in self.keys():
            if reac in fd.keys():
                rv[reac] = self[reac] - fd[reac]
            else:
                rv[reac] = self[reac]
        for reac in sol2only:
            rv[reac] = -fd[reac]
        if not IncZeroes:
            for reac in list(rv.keys()):
                if abs(rv[reac]) < tol:
                    del rv[reac]
        if AsMtx:
            mtx = matrix({"diff":rv})
            rv = mtx
        return rv

    def AsMtx(self):
        return matrix({"Flux":self})
