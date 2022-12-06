class Model():
	def fit(self, data):
    #fit non implementato nella classe base
		raise NotImplementedError('Metodo non implementato')
    
	def predict(self, data):
    #predict non implementato nella classe base
		raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
  def predict(self, data):
    n = len(data) - 1
    num = 0
    predictation = None
    tmp_data = None

#----------Sanitizzazione data--------------
    if data == None:
      raise Exception("data non esiste")

    if len(data) == 1:
      raise Exception("Non ci sono abbastanza dati")
#-------------------------------------------
    
    #calcolo l'incremento medio
    for item in data:
      if tmp_data != None:
        incremento = item - tmp_data
      else:
        incremento = 0

      tmp_data = item
        
      num = num + incremento
      
    predictation = (num / n) + data[-1]
    print(predictation)

    return predictation
    

data = {'1':1,'2':2,'3':3}
# data = [50, 52, 60]
model = IncrementModel()
print(model.predict(data))


    
    
      
      
      
      
      
      
      