import math

class ExamException(Exception):
  pass

class Diff():
  def __init__(self, ratio = 1):
    
    #--------sanitizzazione ratio-----
    if ratio == None or ratio == 0:
      raise ExamException("Il ratio non può essere nullo")
      
    if type(ratio) != int and type(ratio) != float:
      raise ExamException("Il ratio deve essere intero")

    if ratio < 1:
      raise ExamException("ratio deve essere positivo")

    if ratio == 0:
      raise ExamException("Il ratio non può essere 0")
    #---------------------------------
    
    self.ratio = ratio 

  def compute(self, my_list):
    
    #--------sanitizzazione lista---------
    if type(my_list) != list:
      raise ExamException("la lista non è una lista")

    for i in range(len(my_list)):
      try:
        float(my_list[i])
      except:
        raise ExamException("Il valore {} non è un numero".format(my_list[i]))

    if len(my_list) == 1:
      raise ExamException("troppi pochi elementi della lista")
      
    #-------------------------------------
    
    diff_list = []

    for i in range(0, len(my_list) -   1):
      diff_list.append(math.fabs((my_list[i] - my_list[i+1])/self.ratio))

    return diff_list

    
#------MAIN--------
# diff = Diff(2)
# result = diff.compute([2,4,8,16])
# print(result)

