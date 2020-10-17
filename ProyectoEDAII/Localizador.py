try:
    from geopy.geocoders import Nominatim as Nom
    import metro
    import math as mt
    import GrafoMetro as Subway
except ImportError as e:
    print("\n\n\tNo se pudo importar alguna biblioteca\n\n\tMayor informacion: ",e)
geo = Nom(user_agent="specify_your_app_name_here")
class GeoMetro:
    def __init__(self):
        self.LocMetro = {}
        self.positionSubway = {}
    def Extraerinfo(self):
        print("Geolocalizando cada estacion del metro ...")
        for i in metro.lineas:
            for j in i:
                tmp = []
                try:
                    loc = geo.geocode(f"metro {j} CDMX")
                    direccion = loc.address
                    if direccion == "El Metro, Tlalpan, Ciudad de México, 14000, México":
                        loc = geo.geocode(f"{j} CDMX")
                        direccion = loc.address
                    if j not in self.LocMetro:
                        tmp.append(loc.latitude)
                        tmp.append(loc.longitude)
                        self.LocMetro[j]=tmp
                        #print(f"Las coordenadas de {j} han sido guardadas")
                    #print(direccion)
                    #print(f"Coordenadas: {loc.latitude},{loc.longitude}")
                except AttributeError as e:
                    print("No se ha podido geolocalizar",j)
                except Exception as e:
                    print("Algo ocurrio mal con la estacion: ",j)
        print("El Sistema ha sido geolocalizado")
    def SafeData(self,diccionario):
        lines = []
        for i in diccionario.keys():
            lines.append([f'{i};',f'{diccionario[i][0]};',f'{diccionario[i][1]}\n'])
        try:
            with open('DataBase.txt','w') as F:
                for i in lines:
                    F.writelines(i)
        except Exception as e:
            #print("\n\n\tAlgo ocrrio mal")
            print(" ")
    def GetData(self):
        try:
            with open('DataBase.txt','r') as F:
                line = True
                while line:
                    line = F.readline().split(';')
                    #print(line)
                    self.LocMetro[line[0]] = [float(line[1]),float(line[2])]
        except Exception as e:
            #print("\n\n\tAlgo ocrrio mal")
            print(" ")
    def Distancia(self,key,user):
        return mt.sqrt(((self.LocMetro[key][0]-user.latitude)**2) + ((self.LocMetro[key][1]-user.longitude)**2))
    def SearchShorterDistance(self,position):
        Distancias = []
        print(position.latitude,position.longitude)
        for i in self.LocMetro.keys():
            #print(self.Distancia(i,position))
            Distancias.append([self.Distancia(i,position),i])
        #print(Distancias) 
        Distancias.sort()
        #print(Distancias)
        lista = []
        for i in range(3):
            lista.append(Distancias[i])
        return lista
class Usuario:
    def __init__(self,origen,destino):
        self.origen = self.ChoosePosition(origen)
        self.destino = self.ChoosePosition(destino)
    def ChoosePosition(self,loc):
        try:
            return geo.geocode(loc)
        except Exception as e:
            print("Algo ocurrio mal")
            return None
class Usuario_ModoManual:
    def __init__(self,latorigen,lonorigen,latdestino,londestino):
        self.origen = [latorigen,lonorigen]
        self.destino = [latdestino,londestino]
    def ChoosePosition(self,loc):
        try:
            return geo.reverse(f"{loc[0]},{loc[1]}")
        except Exception as e:
            print("Algo ocurrio mal")
            return None
class Main:
    def __init__(self):
        res = int(input("\n\n\tpresiona (1) para Entrar/Continuar o (2) para salir\n\n\t:"))
        while(res < 1 or res >2):
            res = int(input("\n\n\tERROR, intentalo de nuevo\n\n\tpresiona (1) para Entrar/Continuar o (2) para salir\n\n\t:"))
        while res == 1:
            opc = int(input("\n\n\t1)Modo manual (Tu mismo ingresas las coordenadas)\n\t2)modo automatico (Solo se ingresa una direccion)\n\t3)salir\n\n\topcion:"))
            while(opc<1 or opc>3):
                opc = int(input("\n\n\tERROR, intentalo de nuevo\n\n\t1)Modo manual (Tu mismo ingresas las coordenadas)\n\t2)modo automatico (Solo se ingresa una direccion)\n\t3)salir\n\n\topcion:"))   
            if opc == 1:
                self.ModoManual()
            elif opc == 2:
                self.ModoAutomatico()
            elif opc == 3:
                res = 2
            res = int(input("\n\n\tpresiona (1) para Entrar/Continuar o (2) para salir\n\n\t:"))
            while(res < 1 or res >2):
                res = int(input("\n\n\tERROR, intentalo de nuevo\n\n\tpresiona (1) para Entrar/Continuar o (2) para salir\n\n\t:"))
        print("\n\n\tHasta luego\n\n\t")
    def ModoManual(self):
        print("Modo Manual")
        try:
            print("Origen: ")
            latorigen = input("\n\n\tLatitud: ")
            lonorigen = input("\n\n\tLongitud: ")
            print("Destino: ")
            latdestino = input("\n\n\tLatitud: ")
            londestino = input("\n\n\tLongitud: ")
            U1 = Usuario_ModoManual(latorigen,lonorigen,latdestino,londestino)
            Origen = prueba.SearchShorterDistance(U1.ChoosePosition(U1.origen))
            Destino = prueba.SearchShorterDistance(U1.ChoosePosition(U1.destino))
            #print("\n\n\tOrigen: ",Origen,"\n\n\tDestino: ",Destino)
            print("Mejores rutas: ")
            for i in range(3):
                print("\n\nRuta ",i+1,":\n")
                print("Origen: ",Origen[i][1],"-> Destino: ",Destino[i][1])
                metro.RutaMetro(Origen[i][1],Destino[i][1])    
        except Exception as e:
            print("Algo ocurrio mal",e)
    def ModoAutomatico(self):
        print("Modo Automatico")
        try:
            Actual = input("Origen: ")
            Final = input("Destino :")
            U1 = Usuario(f"{Actual} CDMX",f"{Final} CDMX")
            Origen = prueba.SearchShorterDistance(U1.origen)
            Destino = prueba.SearchShorterDistance(U1.destino)
            #print("\n\n\tOrigen: ",Origen,"\n\n\tDestino: ",Destino)
            print("Mejores rutas: ")
            for i in range(3):
                print("\n\nRuta ",i+1,":\n")
                print("Origen: ",Origen[i][1],"-> Destino: ",Destino[i][1])
                metro.RutaMetro(Origen[i][1],Destino[i][1])    
        except Exception as e:
            print("Algo ocurrio mal",e)
if __name__ == "__main__":
    print("\n\n\tPrecaucion, este programa utiliza la biblioteca geopy")
    prueba = GeoMetro()
    #prueba.Extraerinfo()
    #prueba.SafeData(prueba.LocMetro)
    prueba.GetData()
    #print(prueba.LocMetro)
    metro = Subway.SistemaMetro()
    metro.EstacionesNodos()
    metro.CrearSistema()
    menu = Main()