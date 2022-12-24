def initializer(hex_list):
    '''
        Transform a list of hex values into a list of binary values. 

        The input of hex values are stored as strings. And the function 
        will generate binary values corresponded to each hex value.Each 
        binary value is stored as a list of int values. 
    '''
    binary_list = []
    for hex in hex_list:
        binary = bin(int(hex,16))[2:].zfill(8)
        _binary = []
        for i in range(32 - len(binary)):
            _binary.append(0)
        for c in binary:
            _binary.append(int(c))
        binary_list.append(_binary)

    return binary_list

def translate(message):
    '''
        Generate bits notation for a given message.

        The message is a string without space, for example, 'HelloWorld'.
        The output bits notation is a list containing only 0 and 1.
    '''
    num_notations = [ord(c) for c in message]
    binary_notations = [bin(c)[2:].zfill(8) for c in num_notations]
    bits_notations = []
    for notation in binary_notations:
        for c in notation:
            bits_notations.append(int(c))
    return bits_notations

def fillZero(bits, length=8, config='LE'):
    '''
        This function solves the problem that binary value represented by 
        a list of bits might don't reach the required length. The input 
        bits should be a list containing only 0 and 1, and the required 
        length should be given(or use the default value). The config decides 
        the side to pad zero(LE: right, BE: left)
    '''
    zeros = []
    for i in range(len(bits), length):
        zeros.append(0)
    if config == 'LE':
        filled = bits + zeros
    else:
        filled = zeros + bits
    return filled

def chunker(bits, length=8):
    '''
        This function split a single list of binary values into lists of the 
        given length(the default length is 8).
    '''
    chunked = []
    _chunked = []
    counter = 0
    for bit in bits:
        _chunked.append(bit)
        counter += 1
        if counter == length:
            chunked.append(_chunked)
            _chunked = []
            counter = 0
    if counter != 0:
        chunked.append(_chunked)
    return chunked

def b2Tob16(value):
    '''
        This function will transform a binary value into a hex representation
    '''
    str_value = ''
    for v in value:
        str_value += str(v)
    return hex(int(str_value, 2))[2:]
