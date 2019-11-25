

CODE = {'a': '.-',     'b': '-...',   'c': '-.-.',
        'd': '-..',    'e': '.',      'f': '..-.',
        'g': '--.',    'h': '....',   'i': '..',
        'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',
        'p': '.--.',   'q': '--.-',   'r': '.-.',
        's': '...',    't': '-',      'u': '..-',
        'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  ' ': ' '
        }




def Filter(message):
    output = list(message.lower())
    outputcopy = list(message.lower())
    for i in outputcopy:
        if i not in list(CODE.keys()):
            output.remove(i)

    output = ''.join(output)
    output = ' '.join(output.split())  # get rid of multiple spaces
    return output



def MorseTranslate(message):
    message = list(Filter(message))
    morse_out = []
    for letter in message:
        morse_letter = CODE[letter]
        morse_out.append(morse_letter)

    morse_out = ' '.join(morse_out)
    return morse_out    
    

