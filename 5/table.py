#layout = '{0}:\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\n'
layout = '{0:>2}:{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}' \
         '{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>5}'
layoutb = '{0:>7}{1:>5}{2:>5}{3:>5}{4:>5}{5:>5}' \
          '{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}'
#for x in range(12):
 #   print('\t'+str(x+1),end='')
print(layoutb.format(1,2,3,4,5,6,7,8,9,10,11,12))
print('  :-------------------------------------------------------------------------------------------------')
for z in range(12):
    x = z +1 
    print(layout.format(x*1,x*1,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9,x*10,x*11,x*12))
    
