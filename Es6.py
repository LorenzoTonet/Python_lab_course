class CSVFile:

  def __init__(self, name):
    self.name = name
    
    if type(self.name) != str:
      raise Exception('il nome non è una stringa')

  def get_data(self, start = None, end = None):

    #prova ad aprire il file, se non si apre alza un'eccezione
    try:
      myfile = open(self.name, 'r')
    except Exception as e:
      print('Il file non risulta apribile per il seguente errore "{}"'.format(e))
      return None

    #creo una variabile in cui mettere tutti i dati da cui successivamente rimuoverò quelli non interessti
    tmp_data = []
    data = []

    #scorro ogni linea del file e creo ogni volta una lista che contiene le stringhe divise dalla virgola
    for line in myfile:
      elements = line.split(",")

    #escludo dai dati la prima riga
      # if elements[0] != 'Data':

        #tolgo da ogni riga il carattere speciale che fa andare a capo
      elements[-1] = elements[-1].strip("\n")
      tmp_data.append(elements)

    lunghezza = len(tmp_data)

    
#-----------Sanitizza start/end-----------------------------
    
    if type(start) != int and start != None:
      try:
        start = int(start)
      except: 
        raise Exception("start non convertibile")

    if type(end) != int and end != None:
      try:
        end = int(end)
      except:
        raise Exception("end non convertibile")
      
    if start == 0:
      raise Exception("la riga 0 non esiste")
      

    if start == None and end == None:
      data = tmp_data[1:]

    if type(start)==int and type(end)==int and end < start:
      raise Exception("end è minore di start")
      return None

    if start == None and end != None:
      data = tmp_data[1:]

    if start != None and end == None:
      data = tmp_data[start:]

    if type(start)==int and start < 0:
      raise Exception("Start negativo")

    if type(end)==int and end < 0:
      raise Exception("End negativo")

    if type(start)==int and start > lunghezza:
      raise Exception("la riga di start non esiste")
      
    if type(end)==int and end > lunghezza:
      raise Exception("l'end è dopo la fine")
      
#-----------------------------------------------------------
      
    return data
