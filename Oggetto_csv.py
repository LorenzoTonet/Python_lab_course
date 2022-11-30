class CSVFile:
  def __init__(self, name):
    self.name = name

  def get_data(self):
    my_file = open(self.name, 'r')
  
    valori = []
  
    for line in my_file:
      elements = line.split(',')
      if elements[0] != 'Date':
        elements[1] = elements[1].replace("\n", "")
        valori.append(elements)
        
    my_file.close()

    return(valori)