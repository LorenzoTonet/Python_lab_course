#stampa a schermo un messaggio di errore se si cerca di aprire un file vuoto

class CSVFile:
  def __init__(self, name):
    self.name = name

  def get_data(self):
    try:
      my_file = open(self.name, 'r')
    
      valori = []
  
      for line in my_file:
        elements = line.split(',')
        if elements[0] != 'Date':
          elements[1] = elements[1].replace("\n", "")
          valori.append(elements)
    except:
      print('Errore')
        
    my_file.close()

    return(valori)