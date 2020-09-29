# Algoritmo-A-estrela
reciar os algoritmo a estrela em python

<h1 align="center">Algoritmo AEstrela (A*)</h1>

<h2 align="center">Reconstruir algoritmo AEstrela para busca de caminho com base no problema proposto.</h2>

<img src="./img/line.png" alt="line" width="100%">
<br>

<h1 align="center">PROBLEMA</h1>
<h2 align="center">Para o mapa apresentado construa a árvore de busca do caminho entre as cidades Arad e Bucharestpara as estratégias de busca em Largura e em Profundidade.</h2>

<div align="center">
  <img src="./img/mapa.png" alt="Mapa" height="500" width="100%">
</div>
<img src="./img/line.png" alt="line" width="100%">
<br>

<h1 align="center">DISTÂNCIA EM LINHA RETA ATÉ BUCARESTE (função h) </h1>
<div align="center">
  <img src="./img/custo.png" alt="Web Version" height="500" width="800%">
</div>
<img src="./img/line.png" alt="line" width="100%">
<br>

<h1 align="center">CLASSES E FUNÇÕES</h1>

<h2>ATRIBUTOS PARA CLASSE NÓ:</h2>
–String nome; (get - construtor)<br>
–double valorFuncaoF= 0; (get e set)<br>
–doublevalorFuncaoG; (get e set)<br>
–doublevalorFuncaoH; (get - construtor)<br>
–Nó antecessor; (get e set)<br>
–Aresta[] adjacentes; (get e set)<br>
<br>
<h2>ATRIBUTOS PARA CLASSE ARESTA:</h2>
–Double custo; (get - construtor)<br>
–No alvo; (get - construtor)<br>
<br>
<h2>FUNÇÃO AESTRELA:</h2>
–Public static void main(String[] args){}<br>
–publicstaticvoidbuscaAEstrela(Nó origem, Nó destino) {}<br>