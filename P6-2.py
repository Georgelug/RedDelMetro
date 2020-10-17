import sys
import metro as m
class Vertice:
    def __init__(self,nombre):
        self.nombre = nombre
        self.distancia = sys.maxsize
        self.color = "White"
        self.padre = None
        self.vecinos = []
    def AgregarVecino(self , vecino):
        if vecino not in self.vecinos:
            self.vecinos.append(vecino)
        else:
            print("no se pudo agregar vecino")
    def __str__ (self):
        return self.nombre
    def __repr__(self):
        return self.nombre
    def ShowData(self):
        print(f"\n\n\tnombre: {self.nombre}\n\n\tDistancia: {self.distancia}\t\tColor: {self.color}")
class Grafo:
    def __init__(self):
        self.vertices = {}
    def agregarVertice(self,nombreVertice):
        if nombreVertice in self.vertices:
            #print("\n\n\tError ya existe el vertice")
            return False
        vertice = Vertice(nombreVertice)
        self.vertices[vertice.nombre]=vertice
        return True
    def agregarArista(self,verticeNombre1,verticeNombre2):
        if verticeNombre1 in self.vertices and verticeNombre2 in self.vertices:
            vertice1 = self.vertices[verticeNombre1]
            vertice2 = self.vertices[verticeNombre2]
            self.vertices[verticeNombre1].AgregarVecino(vertice2)
            self.vertices[verticeNombre2].AgregarVecino(vertice1)
            return True
        else:
            return False

    def printGrahp(self):
        for nombreVertice in self.vertices.keys():
            print(nombreVertice+"->"+str(self.vertices[nombreVertice].vecinos))
    def BFS(self,nombreStart):
        lnodosvisitados = []
        for u in self.vertices.values():
            u.color = "white"
            u.distancia=sys.maxsize
            u.padre = None
        vertiseStart= self.vertices[nombreStart]
        vertiseStart.color="gray"
        vertiseStart.distancia = 0
        vertiseStart.padre = None
        #vertiseStart.ShowData()
        cola = []
        cola.append(vertiseStart)
        while len(cola)>0:
            u = cola.pop(0)
            #u.ShowData()
            for v in u.vecinos:
                if v.color == "white":
                    v.color = "gray"
                    v.distancia=u.distancia+1
                    v.padre = u
                    cola.append(v)
            u.color="black"
            #u.ShowData()
            lnodosvisitados.append(u)
        return lnodosvisitados
    def DFS(self,nombreStart):
        lnodosvisitados = []
        for u in self.vertices.values():
            u.color = "white"
            u.distancia=sys.maxsize
            u.padre = None
        vertiseStart= self.vertices[nombreStart]
        vertiseStart.color="gray"
        vertiseStart.distancia = 0
        vertiseStart.padre = None
        #vertiseStart.ShowData()
        Pila = []
        Pila.append(vertiseStart)
        while len(Pila)>0:
            u = Pila.pop()
            #u.ShowData()
            for v in u.vecinos:
                if v.color == "white":
                    v.color = "gray"
                    v.distancia=u.distancia+1
                    v.padre = u
                    Pila.append(v)
            u.color="black"
            #u.ShowData()
            lnodosvisitados.append(u)
        return lnodosvisitados
    def DistanciaBFS(self,origen,destino):
        l = self.BFS(origen)
        for i in l:
            if destino == i.nombre:
                vd = i
        for i in l:
            if i == vd:
                return i.distancia
    def __RutaBFS(self,VO,VD):
        nodosdelaruta = []
        nodosdelaruta.append(VO)
        tmp = VO 
        while tmp != VD:
            minimo = self.DistanciaBFS(tmp.vecinos[0].nombre,VD.nombre)
            #print(minimo)
            for i in tmp.vecinos:
                rel =self.DistanciaBFS(i.nombre,VD.nombre)
                if minimo > rel and i!=VO:
                    minimo = rel
            for i in tmp.vecinos:
                if self.DistanciaBFS(i.nombre,VD.nombre) == minimo:
                    nodosdelaruta.append(i)
                    tmp = i
        return nodosdelaruta        
    def RutaBFS(self,Origen,Destino):
        nodosdelaruta = []
        vo = self.vertices[Origen]
        vd = self.vertices[Destino]
        print(self.__RutaBFS(vo,vd))

class SistemaMetro:
    def __init__(self):
        self.g = Grafo()
    def EstacionesNodos(self):
        for i in m.lineas:
            for j in i:
                self.g.agregarVertice(j)
    def BuildLinea(self,linea):
        for i in range(len(linea)):
            if i < len(linea)-1:
                self.g.agregarArista(linea[i],linea[i+1])
    def CrearSistema(self):
        for i in m.lineas:
            self.BuildLinea(i)
    def MostrarSistema(self):
        self.g.printGrahp()
    def MetroBFS(self,origen):
        for i in self.g.BFS(origen):
            print("nombre: ",i.nombre,"Distancia: ",i.distancia)
    def MetroDFS(self,origen):
        for i in self.g.DFS(origen):
            print("nombre: ",i.nombre,"Distancia: ",i.distancia)
    def RutaMetro(self,origen,destino):
        print(self.g.RutaBFS(origen,destino))
if __name__ == "__main__":
    metro = SistemaMetro()
    metro.EstacionesNodos()
    metro.CrearSistema()
    """
    #metro.MostrarSistema()
    print("BFS")
    metro.MetroBFS("Universidad")
    print("\n\nDFS")
    metro.MetroDFS("Universidad")
    """
    print("\n\n\tRutas: \n\n\n")
    metro.RutaMetro("Barranca del Muerto","Universidad")
    metro.RutaMetro("San Antonio","Nativitas")
    metro.RutaMetro("Pantitlán","Popotla")
    metro.RutaMetro("Aragón","Obrera")
    