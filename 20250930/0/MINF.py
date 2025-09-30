def MINF(*ff):
    def g(x):
        return min([fi(x) for fi in ff])
    return g
