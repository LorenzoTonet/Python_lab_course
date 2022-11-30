def sum_csv(file_name):

  
  my_file = open(file_name, 'r')
  
  valori = []
  n_righe = 1
  

  for line in my_file:
    elements = line.split(',')
    if elements[0] != 'Date':
      valore = elements[1]
      valori.append(float(valore))
      n_righe = n_righe + 1
      
  my_file.close()
  
  if n_righe != 1:
    somma = sum(valori)
    
  else:
    somma = None
    
  return(somma)