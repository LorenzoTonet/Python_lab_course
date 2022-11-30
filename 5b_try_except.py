#non va, autograding dà 2.0 come voto


class CSVFile:

  def __init__(self, name):
    self.name = name

    self.can_read = True

    #controllare se il file aperto non è vuoto
    try:
      my_file = open(self.name, 'r')
      my_file.readline()
    except Exception as e:
      self.can_read = False
      print('Errore in apertura del file: "{}"'.format(e))

  def get_data(self):

    #se il file non è leggibile ritorna None
    if self.can_read == False:
      print('Errore: file vuoto o illeggibile')
      return None
    else:
      my_file = open(self.name, 'r')

      data = []

      for line in my_file:
        elements = line.split(',')
        elements[-1] = elements[-1].strip()

        if elements[0] != 'Date':

          data.append(elements)

      my_file.close()

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
