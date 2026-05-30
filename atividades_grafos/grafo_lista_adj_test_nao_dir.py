import unittest
from meu_grafo_lista_adj_nao_dir import *
import gerar_grafos_teste
from bibgrafo.aresta import Aresta
from bibgrafo.vertice import Vertice
from bibgrafo.grafo_errors import *
from bibgrafo.grafo_json import GrafoJSON
from bibgrafo.grafo_builder import GrafoBuilder


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = GrafoJSON.json_to_grafo('test_json/grafo_pb.json', MeuGrafo())

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = GrafoJSON.json_to_grafo('test_json/grafo_pb2.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = GrafoJSON.json_to_grafo('test_json/grafo_pb3.json', MeuGrafo())

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = GrafoJSON.json_to_grafo('test_json/grafo_pb4.json', MeuGrafo())

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(['J', 'C', 'E', 'P']).arestas(True).build()

        self.g_c2 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(3).arestas(True).build()

        self.g_c3 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(1).build()

        # Grafos com laco
        self.g_l1 = GrafoJSON.json_to_grafo('test_json/grafo_l1.json', MeuGrafo())

        self.g_l2 = GrafoJSON.json_to_grafo('test_json/grafo_l2.json', MeuGrafo())

        self.g_l3 = GrafoJSON.json_to_grafo('test_json/grafo_l3.json', MeuGrafo())

        self.g_l4 = GrafoBuilder().tipo(MeuGrafo()).vertices([v:=Vertice('D')]) \
            .arestas([Aresta('a1', v, v)]).build()

        self.g_l5 = GrafoBuilder().tipo(MeuGrafo()).vertices(3) \
            .arestas(3, lacos=1).build()

        # Grafos desconexos
        self.g_d = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), Vertice('C'), Vertice('D')]) \
            .arestas([Aresta('asd', a, b)]).build()

        self.g_d2 = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()

        # Grafo p\teste de remoção em casta
        self.g_r = GrafoBuilder().tipo(MeuGrafo()).vertices(2).arestas(1).build()

        #Grafo Eh_bipartido
        self.e_b = GrafoBuilder().tipo(MeuGrafo()).vertices(4).build()
        self.e_b2 = GrafoBuilder().tipo(MeuGrafo()).vertices(1).build() 
        self.e_b3 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C'), d:=Vertice('D')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('cd', c, d), Aresta('da', d, a)]).build()
        self.e_b4 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:= Vertice('C'), d:=Vertice('D'), e:=Vertice('E')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('de', d, e)]).build()
        self.e_b5 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:= Vertice('C'), d:= Vertice('D'), e:= Vertice('E')]) \
            .arestas([Aresta('ab', a, b), Aresta('cd', c, d), Aresta('ce', c, e), Aresta('de', d, e)]).build()
        self.e_b6 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C'), d:=Vertice('D'), e:=Vertice('E')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('cd', c, d), Aresta('de', d, e), Aresta('ae', a, e)]).build()
        self.e_b7 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(3).arestas(True).build()
        self.e_b8 = GrafoBuilder().tipo(MeuGrafo()).build()
        self.e_b9 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B')]) \
            .arestas([Aresta('ab', a, b), Aresta('ba', b, a)]).build()
        self.e_b10 = GrafoBuilder().tipo(MeuGrafo()).vertices([a:=Vertice('A')]).arestas([Aresta('aa', a, a)]).build()
  
        self.h_c = GrafoBuilder().tipo(MeuGrafo()).vertices(1).build()
        self.h_c2 = GrafoBuilder().tipo(MeuGrafo()).vertices([a:=Vertice('A')]).arestas([Aresta('aa', a, a)]).build()
        self.h_c3 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('ca', c, a)]).build()
        self.h_c4 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B')]) \
            .arestas([Aresta('ab', a, b), Aresta('ba', b, a)]).build()
        self.h_c5 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:= Vertice('C'), d:=Vertice('D'), e:=Vertice('E')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('de', d, e)]).build()
        self.h_c6 = GrafoBuilder().tipo(MeuGrafo()).build()
        self.h_c7 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:= Vertice('C'), d:=Vertice('D'), e:=Vertice('E')]) \
            .arestas([Aresta('ab', a, b), Aresta('cd', c, d), Aresta('de', d, e), Aresta('ec', e, c)]).build()
        self.h_c8 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices(3).arestas(True).build()
        self.h_c9 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C'), d:=Vertice('D')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('ad', a, d), Aresta('bb', b, b)]).build()
        self.h_c10 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:= Vertice('C'), d:=Vertice('D'), e:=Vertice('E')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('cd', c, d), Aresta('de', d, e)]).build()
        
        self.e_a = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('ca', c, a)]).build()
        self.e_a2 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C'), d:=Vertice('D')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('ad', a, d)]).build()
        self.e_a3 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C'), d:=Vertice('D')]) \
            .arestas([Aresta('ab', a, b), Aresta('cd', c, d)]).build()
        self.e_a4 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C'), d:=Vertice('D')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c)]).build()
        self.e_a5 = GrafoBuilder().tipo(MeuGrafo()).vertices([a:=Vertice('A')]).arestas([Aresta('aa', a, a)]).build()
        self.e_a6 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:=Vertice('C'), d:=Vertice('D')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('ad', a, d), Aresta('bb', b, b)]).build()
        self.e_a7 = GrafoBuilder().tipo(MeuGrafo()).vertices([a:=Vertice('A')]).build()
        self.e_a8 = GrafoBuilder().tipo(MeuGrafo()).vertices([a:=Vertice('A'), b:= Vertice('B')]).arestas(1).build()
        self.e_a9 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B')]) \
            .arestas([Aresta('ab', a, b), Aresta('ba', b, a)]).build()
        self.e_a10 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:= Vertice('C'), d:=Vertice('D'), e:=Vertice('E')]) \
            .arestas([Aresta('ab', a, b), Aresta('bc', b, c), Aresta('cd', c, d), Aresta('de', d, e)]).build()
        self.e_a11 = GrafoBuilder().tipo(MeuGrafo()) \
            .vertices([a:=Vertice('A'), b:=Vertice('B'), c:= Vertice('C'), d:=Vertice('D'), e:=Vertice('E'), f:=Vertice('F'), g:=Vertice('G'), h:=Vertice('H'), i:= Vertice('I'), j:=Vertice('J')]) \
            .arestas([Aresta('ab', a, b), Aresta('gb', g, b), Aresta('hb', h, b), Aresta('be', b, e), Aresta('bc', b, c), Aresta('cd', c, d), Aresta('df', d, f), Aresta('hi', h, i), Aresta('hj', h, j)]).build()
        
        

    def test_eh_arvore(self):
        self.assertFalse(self.e_a.eh_arvore()) # ciclo 3 vertices
        self.assertEqual(self.e_a2.eh_arvore(), {'C', 'D'}) #arvore simples
        self.assertFalse(self.e_a3.eh_arvore()) # desconexo
        self.assertFalse(self.e_a4.eh_arvore()) #vertice isolado da arvore
        self.assertFalse(self.e_a5.eh_arvore()) #laço 1v
        self.assertFalse(self.e_a6.eh_arvore()) #laço inserido
        self.assertEqual(self.e_a7.eh_arvore(), {'A'}) # 1 vertice
        self.assertEqual(self.e_a8.eh_arvore(), {'A', 'B'}) # 2 vertices. 
        self.assertFalse(self.e_a9.eh_arvore()) # Paralela
        self.assertEqual(self.e_a10.eh_arvore(), {'A', 'E'}) # Arvore linear
        self.assertEqual(self.e_a11.eh_arvore(), {'A','F', 'E', 'I', 'J', 'G'}) # Arvore complexa. 



        
    def test_ha_ciclo(self):
        self.assertFalse(self.h_c.ha_ciclo()) # 1 vertice
        self.assertTrue(self.h_c2.ha_ciclo()) # 1 vertice com laço
        self.assertTrue(self.h_c3.ha_ciclo()) # ciclo simples de 3 vertices
        self.assertTrue(self.h_c4.ha_ciclo()) # paralela
        self.assertFalse(self.h_c5.ha_ciclo()) # desconexo sem ciclo
        self.assertFalse(self.h_c6.ha_ciclo()) # Grafo nulo
        self.assertTrue(self.h_c7.ha_ciclo()) # desconexo com ciclo
        self.assertTrue(self.h_c8.ha_ciclo()) # K3
        self.assertTrue(self.h_c9.ha_ciclo()) # laço inserido
        self.assertFalse(self.h_c10.ha_ciclo()) # grafo linear



    def test_eh_bipartido(self):
        self.assertTrue(self.e_b.eh_bipartido()) # 3 vertices desconexo
        self.assertTrue(self.e_b2.eh_bipartido()) #vertice solo
        self.assertTrue(self.e_b3.eh_bipartido()) # Ciclo bipartido
        self.assertTrue(self.e_b4.eh_bipartido())  #desconexo porem bipartido
        self.assertFalse(self.e_b5.eh_bipartido()) #desconexo não bipartido
        self.assertFalse(self.e_b6.eh_bipartido()) # Ciclo nao bipartido (5 vertices)
        self.assertFalse(self.e_b7.eh_bipartido()) #K3
        self.assertTrue(self.e_b8.eh_bipartido()) #Grafo Nulo
        self.assertTrue(self.e_b9.eh_bipartido()) #Aresta paralela
        self.assertFalse(self.e_b10.eh_bipartido()) # Laço
  
    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(TypeError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_remove_vertice(self):
        self.assertIsNone(self.g_r.remove_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_vertice('A'))
        self.assertFalse(self.g_r.existe_rotulo_aresta('1'))
        with self.assertRaises(VerticeInvalidoError):
            self.g_r.get_vertice('A')
        self.assertFalse(self.g_r.get_aresta('1'))
        self.assertEqual(self.g_r.arestas_sobre_vertice('B'), set())

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))
