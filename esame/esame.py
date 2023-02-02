import os.path

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
  def __init__(self, name):
    self.name = name

    if type(self.name) != str:
      raise ExamException('il nome non è una stringa')

  def get_data(self):
    if os.path.exists(self.name) == False:
      raise ExamException('il file non esiste')

    self.can_read = True
    try:
      my_file = open(self.name, 'r')
      my_file.readline()
    except ExamException as e:
      self.can_read = False
      print('Errore in apertura del file: "{}"'.format(e))
      return None

    if self.can_read == True:
      data = []

      for line in my_file:
        elements = line.split(',')
        elements[-1] = elements[-1].strip()

        if elements[0] != 'epoch':
          line_data = []
          
          try:
            line_data.append(int(elements[0]))
          except:
            continue

          if type(elements[1]) != int and type(elements[1]) != float:
            try:
              float(elements[1])
            except:
              continue

            line_data.append(elements[1])
            data.append(line_data)

      for i in range(1, len(data)):
        if data[i][0] <= data[i-1][0]:
          raise ExamException('i dati non sono in ordine cronologico')

      return data

def compute_daily_max_difference(time_series):
  max_diff_list = []
  lenght = len(time_series)
  i = 0

  while i < lenght:
    same_day_data = []
    same_day_data.append(time_series[i])

    for j in range(i+1, lenght):
      start_day = time_series[j][0]-(time_series[j][0]%86400)

      if start_day == (same_day_data[0][0]-(same_day_data[0][0]%86400)):
        same_day_data.append(time_series[j])


    i = i + len(same_day_data) + 1
    daily_max_diff = compute(same_day_data)
    max_diff_list.append(daily_max_diff)

  return max_diff_list

def compute(same_day_data):
  same_day_temperatures = []

  if len(same_day_data) == 1:
    return None

  for item in same_day_data:
    same_day_temperatures.append(float(item[1]))

  single_day_diff = float(max(same_day_temperatures) - min(same_day_temperatures))

  return single_day_diff


time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

max_diff = compute_daily_max_difference(time_series)
print(max_diff)
      
                                     
                   


