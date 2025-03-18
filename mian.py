#num_primo = [n for n in range(2,22) if all(n % i != 0 for i in range(2,n-1))]
#print(num_primo)


#************************************
#COMPITO LAB DI PROG 1


#1)

class CSVTimeSeriesFile:

    def __init__(self, mySeriesFiles):
        self.name = mySeriesFiles

    def get_data(self, country):
        with open( self.name, "r") as files:
            lista = []
            for linea in files:
                linea = linea.strip().split(",")
                if linea[2] == country:
                    lista.append(linea)
            for element in lista:
                anno = element[0]
                anno = anno.strip().split("-")
                data = anno[0]
                linea[0] = data
                del(element[2])
                try:
                    element[1] = float(element[1])
                    element[1] = round(element[1], 3)
                except:
                    continue
            for elemento in lista:
                elet = elemento[0].strip().split("-")
                elemento[0] = elet[0]
            return lista   # qui abbiamo la lista di liste contenendo ogni anno sotto forma stringa con la sua temperatura sotto forma float

time_series_file = CSVTimeSeriesFile(r"C:\Users\delma\Downloads\GlobalLandTemperaturesByCountry.csv")
time_series_italy = time_series_file.get_data(country="Italy")
print(time_series_italy)


##2) calcoliamo le vairazioni

def calcolo_media(time_series_1):
    dictionary = {}
    for 





            
        

        

