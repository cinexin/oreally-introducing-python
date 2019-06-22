# Old style with %
'''
%s = string
%d = decimal integer
%x = hexadecimal integer
%o = octal integer
%f = decimal float
%e = exponential float
%g = decimal or exponential float
%% = a literal %
'''

print('%s'% 42) 
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)
print('%d%%' % 100)
# String an integer interpolation
actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print('Our cat %s weighs %d pounds' %(cat,weight))

n = 42
f = 7.03
s = 'string cheese'
'%d %f%s' % (n, f, s)

'''
Set a minimum field width of 10 chars for each var
Align them to the right, filling unused spots on the left with spaces
'''
'%10d %10f %10s' % (n, f, s)
# The same, but vars aligned to the left
'%-10d %-10f %-10s' % (n,f,s)
# The same, but vars right aligned (and set width to 4)
'%.4d %.4f %.4s' % (n,f,s)

'''
Get fields from arguments instead of hard-coding them
'''
'%*.*d %*.*f %*.*s' % (10,4,n,10,4,f,10,4,s)

# New style formatting with {}
'{} {} {}'.format(n,f,s)
'{2} {0} {1}'.format(n,f,s)
'{n} {f} {s}'.format(n = 42, f = 7.03, s = 'string cheese')
dict = {'n': 42, 'f': 7.03, 's': 'string cheese'}
'{0[n]} {0[f]} {0[s]} {1}'.format(dict, 'other')
# New style specifying specific format
'{0:d} {1:f} {2:s}'.format(n,f,s)
'{n:d} {f:f} {s:s}'.format(n = 42, f = 7.89, s ='my string')
# Minimum field width = 10, right-aligned (default)
'{0:10d} {1:10f} {2:10s}'.format(n,f,s)
# Minimum field width = 10, right-aligned (explicit)
'{0:>10d} {1:>10f} {2:>10s}'.format(n,f,s)
# Minimum field widht = 10, centered
'{0:^10d} {1:^10f} {2:^10s}'.format(n,f,s)
# Use precision with floats (or strings) but not with integers
'{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n,f,s)
# You can specify fill character too...
'{0:!^100s}'.format('BIG SALE')