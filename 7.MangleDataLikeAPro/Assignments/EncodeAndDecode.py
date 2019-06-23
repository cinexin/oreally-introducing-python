'''
7.1 Create a Unicode a string called mystery and assing it the value
'\U0001f4a9'
'''
mystery = '\U0001f4a9'
print(mystery)
import unicodedata
name = unicodedata.name(mystery)
print(name)
'''
7.2. Encode mustery, this time using UTF-8, into the bytes var pop_bytes
'''
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)
'''
7.3. Usign UTF-8, decode pop_bytes into the string var pop_string
'''
decoded_pop = pop_bytes.decode('utf-8')
print(decoded_pop)
