import os.path

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

        if type(self.name) != str:
            raise ExamException('il nome non è una stringa')

    def get_data(self):
        #controllo che il file esista
        if os.path.exists(self.name) == False:
            raise ExamException('il file non esiste')


        # Provo ad aprirlo e leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
            return None
        
        if self.can_read == True:
            data = [] #lista che conterrà tutte le liste del dataset
            n_line = 0
            
            #itero ogni riga del file
            for line in my_file:
                elements = line.split(',') #divido gli elementi delle singole righe e li inserisco nella lista elements
                elements[-1] = elements[-1].strip() #tolgo gli eventuali spazi bianchi alla fine dell'ultimo elemento

                #verifico di non essere nell'intestazione e in caso contrario 
                if elements[0] != 'epoch':
                    n_line += 1
                    line_data = [] #creo la lista definitiva che successivamente appenderò in data[]
                    
                    #provo a castare l'oggetto che dovrebbe contenere l'epoch e lo aggiungo a line_data
                    try:
                        line_data.append(int(elements[0]))
                    except:
                        pass

                    
                    #verifico che l'oggetto che dovrebbe contenere la temperatura sia di tipo int o float e in caso provo a convertirlo
                    if type(elements[1]) != int and type(elements[1]) != float:
                        try:
                            float(elements[1])
                        except:
                            pass
                    #aggiungo l'oggetto temperatura a line_data
                    line_data.append(elements[1])

                    #aggiungo la lista a data
                    data.append(line_data)

            for i in range(1, len(data)):
                if data[i][0]<=data[i-1][0]:
                    raise ExamException('i dati non sono in ordine cronologico')
                    
            return data

def compute_daily_max_difference(time_series):
    max_diff = []
    lenght = len(time_series)

    for i in range(0, lenght):
      same_day_data = []
      same_day_data.append(time_series[i]) #appendo il primo elemento che userò per confrontare

        #for che itera tutti gli altri elementi della time series
      for j in range(i+1, lenght):
        
        if (time_series[j][0]-(time_series[j][0]%86400)) == (same_day_data[0][0]-(same_day_data[0][0]%86400)):
                same_day_data.append(time_series[j])
        else:
          break
          
      max_diff.append((compute_diff(same_day_data)))
      
    
    return max_diff


def compute_diff(same_day_data):
    same_day_temp = []

    if len(same_day_data) < 2:
        return None

    for item in same_day_data:
        same_day_temp.append(float(item[1]))
    
    single_max_diff = float(max(same_day_temp) - min(same_day_temp))

    return single_max_diff



time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
# print(time_series)
# print(len(time_series))


max_diff = compute_daily_max_difference(time_series)
print(max_diff)
#print(len(max_diff))

    
