result = []
def divider(a, b):
 try:
  if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
   raise TypeError('Ключ или значение не является числом')
  if a < b:
   raise ValueError('a меньше чем b')
  if b > 100:
   raise IndexError('b больше чем 100')
  return a/b
 except Exception as e:
  print(f'Ошибка: {e}')
  return None
 
data = {10: 2, 2: 5, "123": 4, 18: 0, 8 : 4}
for key,value in data.items():
  try:
    res = divider(key, value)
    if res is not None:
      result.append(res)
  except Exception as e:
    print(f'Ошибка при обработке {key}: {e}')


print(result)