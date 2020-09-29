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

      




    def buscaMenorValorFuncaoF(cities, name_city):
      for city in self.cities:
        if (city.nome == self.fila_propriedades[0]):
          menor
          city.aresta[2].noAlvo









# ---------------------------------------------------------------------------
Cities = []
Cities.append(Nó('Arad', 366))
Cities[0].getAdjacentes('Zerind',75)
Cities[0].getAdjacentes('Sibiu',140)
Cities[0].getAdjacentes('Timisoara',118)

# Cities.append(Nó('Bucharest', 0))
# Cities[1].getAdjacentes('Urziceni',85)
# Cities[1].getAdjacentes('Giurgiu',90)
# Cities[1].getAdjacentes('Fagaras',211)

# Cities.append(Nó('Craiova', 160))
# Cities[2].getAdjacentes('Drobeta',120)
# Cities[2].getAdjacentes('Rimnicu',146)
# Cities[2].getAdjacentes('Pitesti',138)

# Cities.append(Nó('Drobeta', 242))
# Cities[3].getAdjacentes('Craiova',120)
# Cities[3].getAdjacentes('Mehadia',75)


# Cities.append(Nó('Eforie', 161))
# Cities[4].getAdjacentes('Hirsova',86)

# Cities.append(Nó('Fagaras', 176))
# Cities[5].getAdjacentes('Bucharest',211)
# Cities[5].getAdjacentes('Sibiu',99)

# Cities.append(Nó('Giurgiu', 77))
# Cities[6].getAdjacentes('Bucharest',90)

# Cities.append(Nó('Hirsova', 151))
# Cities[7].getAdjacentes('Eforie',86)
# Cities[7].getAdjacentes('Urziceni',98)

# Cities.append(Nó('Iasi', 226))
# Cities[8].getAdjacentes('Vaslui',92)
# Cities[8].getAdjacentes('Neamt',87)

# Cities.append(Nó('Lugoj', 244))
# Cities[9].getAdjacentes('Mehadia',70)
# Cities[9].getAdjacentes('Timisoara',111)

# Cities.append(Nó('Mehadia', 241))
# Cities[10].getAdjacentes('Lugoj',70)
# Cities[10].getAdjacentes('Drobeta',75)

# Cities.append(Nó('Neamt', 234))
# Cities[11].getAdjacentes('Iasi',87)

# Cities.append(Nó('Oradea', 380))
# Cities[12].getAdjacentes('Zerind',71)
# Cities[12].getAdjacentes('Subiu',151)

# Cities.append(Nó('Pitesti', 100))
# Cities[13].getAdjacentes('Bucharest',101)
# Cities[13].getAdjacentes('Craiova',138)
# Cities[13].getAdjacentes('Rimnicu Vilcea',97)

# Cities.append(Nó('Rimnicu Vilcea', 193))
# Cities[14].getAdjacentes('Pitesti',97)
# Cities[14].getAdjacentes('Sibiu',80)
# Cities[14].getAdjacentes('Craiova',146)

# Cities.append(Nó('Sibiu', 253))
# Cities[15].getAdjacentes('Rimnicu Vilcea',80)
# Cities[15].getAdjacentes('Fagaras',99)
# Cities[15].getAdjacentes('Oradea',151)

# Cities.append(Nó('Timisoara', 329))
# Cities[16].getAdjacentes('Arad',118)
# Cities[16].getAdjacentes('Loguj',111)

# Cities.append(Nó('Urziceni', 80))
# Cities[17].getAdjacentes('Bucharest',85)
# Cities[17].getAdjacentes('Vaslui',142)
# Cities[17].getAdjacentes('Hirsova',98)

# Cities.append(Nó('Vaslui', 199))
# Cities[18].getAdjacentes('Iasi',92)
# Cities[18].getAdjacentes('Urziceni',142)


# Cities.append(Nó('Zerind', 374))
# Cities[19].getAdjacentes('Arad', 75)
# Cities[19].getAdjacentes('Oradea', 71)



# FAZENDO CALCULO DA FUNÇÃO F
# FUNÇÃO F => F = G + H
# FUNÇÃO G => Custo do nó inicial até o  nó atual.
# FUNÇÃO H => Custo do nó atual até o  nó destino.

for city in Cities:
  print('só 1')
  for adjacentes in city.aresta:
    print('só 3')
    for search_city in Cities:
      print('só 3')
      print(search_city.nome)
      if (search_city.nome == adjacentes.noAlvo):
         adjacentes.valorF = search_city.valorFuncaoH + adjacentes.custo
    


# for city in Cities:
#   for adjacentes in city.aresta:
#     print(adjacentes.noAlvo)
#     print(adjacentes.valorF)

# print(Cities[0].aresta[2].noAlvo)


# algoritmo = Aestrela()
# algoritmo.main(Cities)
# algoritmo.buscaAEstrela(Cities[0], Cities[1])