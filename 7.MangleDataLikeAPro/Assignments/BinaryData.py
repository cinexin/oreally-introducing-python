'''
7.12. Use unhexlyfy to convert this hex strings to a byte called gif
'''
hex_string = '47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
import binascii
gif = binascii.unhexlify(hex_string)
'''
7.13. does gif matches GIF89a
'''
gif[:6] == b'GIF89a'
'''
7.14
The pixel width of a GIF is a 16-bit little endian integer beginning at byte offset 6
height is the same starting at offset 8
'''
print(gif[6:8])
print(gif[8:10])
import struct
struct.unpack('<HH', gif[6:10])