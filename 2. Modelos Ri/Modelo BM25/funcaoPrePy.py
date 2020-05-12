import numpy as np
from os.path import isfile
from re import sub
import re

# passa como parametro um arquivo de tokens e o transforma em uma lista de tuplas
def removeSpacePy(texto):
    for i in range(len(texto)):
        texto[i] = texto[i].replace("\n", "")
        texto[i] = texto[i].replace("\\n", "")
        texto[i] = texto[i].replace(" ", "AB")
        texto[i] = texto[i].replace("\s", "")
        texto[i] = texto[i].replace("\t", "")
        texto[i] = texto[i].replace("0", "")
        texto[i] = texto[i].replace("1", "")
        texto[i] = texto[i].replace("2", "")
        texto[i] = texto[i].replace("3", "")
        texto[i] = texto[i].replace("4", "")
        texto[i] = texto[i].replace("5", "")
        texto[i] = texto[i].replace("6", "")
        texto[i] = texto[i].replace("7", "")
        texto[i] = texto[i].replace("8", "")
        texto[i] = texto[i].replace("9", "")
        
    for i in range(len(texto)):
        x = texto[i]
        texto[i] = re.sub(r'#.*', '#', x) 
    return texto


def tokensWordsPy(texto):
    for i in range(len(texto)):
        texto[i] = texto[i].replace("staticmethod", 'fd')

        texto[i] = texto[i].replace('classmethod', 'cw')
        texto[i] = texto[i].replace('memoryview' ,'ei')
        
        texto[i] = texto[i].replace('issubclass', 'ea')
        texto[i] = texto[i].replace('isinstance' ,'dz')
        texto[i] = texto[i].replace('frozenset', 'do')
        texto[i] = texto[i].replace('property', 'es')
        texto[i] = texto[i].replace('callable', 'cv')
        texto[i] = texto[i].replace('nonlocal', 'ce')
        texto[i] = texto[i].replace('continue', 'bo')
        texto[i] = texto[i].replace('copyright', 'db')
        texto[i] = texto[i].replace('bytearray', 'ct')
        texto[i] = texto[i].replace('enumerate', 'dh')
        texto[i] = texto[i].replace('finally', 'bu')
        
        texto[i] = texto[i].replace('compile' ,'cz')
        texto[i] = texto[i].replace('complex', 'da')
        texto[i] = texto[i].replace('delattr' ,'dd')
        texto[i] = texto[i].replace('credits', 'dc')
        texto[i] = texto[i].replace('getattr', 'dp')
        texto[i] = texto[i].replace('globals', 'dq')
        texto[i] = texto[i].replace('license', 'ed')
        texto[i] = texto[i].replace('reverse', 'ex')
        texto[i] = texto[i].replace('hasattr', 'dr')
        texto[i] = texto[i].replace('setattr', 'fa')
        texto[i] = texto[i].replace('return', 'ci')
        texto[i] = texto[i].replace('divmod', 'dg')
        texto[i] = texto[i].replace('random', 'bf')
        texto[i] = texto[i].replace('assert', 'bl')
        texto[i] = texto[i].replace('except', 'bt')
        texto[i] = texto[i].replace('global', 'bw')
        texto[i] = texto[i].replace('import', 'ca')
        texto[i] = texto[i].replace('lambda', 'cd')
        texto[i] = texto[i].replace('format', 'dn')
        texto[i] = texto[i].replace('locals', 'ef')
        texto[i] = texto[i].replace('object', 'em')
        texto[i] = texto[i].replace('sorted', 'fc')
        texto[i] = texto[i].replace('raise', 'ch')
        texto[i] = texto[i].replace('numpy', 'bc')
        texto[i] = texto[i].replace('False', 'bh')
        texto[i] = texto[i].replace('True','bj')
        
        
        texto[i] = texto[i].replace('break', 'bm')
        texto[i] = texto[i].replace('class', 'bn')
        texto[i] = texto[i].replace('yield', 'cm')
        texto[i] = texto[i].replace('while', 'ck')
        texto[i] = texto[i].replace('ascii', 'cq')
        texto[i] = texto[i].replace('bytes', 'cu')
        texto[i] = texto[i].replace('filter', 'dl')
        texto[i] = texto[i].replace('round', 'ew')
        texto[i] = texto[i].replace('float', 'dm')
        texto[i] = texto[i].replace('input', 'dx')
        texto[i] = texto[i].replace('print', 'er')
        texto[i] = texto[i].replace('range', 'eu')
        
        texto[i] = texto[i].replace('slice', 'fb')
        texto[i] = texto[i].replace('super', 'fg')
        texto[i] = texto[i].replace('tuple ','fh')
        texto[i] = texto[i].replace('math ','bg')
        texto[i] = texto[i].replace('None', 'bi')
        texto[i] = texto[i].replace('elif', 'br')
        texto[i] = texto[i].replace('else', 'bs')
        texto[i] = texto[i].replace('from', 'bx')
        texto[i] = texto[i].replace('pass', 'cg')
        texto[i] = texto[i].replace('with', 'cl')
        texto[i] = texto[i].replace('bool', 'cs')
        texto[i] = texto[i].replace('dict', 'de')
        texto[i] = texto[i].replace('eval', 'di')
        texto[i] = texto[i].replace('exec', 'dj')
        texto[i] = texto[i].replace('exit', 'dk')
        texto[i] = texto[i].replace('help', 'dt')
        texto[i] = texto[i].replace('iter', 'eb')
        texto[i] = texto[i].replace('list', 'ee')
        texto[i] = texto[i].replace('next' ,'el')
        texto[i] = texto[i].replace('open' ,'eo')

        texto[i] = texto[i].replace('quit', 'et')
        texto[i] = texto[i].replace('repr', 'ev')
        texto[i] = texto[i].replace('type', 'fi')
        texto[i] = texto[i].replace('vars', 'fj')
        texto[i] = texto[i].replace('and', 'ba')

        texto[i] = texto[i].replace('sys', 'bd')

        texto[i] = texto[i].replace('def', 'bp')
        texto[i] = texto[i].replace('bel', 'bq')  
        texto[i] = texto[i].replace('for', 'bv')  
        texto[i] = texto[i].replace('not', 'cf')  
        texto[i] = texto[i].replace('hex', 'du')  
        texto[i] = texto[i].replace('int', 'dw')
        texto[i] = texto[i].replace('len', 'ec')   
        texto[i] = texto[i].replace('map','eg')
        texto[i] = texto[i].replace('max', 'eh')
        texto[i] = texto[i].replace('min', 'ej')
        texto[i] = texto[i].replace('oct', 'en')
        texto[i] = texto[i].replace('ord', 'ep')
        texto[i] = texto[i].replace('pow', 'eq')
        texto[i] = texto[i].replace('set' ,'ez')
        texto[i] = texto[i].replace('str', 'fe')
        texto[i] = texto[i].replace('sum', 'ff')
        texto[i] = texto[i].replace('zip', 'fl')
        texto[i] = texto[i].replace('try', 'cj')
        texto[i] = texto[i].replace('abs', 'cn')
        texto[i] = texto[i].replace('all', 'co')
        texto[i] = texto[i].replace('any', 'cp')
        texto[i] = texto[i].replace('bin', 'cr')
        texto[i] = texto[i].replace('chr', 'cx')
        texto[i] = texto[i].replace('dir', 'df')
        texto[i] = texto[i].replace('id', 'dv')
        texto[i] = texto[i].replace('or', 'bb')
        texto[i] = texto[i].replace('os', 'be')
        texto[i] = texto[i].replace('as', 'bk')
        texto[i] = texto[i].replace('if', 'bz')
        texto[i] = texto[i].replace('in', 'cb')
        texto[i] = texto[i].replace('is', 'cc')
    return texto