#non va, autograding dà 2.0 come voto


class CSVFile:

  def __init__(self, name):
    self.name = name
    
    if type(self.name) != str:
      raise Exception('il nome non è una stringa')

    self.can_read = True

    #controllare se il file aperto non è vuoto
    try:
      my_file = open(self.name, 'r')
      my_file.readline()
    except Exception as e:
      self.can_read = False
      print('Errore in apertura del file: "{}"'.format(e))

  def get_data(self, start = None, end = None):

    #se il file non è leggibile ritorna None
    if self.can_read == False:
      print('Errore: file vuoto o illeggibile')
      return None
    else:
      
      my_file = open(self.name, 'r')  
      
      n_righe = 0
      data = []
      tmp_data = []
      
      for line in my_file:
        elements = line.split(',')
        elements[-1] = elements[-1].strip()

        if elements[0] != 'Date':

          tmp_data.append(elements)
          
      n_righe = len(tmp_data)
      
      
      my_file.close()
      
#------Test su start end------------------------
      if start == 0:
        raise Exception("la riga 0 non esiste")
      
      if start == None and end == None: data = tmp_data
      
      if start == None and end != None:
        raise Exception("non c'è uno start")
        return None
        
      if end == None and start != None:
        raise Exception("non c'è una end")
        return None
        
      #start.replace(" ", "")
      #end.replace(" ", "")
      
      if type(start) != int:
        raise Exception("lo start non è un intero")
        return None
        
      if type(end) != int:
        raise Exception("l'end non è un intero")
        return None

      if start > n_righe:
        raise Exception("la riga start non esiste")
        return None

      if end < start:
        raise Exception("start è maggiore di end")
        return None

      if end > n_righe and end > start:
        data = tmp_data
        
#------------------------------------------------------ 
      #for i,line in enumerate(tmp_data):
        #if i in righe:
          #data.append(line)
        #else:
          #pass
        
      data = tmp_data[start:end]
      return data

      



class NumericalCSVFile(CSVFile):

  def get_data(self):

    #metto la lista di liste della prima funzione(lista di righe)
    string_data = super().get_data()

    numerical_data = []

    #scorro ogni lista(row) di string_data
    for row in string_data:

      #variabile temporanea in cui mettere la 1' colonna e le altre convertite
      tmp_data = []

      #scorro gli elementi della lista(riga)
      #enumerate assegna un numero agli elementi, come un indice(i)
      for i, element in enumerate(row):
        #se l'elemento ha indice 0 è la prima colonna, la aggiungo senza convertirla
        if i == 0:
          tmp_data.append(element)

        #se l'indice è diverso da 0 allora non è la prima colonna
        #li aggiungo provando a convertirli in float
        else:
          try:
            tmp_data.append(float(element))
          except:
            print('Elemento colonna non convertibile in float')
            break
        
        #controllo se il numero di elementi della riga corrisponde a quello della riga dopo la conversione
        if len(tmp_data) == len(row):
          numerical_data.append(tmp_data)

    print(str(numerical_data))
    return (numerical_data)
