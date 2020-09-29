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


def aEstrela(origem,fim): 
  # 1. Criar fila explorados e fila de prioridades = {Ø}
  fila=[]
  explorados=[]

  # 2. Se origem == destino -> finaliza
  if(origem.getNome() != fim.getNome()):
    # 3. Função g do nó origem = 0
    origem.setFuncaoG(0)
    # 4. filaPrioridades adiciona origem
    fila.append(origem)
    # 5. Enquanto filaPrioridades não vazia e destino não encontrado
    encontrado=False

    while(len(fila)>0 and not(encontrado)):
      # 5_1. Nó atual = Nó com menor função f
      atual = encontrarMenor(fila)
      # 5_2. Fila explorados adiciona nó atual
      explorados.append(atual)
      # 5_3. Se nó atual == destino -> parar
      if(atual.getNome()==fim.getNome()):
        encontrado=True

      # 5_4. Se não...
      else:
        # 5_4_1. Para cada aresta adjacente do no atual
        for aresta in atual.getAdjacentes():
          # 5_4_2. Nó filho = aresta.alvo
          filho = aresta.getAlvo()
          # 5_4_3. funcaoGTemp= noAtual.FuncaoG() + aresta.custo
          funcaoGTemp = atual.getFuncaoG() + aresta.getCusto()
          # 5_4_4. funcaoFTemp= funcaoGTemp+ noFilho.FuncaoH()
          funcaoFTemp= funcaoGTemp+filho.getFuncaoH()
          # 5_4_5. Se caso o nó filho já tenha sido explorado e seu valor de função f é maior que a função f do pai, então ele é desconsiderado
          if((filho in explorados) and (funcaoFTemp>=filho.getFuncaoF())):
            continue

          # 5_4_6. senão se o nó filho não está na filaPrioridadesou sua função f é maior que a funcaoFTemp
          elif((filho not in fila)or (funcaoFTemp < filho.getFuncaoF())):
            # 5_4_6_1. filho.Adjacente= atual
            filho.setAdjacente(atual)
            # 5_4_6_2.filho.funcaoG= funcaoGTemp
            filho.setFuncaoG(funcaoGTemp)
            # 5_4_6_3. filho.funcaoF= funcaoFTemp
            filho.setFuncaoF(funcaoFTemp)
            # 5_4_6_4. Se filaPrioridadescontem filho
            # 5_4_6_5. fila.removefilho
            if(filho not in fila):
              # 5_4_6_5. Fila adiciona filho
              fila.append(filho)

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
