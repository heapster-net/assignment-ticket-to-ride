import sys
print 'digraph G {'
print 'edge [arrowhead=none]'
with open(sys.argv[1], 'r') as f:
    for line in f:
        x = line.split()
        print x[0] + ' -> ' + x[1] + ' [label="' + x[2] + '"]'
print '}'
