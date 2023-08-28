import sys
import binascii
import itertools

def make_crc(filename):
    with open(filename, 'rb') as fp:
        data = fp.read()
        return binascii.crc32(data, 0) & 0xffffffff
    
if __name__ == '__main__':
    for e in map(lambda e: e[1],
                 filter(lambda e: len(e[1]) > 1,
                        map(lambda e: (e[0], list(e[1])),
                            itertools.groupby(sorted(map(lambda e: (make_crc(e), e), sys.argv[1:])),
                                              lambda e: e[0])))):
        crc = e[0][0]
        filenames = list(map(lambda data: data[1], e))
        print(f'{crc}\t{filenames}')

        
        
