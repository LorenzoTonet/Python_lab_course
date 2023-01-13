import math

class Model():
  def __init__(self, window):
    self.window = window
  
  def fit(self, data):
    #fit non implementato nella classe base
    raise NotImplementedError('Metodo non implementato')
  
  def predict(self, data):
    #predict non implementato nella classe base
	  raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
  
  def comp_avg_increment(self, data):
    
    #QUESTA FUNZIONE FA SIA IL CALCOLO CHE IL CONTROLLO OGNI VOLTA CHE VIENE RICHIAMATA QUINDI HO LA SICUREZZA CHE CONTROLLI TUTTI I DATI
    #----------Sanitizzazione data--------------
    if data == None:
      raise Exception("data non esiste")

    if type(data) != list:
      raise TypeError("data non è una lista")

    if len(data) <= 1:
      raise Exception("Non ci sono abbastanza dati")

    try:
      data[0] = float(data[0])
    except:
      raise TypeError("non convertibile a float")

    #-------------------------------------------
    
    n = len(data) - 1
    num = 0
    tmp_data = None
    
    for item in data:
      if tmp_data != None:
        try:
          item = float(item)
          incremento = item - tmp_data #l'incremento è dato dall' valore attuale meno quello precedente
        except:
          raise TypeError("non convertibile a float")
          
      else:
        incremento = 0

      tmp_data = item #tmp_data è una variabile temporanea che tiene conto dei dato precedente per calcolare l'incremento
        
      num = num + incremento #numeratore che somma man mano gli incrementi

    avg_increment = num / n #calcolo dell'incremento medio |somma degli incrementi diviso il numero di elementi
    return avg_increment

  def predict(self, data):
    
    average_increment = self.comp_avg_increment(data)
    prediction = data[-1] + average_increment

    return prediction

  def evaluate(self, ev_dataset):

    somma = 0
    #lista di valori di test durante il test
    test_values = []
    expected_values = []
    #calcolo dei valori di test
    for i in range (0, len(ev_dataset) - self.window):
      test_values.append(self.predict(ev_dataset[i: i + self.window]))
      try:
        expected_values.append(ev_dataset[i+3]) #aggiunge alla lista dei valori attesi il valore nella posizione dopo la finestra
      except:
        pass

    #lista contenente le tuple
    list_of_tuples = []
    for i in range(len(test_values)):

      #my_tuple = ([valori reali] [valori predetti] [errore])
      my_tuple = (expected_values[i], test_values[i], expected_values[i] - test_values[i])
      list_of_tuples.append(my_tuple)

      print("{}, {}, {}".format(my_tuple[0], my_tuple[1], my_tuple[2]))

    for item in list_of_tuples:
      somma = somma + math.fabs(item[2])
      print(somma)
    errore_medio = somma / len(list_of_tuples)

    return errore_medio
    
class FitIncrementModel(IncrementModel):
  
  def fit(self, fit_data):
    self.global_avg_increment = self.comp_avg_increment(fit_data)

  def predict(self, data):
    
    actual_increment = self.comp_avg_increment(data)
    prediction = data[-1] + (self.global_avg_increment + actual_increment)/2

    return prediction
    

test_data = [67, 72, 72, 67, 72]
model = IncrementModel(3)
print(model.evaluate(test_data))

      