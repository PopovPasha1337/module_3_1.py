calls = 0
def count_calls():
  global calls
  calls += 1

def string_info(string):
   count_calls()
   return (len(string)),
   string.upper(), string.lower()
def is_contains(string, les_to_search):
  count_calls()
  string_info = string.lower()
  for item in  les_to_search:
    if item.lower() in string_info:
      return True
      return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic'])) 
print(calls)