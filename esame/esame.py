import os.path

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
  def __init__(self, name):
    self.name = name

    #se il nome non è una stringa alza un'eccezione
    if type(self.name) != str:
      raise ExamException('il nome non è una stringa')

  def get_data(self):
    if os.path.exists(self.name) == False:
      raise ExamException('il file non esiste')
      
    self.can_read = True
    
    try:
      my_file = open(self.name, 'r')
      my_file.readline()
    except:
      self.can_read = False
      raise ExamException('Errore in apertura del file')

    if self.can_read == True:
      data = []

      #itero tutte le righe del file dividendo le colonne
      for line in my_file:
        elements = line.split(',')
        #dall'ultimo elemento toglie lo spazio
        elements[-1] = elements[-1].strip()

        if elements[0] != 'epoch':
          line_data = []

          #casto l'epoch a int e se non ci riesco passo all'iterazione succ.
          try:
            line_data.append(int(elements[0]))
          except:
            continue

          #casto la temperatura a float e se non ci riesco passo all'iterazione succ.
          if type(elements[1]) != int and type(elements[1]) != float:
            try:
              float(elements[1])
            except:
              continue

            line_data.append(elements[1])
            
            data.append(line_data)

      #controllo che le epoch siano in ordine/non duplicati
      for i in range(1, len(data)):
        if data[i][0] <= data[i-1][0]:
          raise ExamException('i dati non sono in ordine cronologico')

      return data


def compute_daily_max_difference(time_series):
  max_diff_list = []
  lenght = len(time_series)
  i = 0

  #itero la lista di liste
  while i < lenght:
    #lista di dati di un nuovo giorno
    same_day_data = []
    #appendo il primo valore del primo giorno che userò per confrontarlo con gli altri
    same_day_data.append(time_series[i])

    #itero gli elementi successivi all'elemento che ho inserito nella lista
    for j in range(i+1, lenght):
      start_day = time_series[j][0]-(time_series[j][0]%86400)

      #se l'inizio del giorno è uguale significa che il dato j-esimo è del giorno che sto analizzando
      if start_day == (same_day_data[0][0]-(same_day_data[0][0]%86400)):
        same_day_data.append(time_series[j])


    #aumento l'indice in modo che l'iterazione successiva parta dal dato del giorno successivo
    i = i + len(same_day_data) + 1

    #calcolo l'escursione termica del giorno che ho preso in analisi e aggiungo il risultato alla lista
    daily_max_diff = compute(same_day_data)
    max_diff_list.append(daily_max_diff)

  return max_diff_list

#funzione che calcola l'escursione termica dai dati di un giorno intero
def compute(same_day_data):
  same_day_temperatures = []

  if len(same_day_data) == 1:
    return None

  for item in same_day_data:
    same_day_temperatures.append(float(item[1]))

  single_day_diff = float(max(same_day_temperatures) - min(same_day_temperatures))

  return single_day_diff


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

max_diff = compute_daily_max_difference(time_series)
      
                                     
                   


