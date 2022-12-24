from utils.initializer import translate, fillZero, chunker

def preprocessMessage(message):
    '''
        preprocess the message to be encrypted
    '''
    bits = translate(message) # translate input message into a binary value(stored as a list)
    length = len(bits)
    message_len = [int(b) for b in bin(length)[2:].zfill(64)] #translate the length of message into a 64bits binary value

    # if the length of the binary message is less than 448(after being concatenated with message_len, less than 512).
    # the final output will be padded to 512 and returned directly without chunking
    if length < 448:
        bits.append(1)
        bits = fillZero(bits, 448, 'LE')
        bits = bits + message_len
        return [bits]

    # if the length of the binary is between 448 and 512, substitute the last 64bits with message_len 
    elif 448 <= length <= 512:
        bits.append(1)
        bits = fillZero(bits, 1024, 'LE')
        bits[-64:] = message_len
        return chunker(bits, 512)

    # if the length of the binary is more than 512, padding with 0 until the final 
    # length(concatenated with the message_len) reach the mutiple of 512. the final 
    # output will be chunked
    else:
        bits.append(1)
        while (len(bits)+64) % 512 != 0:
            bits.append(0)
        bits = bits + message_len
        return chunker(bits, 512)

# if __name__ == '__main__':
#     chunked = preprocessMessage('rememberOurSummerFarAwayFromHomeDoItScaredToBeLonelyDrownSoFarAwayWaitingForTomorrowThereForYou')
#     print('finished!')
