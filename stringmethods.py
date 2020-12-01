#string capitalization
s = 'abcd'
print(s.upper())
print(s.lower())

s = 'AbCdEf'
print(s.swapcase())

s = 'a bunch of words'
print(s.capitalize())
s = 'A BUNCH OF WORDS'
print(s.capitalize())
print(s.title())


#string padding
s = 'abcde'
print(s.center(10, '-'))
print(s.ljust(10, '+'))
print(s.rjust(10, '%'))

d = {'a': 1000, 'bcd': 10, 'edfg': 1, 'j': 999}
for key, value in d.items():
	print(f'{key.ljust(10, ".")}{value}')

s = '12345'
print(s.zfill(10))

#tabs are 8 characters

#Searching in strings

s = 'abcdef'
print(s.index('c'))
print(s.index('cd')) #where it starts
print(s.find('cd'))
print(s.find('!'))#if the character is not in the str, -1 returned

s = 'abcdabcdabcd'
print(s.find('a')) #returns first index
print(s.find('a', 2))#returns index after 2
print(s.find('a', 4, 8)) #between [4,8)
print(s.rfind('a')) #first one from the end
print(s.rindex('c')) #same thing ^

print(s.count('b'))

s = '            Sam'
print(s.strip()) #strip() strips ' ' on either side as well as \t,\n
s = '*****Sam*******'
print(s.strip('*'))
s = '*-*-Sam*-*-*-'
print(s.strip('*-'))
print(s.rstrip('*-')) #r/lstrip('*') doesnt seem to work
print(s.lstrip('*-'))

s = 'what a great sentence'
print(s.replace(' ', '__'))
print(s.replace('h', '^^^', 1))
print(s.replace(' ', ''))

#Splitting, partitioning
#any string can  be used for split(), '^^^', '!'

s = 'abc,def,ghi'
print(s.split(',')) #returns list of strings
print(s.split(',', 1)) #max number of cuts, wont return error if there arent enough
print(s.rsplit(',', 1)) #works from the right side
print(s.split()) #cuts at space, tab, \n, anything thats None
print(s.partition(',')) #returns before, delimeter, and after
print(s.rpartition(',')) #from right side

s='abc\ndef\nasd\ng hj'
print(s.splitlines()) #keeps white space inthe string s if needed
print(s.splitlines(keepends=True)) #keeps end of what its cutting by, which is \n


#Str.maketrans and str.translate

s = 'abcdefabcdef'
print(s.replace('a', 'o').replace('c', 'x'))

d = str.maketrans('aei', 'eio')
print(d) #dictionary that contains before:after ascii values

print(s.translate(d))

d = str.maketrans({'a':'e', 'e':'i', 'i':'o'})
print(s.translate(d))

d = str.maketrans('aei', 'eio', 'bc') #the last 'bc' removes them from the dict
print(s.translate(d))

#rot-13
import string
print(string.ascii_lowercase)
backwards = string.ascii_lowercase[13:]+string.ascii_lowercase[:13]
rot13_d = str.maketrans(string.ascii_lowercase, backwards)

s = 'ello mate'
print(s.translate(rot13_d))

#Joining Strings

s = 'abc,def,ghi,fjk'
fields = s.split(',')
t = ' '.join(fields) #glue.join(running_in)
print(t)

lister = ['abc', 'def', 'ghi']
print(''.join(lister))


#str.startswith and str.endswith

print(s.startswith('ab'))
print(s.endswith('ab'))
print(s.startswith(('a', 'y'))) #tuples are able to be used


#Encode and Decode

s = 'abcd'
len(s)


print(s.encode()) #returns a bytestring ('bytes')
print(s.encode('iso-8859-8')) # ASCII + Hebrew
							  # if using a different language, 
							  #.encode('...', errors=ignore) to ignore
print(s.encode('utf-8'))

print(s.encode().decode())

#The str.is* method

s = 'abcd1~'
print(s.isalnum()) #are they letters or int
print(s.isalpha()) #are they letters
print(s.isascii()) #is it ascii (not other language)
s = '1234'
print(s.isdigit()) #can be turned into int?
print(s.isnumeric()) #deals with other languages
print(s.isdecimal()) #stuff like exponents are not decimals

s = 'x'
print(s.isidentifier()) #can it be a variable name/identifier

#isupper(), islower()

print(s.isprintable())
s = '\n'
print(s.isprintable())
s = ' '
print(s.isspace())

s = 'this is a title test'
print(s.istitle()) #don't use numbers it throws an error

s = s.title()
print(s.istitle())

###STR.FORMAT and STR.FORMAT_MAP


name  = 'Sam'
s = 'Hello, {0}. How are you today, {0}?'
print(s.format(name))
print('Mr. {}'.format(name))

print('Mr. {0:>15} {0:^15} {0:15}.'.format(name))
print('Mr. {x:-<15}'.format(x=name))

d = {'a':1, 'b':2, 'c':3}
print('a{a} b{b} c{c}'.format(**d))

a = 100
b = 'hey'
print(f'look, a = {a}, b = {b}')





