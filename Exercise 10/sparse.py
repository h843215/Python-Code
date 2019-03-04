class SparseVector(object):
    def __init__(self, length):
        self.length = length
        self.sv = {}
        
    #Reference from slides
    #def __str__(self):
        #fields = self.length
        #return "SparseVector(" + str(fields) + ")"

    def __len__(self):
        return self.length

    def set_pos(self, pos, el):
        self.sv[pos] = el #create a dict then put pos and el in here (create dict in __init__)

    def get_pos(self, pos):
        if pos not in self.sv: #if there is no index return 0
            return 0
        else:
            return self.sv[pos] #if there is an index return pos

    def __str__(self):
        fields = [0]*self.length
        for pos in self.sv:
            fields[pos] = self.sv[pos]
        #fields = [i.strip(' ','') for i in fields]
        #Error is not related to fields ignore!!
        SV = "SparseVector" + str(fields)
        SV = ''.join(SV.split()) #remove space
        return SV     

    def concatenate(self, v):
        fields = [0]*self.length
        for pos in self.sv:
            fields[pos] = self.sv[pos]
        merge = {}
        if POS not in merge:
            ano[POS] = merge[POS]
        lo = fields + ano
        end = "SparseVector" + str(lo)
        end = ''.join(end.split())
        return end
        #SOLUTION
        #ano = dict(self.sv)
        #for k, i in v.sv.items():
            #ano[k + self.length] = i

        #end = SparseVector(self.length + v.length)
        #end.new(ano)
        #return end

    #def new(self, ano):
        #self.sv = dict(ano)
