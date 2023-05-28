class nota_fiscal:
    def __init__(self,nome,cnpj,telefone,cidade,estado):
        self.nome=nome
        self.cnpj=cnpj
        self.telefone=telefone
        self.cidade=cidade
        self.estado=estado
    def fone(self,a):
        print(self.telefone,a)
    
    def city(self):
        print(self.cidade,self.estado)

mercado = nota_fiscal("carlos","108460517","149989795","uberlandia","são paulo")
mercado.fone(12)c
mercado.city()