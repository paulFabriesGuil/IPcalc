#! /usr/bin/python
#
#for cidr in range(33):
#    first_part='1'*cidr
#    second_part='0'*(32-cidr) #right
#    mask_bin = first_part+second_part
#    ip_number = int(mask_bin, 2)
#    bytefication = ip_number.to_bytes(4,'big')
#    byar = bytearray(bytefication)
#    asad = int.from_bytes(byar, byteorder = 'big')
#    bytefication = asad.to_bytes(4,'big')
#    ip_number = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(bytefication[0]),int(bytefication[1]),int(bytefication[2]),int(bytefication[3])))
#    result = ip_number.split('.')
#    print(('{0}.{1}.{2}.{3}'.format(int(result[0],2),int(result[1],2),int(result[2],2),int(result[3],2))))
#    for by in byar:
#        str_by= str(by)
#        asad += str_by + "."
#    asad = asad[:-1]
#    print(asad)


#number = 192
#bin_num = number.to_bytes(1,'big')
#bin_num = str(bin_num)[4:-1]
#print(bin_num)
print(hex(192)[2:])
#conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
#                    5: '5', 6: '6', 7: '7',
#                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
#                    13: 'D', 14: 'E', 15: 'F'}
#
#number = str(192)
#number = '{0:08b}'.format(int(number))
#firstletter = '0'*4+number[:4]
#secondletter = '0'*4+number[4:]
#print(firstletter, secondletter)
#firstletter = conversion_table[int(firstletter,2)]
#secondletter = conversion_table[int(secondletter,2)]
#print(firstletter+secondletter)