class ExamException(Exception):
  pass

class MovingAverage():
  def __init__(self, window):
  
    if window == None:
      raise ExamException("window non è stato specificato")
    
    if type(window) != int:
      raise ExamException("La finestra deve essere intera")

    if window < 1:
      raise ExamException("window deve essere positivo")

    if window == 0:
      raise ExamException("La finestra non può essere 0")

    self.window = window

    
  def compute(self, my_list):
    
    avg_list = [] #lista che verrà ritornata

    #-------Sanitizzazione---------------
    if type(my_list) != list:
      raise ExamException("la lista non è una lista")

    if self.window == 1:
      return my_list

    if self.window > len(my_list):
      raise ExamException("La lunghezza della finestra non è valida")

    for i in range(len(my_list)):
      try:
        float(my_list[i])
      except:
        raise ExamException("Il valore {} non è un numero".format(my_list[i]))
    
    #------------------------------------

    for i in range((len(my_list) - self.window) + 1):
      avg_list.append(sum(my_list[i: i + self.window]) / self.window)

    return avg_list




