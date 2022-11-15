def sum_list(list):
  somma = 0
  
  if len(list) == 0: 
    return None
  
  for item in list:
    somma = somma + item

  return somma
