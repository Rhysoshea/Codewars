'''
Instructions

The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''


''' Solution '''
def rgb(r, g, b):
    list = [x if x >= 0 else 0 for x in [r,g,b]]
    list = [x if x <= 255 else 255 for x in list]
    return ''.join([('0'+hex(x)[2:].upper()) if len(hex(x)[2:])==1 else hex(x)[2:].upper() for x in list])


# print(rgb(-255,255,211))

''' Best practice solution '''
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
## capital X ensures the characters are capitalized
## :02 ensures each output is 2 characters padded with 0

print(rgb(-255,255,211))
