### @Author = Sandeep Anand
# This is a Code to test best scrap methodology
'''
1. Use of Beutiful soup 4 to extract the html data
2. Use of a Json formatter to obtain the Json string
3. Json string is extracted into a dictionary
4. Defining and using of recursive function
'''
###############################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import string
import json

url_ex1 = "https://finance.yahoo.com/quote/NVDA/key-statistics?p=NVDA"
page = urlopen(url_ex1)
soup = BeautifulSoup(page.read(), 'html.parser')
count =0
count_line = 0

# First Recursive Defining a Recursive Function
def key_gen_recursion(d, indent=' ', braces=1):
    """ Recursively prints nested dictionaries."""
    for key, value in d.items():
        if isinstance(value, dict):
            print('%s%s%s%s' % (indent, braces * '[', key, braces * ']'))
            key_gen_recursion(value, indent + '  ', braces + 1)
        else:
            print(indent + '%s = %s' % (key, value))

# Second Recursive Function to tried ie, somewhat better , Also takes Lists into Consideration
'''
Taken from: http://code.activestate.com/recipes/578094-recursively-print-nested-dictionaries/
'''
def recursive_print(src, dpth=0, key=''):
    """ Recursively prints nested elements."""
    tabs = lambda n: ' ' * n * 4  # or 2 or 8 or...
    brace = lambda s, n: '%s%s%s' % ('[' * n, s, ']' * n)

    if isinstance(src, dict):
        for key, value in src.items():
            print(tabs(dpth) + brace(key, dpth))
            recursive_print(value, dpth + 1, key)
    elif isinstance(src, list):
        for litem in src:
            recursive_print(litem, dpth + 2)
    else:
        if key:
            print(tabs(dpth) + '%s = %s' % (key, src))
        else:
            print(tabs(dpth) + '- %s' % src)

# final_page stores the whole line as a string everything line wise
for line in soup:
    count += 1
    if count == 2:
        final_page = str(line)

tempstr = final_page.split("root.App.main")[1].strip().split("(this)")[0].strip()
#pat1 =  re.match(r'^= (.*?)',str(tempstr),re.IGNORECASE)
#m = pat1.match(tempstr)

print("\n", len(tempstr))
jsonstrinng =  tempstr[2:len(tempstr)-3]
jsondata = json.loads(jsonstrinng)

#Calling the Function for Getting all the Keys and the values
recursive_print(jsondata["context"])

