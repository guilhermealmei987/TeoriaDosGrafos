from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def ha_aresta(self, v1, v2):
        if not (self.existe_rotulo_vertice(v1) or self.existe_rotulo_vertice(v2)):
            raise VerticeInvalidoError
        for i in self.arestas:
            if (str(self.arestas[i].v1) ==v1 and str(self.arestas[i].v2) == v2) or (str(self.arestas[i].v1) == v2 and str(self.arestas[i].v2) == v1):
                return True
        return False


    def vertices_nao_adjacentes(self):
            '''
            Provê um conjunto de vértices não adjacentes no grafo.
            O conjunto terá o seguinte formato: {X-Z, X-W, ...}
            Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
            :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
            '''
            vnadj = set()
            lista_rotulos = [v.rotulo for v in self.vertices]           
            for i in range(len(lista_rotulos)):
                for j in range(i + 1, len(lista_rotulos)):
                    v1 = lista_rotulos[i]
                    v2 = lista_rotulos[j]
                    if not self.ha_aresta(v1, v2):
                        vnadj.add(f"{v1}-{v2}")
            return vnadj


    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.arestas:
            if self.arestas[i].v1 == self.arestas[i].v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not (self.existe_rotulo_vertice(V)):
            raise VerticeInvalidoError
        
        """Tem que converter pra string str() pq o .v1 puxa um Objeto do tipo Vertice, impossibilitando comparação"""
        cont = 0
        for i in self.arestas:
            if str(self.arestas[i].v1) == V or str(self.arestas[i].v2) == V:
                cont += 1
        return cont


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in self.arestas:
            for j in self.arestas:
                if i != j:
                    if (self.arestas[i].v1 == self.arestas[j].v1 and self.arestas[i].v2 == self.arestas[j].v2) or (self.arestas[i].v1 == self.arestas[j].v2 and self.arestas[i].v2 == self.arestas[j].v1):
                        return True
        return False


    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        lista = set()
        if not (self.existe_rotulo_vertice(V)):
            raise VerticeInvalidoError
        for i in self.arestas:
            if self.arestas[i].v1.rotulo == V or self.arestas[i].v2.rotulo == V:
                lista.add(self.arestas[i].rotulo)
        return lista

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if((len(self.vertices_nao_adjacentes())) == 0):
            return True
        return False
        '''for i in self.vertices:
            for j in self.vertices:
                if j != i:
                    if not self.ha_aresta(str(i), str(j)):
                        return False
        return True'''

    def eh_conexo(self):
        if (len(self.vertices) == 0 or len(self.vertices) == 1):
            return True
        visitados = set()
        self.recDfs(self.vertices[0].rotulo, visitados)
        return (len(visitados) == len(self.vertices))

    def recDfs(self, V, visitados):
        arestas_rotulos = self.arestas_sobre_vertice(V)
        #percorrer a lista de rotulos dos vertices adjacentes ao vertice atual
        for i in arestas_rotulos:
            #Condição para não usar o mesmo vertice da aresta, que acabei de visitar
            if(self.get_aresta(i).v1.rotulo == V):
                vert = self.get_aresta(i).v2.rotulo
            else:
                vert = self.get_aresta(i).v1.rotulo
            
            if vert not in visitados:
                visitados.add(vert)
                self.recDfs(vert, visitados)
        return visitados

    def ha_ciclo(self):
        #Algoritmos de busca em profundidade retorna uma arvore
        a_visitados = set()
        v_visitados = set()
        for V in self.vertices:
            V = V.rotulo
            if V not in v_visitados:
                #adiciona nó raiz
                v_visitados.add(V)
                if(self.recDfs_ciclo(V, v_visitados, a_visitados)):
                    return True
        return False
        
    def recDfs_ciclo(self, V, v_visitados, a_visitados):
        arestas_rotulos = self.arestas_sobre_vertice(V)
        #percorrer a lista de rotulos dos vertices adjacentes ao vertice atual
        for i in arestas_rotulos:              
            if i not in a_visitados:
                #Condição para não usar o mesmo vertice da aresta, que acabei de visitar
                if(self.get_aresta(i).v1.rotulo == V):
                    vert = self.get_aresta(i).v2.rotulo
                else:
                    vert = self.get_aresta(i).v1.rotulo
                if vert in v_visitados:
                    return True
                else:
                    a_visitados.add(i)
                    v_visitados.add(vert)
                    if(self.recDfs_ciclo(vert,v_visitados, a_visitados) == True):
                        return True

    def folhas_rotulos(self):
        #Algoritmos de busca em profundidade retorna uma arvore
        visitados = set()
        folhas = set()
        if(len(self.vertices) == 0):
            return False      
        elif(len(self.vertices) == 1):
            visitados.add(self.vertices[0].rotulo)
            return visitados
        V = self.vertices[0].rotulo
        visitados.add(V)
        return self.recDfs2(V, visitados, folhas)
    
    def recDfs2(self, V, visitados, folhas):
        arestas_rotulos = self.arestas_sobre_vertice(V)
        #percorrer a lista de rotulos dos vertices adjacentes ao vertice atual
        if (len(arestas_rotulos) == 1):
            folhas.add(V)
        for i in arestas_rotulos:
            #Condição para não usar o mesmo vertice da aresta, que acabei de visitar
            if(self.get_aresta(i).v1.rotulo == V):
                vert = self.get_aresta(i).v2.rotulo
            else:
                vert = self.get_aresta(i).v1.rotulo
            if vert not in visitados:
                visitados.add(vert)
                folhas = self.recDfs2(vert, visitados, folhas)
        return folhas


    def eh_arvore(self):
        '''
        :return: Falso ou Um conjunto de Vertices folhas da árvore, considerando árvore não enraizada
        '''
        if not self.eh_conexo():
            return False
        if self.ha_ciclo():
            return False
        return self.folhas_rotulos()


    def eh_bipartido(self):
        v_visitados = set()
        for i in self.vertices: 
            V = i.rotulo
            if V not in v_visitados:     
                preto = set()
                vermelho = set()
                a_visit = set()
                preto.add(V)
                if not self.rec_bipartido(V, vermelho, preto, a_visit, v_visitados):
                    return False
        return True
    def rec_bipartido(self, V, vermelho, preto, a_visi, v_visitados):
        arestas_rotulo = self.arestas_sobre_vertice(V)
        for i in arestas_rotulo:
            if(i not in a_visi):
                a_visi.add(i)
                if(self.get_aresta(i).v1.rotulo == V):
                    vert = self.get_aresta(i).v2.rotulo
                else:
                    vert = self.get_aresta(i).v1.rotulo
                if vert not in v_visitados:
                    v_visitados.add(vert)
                if(V in preto):
                    if (vert in preto):
                        return False
                    elif(vert in vermelho):
                        continue
                    vermelho.add(vert)
                elif(V in vermelho ):
                    if (vert in vermelho):
                        return False
                    elif (vert in preto):
                        continue
                    preto.add(vert)
                
                if not self.rec_bipartido(vert, vermelho, preto, a_visi, v_visitados):
                    return False
        return True

                

