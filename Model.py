class Model():
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
    
    
class FitIncrementModel(IncrementModel):
  
  def fit(self, data):
    self.global_avg_increment = self.comp_avg_increment(data)

  def predict(self, data):
    
    actual_increment = self.comp_avg_increment(data)
    prediction = data[-1] + (self.global_avg_increment + actual_increment)/2

    return prediction
    
    

# data = {'1':1,'2':2,'3':3}
# data = [50, 52, 60]
# model = IncrementModel()
# print(model.predict(data))


    
    
      
      
      
      
      
      
      