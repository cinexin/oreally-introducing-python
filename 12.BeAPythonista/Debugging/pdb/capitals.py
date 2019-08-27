def process_cities(filename):
    "Process cities and its capitals as they appear in countries.txt"
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            if 'quit' == line.lower():
                return
            country, city = line.split(',')
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=',')


'''
When we try to process "countries2.txt", we find not all the countries are processed...
wtf?
use the debugger! 
pythomn -m pdb capitals.py countries2.txt
'''
if __name__ == "__main__":
    import sys
    process_cities(sys.argv[1])
