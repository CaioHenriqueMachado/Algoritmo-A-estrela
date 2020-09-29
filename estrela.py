class Aresta:
    def __init__(self, alvo,custo):
        self.custo=custo
        self.alvo=alvo
  
    def getCusto(self):
        return self.custo
  
    def getAlvo(self):
        return self.alvo

class No:
    def __init__(self, nome, funcaoH):
        self.nome=nome
        self.funcaoH=funcaoH
        self.funcaoF=0
        self.adjacente=None

    def getNome(self):
        return self.nome
    
    def getFuncaoH(self):
        return self.funcaoH

    def setFuncaoF(self, funcaoF):
        self.funcaoF = funcaoF
    
    def getFuncaoF(self):
        return self.funcaoF
    
    def setFuncaoG(self, funcaoG):
        self.funcaoG=funcaoG

    def getFuncaoG(self):
        return self.funcaoG
    
    def setAdjacente(self, adjacente):
        self.adjacente=adjacente
    
    def getAdjacente(self):
        return self.adjacente
    
    def setAdjacentes(self, adjacentes):
        self.adjacentes=adjacentes
    
    def getAdjacentes(self):
        return self.adjacentes


def encontrarMenor(lista):
    menor = 0
    for indice in range(0,len(lista)):
        if(lista[menor].getFuncaoF()>lista[indice].getFuncaoF()):
            menor = indice
    return lista.pop(menor)

def percorrerCaminho(alvo):
    caminho = "]"
    while(not(alvo is None)):
       caminho=", "+alvo.getNome()+caminho
       alvo=alvo.getAdjacente()
    caminho = "["+caminho
    return caminho


class Aestrela:
  def main(self, cities):
    self.cities = cities

  def buscaAEstrela(self, nó_origem, nó_destino):

    # 1. Criar fila explorados e fila de prioridades = {Ø}
    self.fila_explorados = []
    self.fila_propriedades = []

    # 2. Função g do nó origem = 0
    nó_origem.getValorFuncaoG(0)

    # 3. Se origem == destino -> finaliza
    if (nó_origem.nome == nó_destino.nome):
      print("FINALIZOU !!")
      return True

    # 4. filaPrioridades adiciona origem
    self.fila_propriedades.append(nó_origem.nome)

    # 5. Enquanto filaPrioridades não vazia e destino não encontrado
    while ( len(self.fila_propriedades) != 0 ):
      # 5_1.No atual = no com menor função f
      buscaMenorValorFuncaoF(self.cities, self.fila_propriedades[0])

      










# ---------------------------------------------------------------------------

arad = No("Arad",366)
bucharest=No("Bucharest",0)
craiova = No("Craiova",160)
eforie=No("Eforie",161)
fagaras= No("Fagaras",178)
giurgiu = No("Giurgiu", 77)
zerind = No("Zerind", 374)
oradea = No("Oradea", 380)
sibiu = No("Sibiu", 253)
rimnicu = No("Rimnicu Vilcea", 193)
pitesti = No("Pitesti", 98)
timisoara = No("Timisoara", 329)
lugoj = No("Lugoj", 244)
mehadia = No("Mehadia", 241)
drobeta = No("Drobeta", 242)

arad.setAdjacentes([Aresta(zerind,75),Aresta(sibiu,140),Aresta(timisoara,118)])
zerind.setAdjacentes([Aresta(arad,75),Aresta(oradea,71)])
oradea.setAdjacentes([Aresta(zerind,71),Aresta(sibiu,151)])
sibiu.setAdjacentes([Aresta(arad,140),Aresta(fagaras,99),Aresta(oradea,151),Aresta(rimnicu,80)])
fagaras.setAdjacentes([Aresta(sibiu,99),Aresta(bucharest,211)])
rimnicu.setAdjacentes([Aresta(sibiu,80),Aresta(pitesti,97),Aresta(craiova,146)])
pitesti.setAdjacentes([Aresta(rimnicu,97),Aresta(bucharest,101),Aresta(craiova,138)])
timisoara.setAdjacentes([Aresta(arad,118),Aresta(lugoj,111)])
lugoj.setAdjacentes([Aresta(timisoara,111),Aresta(mehadia,70)])
mehadia.setAdjacentes([Aresta(lugoj,70),Aresta(drobeta,75)])
drobeta.setAdjacentes([Aresta(mehadia,75),Aresta(craiova,120)])
craiova.setAdjacentes([Aresta(drobeta,120),Aresta(rimnicu,146),Aresta(pitesti,138)])
bucharest.setAdjacentes([Aresta(pitesti,101),Aresta(giurgiu,90),Aresta(fagaras,211)])
giurgiu.setAdjacentes([Aresta(bucharest,90)])

aEstrela(arad,bucharest)
print(percorrerCaminho(bucharest))
