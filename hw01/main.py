for i in range(1,10):
    print(end=' '*7*(i-1))
    for j in range(i,10):
        formula = '{0:1}*{1:1}={2:>2}'
        print(formula.format(i,j,i*j),end =' ')
    print()
