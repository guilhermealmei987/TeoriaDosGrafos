from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *
import heapq

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau_entrada(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass


    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        n = len(self.vertices)
        #Construir matriz com 0 e 1
        clone = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                #se existe aresta
                if (self.matriz[i][j] != {}):
                    clone[i][j] = 1

        for i in range(n):
            for j in range(n):
                #se tiver aresta. olha por coluna
                if clone[j][i] == 1:
                    for k in range(n):
                        #verifica se há aresta na linha correspondente
                        clone[j][k] = max(clone[j][k], clone[i][k])
        return clone

    #. ..- / -. .- --- / .- --. ..- . -. - --- / -- .- .. ... / ... --- -.-. --- .-. .-. ---
    def menor_caminho(self, Vi, Vf):
        if not (self.existe_rotulo_vertice(Vi) and self.existe_rotulo_vertice(Vf)):
            raise VerticeInvalidoError       
        
        n = len(self.vertices)
        clone = [[float('inf') for _ in range(n)] for _ in range(n)]
        
        # Construcao da matriz
        for i in range(n):
            for j in range(n):
                if i == j:
                    clone[i][j] = 0
                elif self.matriz[i][j] != {}:
                    pesos = [self.matriz[i][j][k].peso for k in self.matriz[i][j]]

                    if any(p < 0 for p in pesos):
                        return False
                    else:
                        clone[i][j] = min(pesos)

        #lista de prioridade, vai receber tupla com peso e rotulo
        listapri = []

        #usando heapq para sempre priorizar a aresta de menor peso
        heapq.heappush(listapri, (0, Vi))
        
        #Dicionario com vertices visitados, o Valor de cada chave é o peso acumulado para chegar no vertice, e o seu pai
        visitados = {Vi: (0, None)}

        #enquanto tiver vertices para acessar
        while listapri:

            peso_atual, Va_rotulo = heapq.heappop(listapri)

            #Se chegou no destino
            if Va_rotulo == Vf:
                break

            # Se encontra um custo maior do que o ja registrado, pula
            if peso_atual > visitados[Va_rotulo][0]:
                continue
 
            x = self.indice_do_vertice(self.get_vertice(Va_rotulo))

            for i in range(n):

                peso_aresta = clone[x][i]
                
                #se tiver uma aresta para outro vertice..
                if peso_aresta != float('inf') and x != i:

                    vert = self.vertices[i].rotulo
                    novo_peso = peso_atual + peso_aresta

                    # Não descarto vertices ja visitados, pois Se for um caminho com menos peso para alcançar o vértice, atualizo
                    if vert not in visitados or novo_peso < visitados[vert][0]:
                        visitados[vert] = (novo_peso, Va_rotulo)
                        heapq.heappush(listapri, (novo_peso, vert))

        
        if Vf in visitados:
            #Construir o caminho percorrendo antecessores do Vertice Final alcançado
            caminho = []
            v_atual = Vf
            while (v_atual is not None):
                caminho.append(v_atual)
                v_atual = visitados[v_atual][1] 
            
            caminho.reverse()
            return caminho
        else:
            return []
            
        







        



        