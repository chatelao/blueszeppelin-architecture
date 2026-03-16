import zlib
import string

def encode_puml(puml_text):
    # PlantUML encoding alphabet
    puml_alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + "-_"

    # Compress with zlib (deflate)
    # PlantUML uses a specific deflate without headers/trailers usually or just raw
    zlib_obj = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=-15, memLevel=8, strategy=zlib.Z_DEFAULT_STRATEGY)
    compressed = zlib_obj.compress(puml_text.encode('utf-8')) + zlib_obj.flush()

    # Custom 6-bit encoding
    def encode_6bit(b):
        if b < 10: return chr(48 + b)
        if b < 36: return chr(65 + b - 10)
        if b < 62: return chr(97 + b - 36)
        if b == 62: return '-'
        if b == 63: return '_'
        return '?'

    res = ""
    for i in range(0, len(compressed), 3):
        b1 = compressed[i]
        b2 = compressed[i+1] if i+1 < len(compressed) else 0
        b3 = compressed[i+2] if i+2 < len(compressed) else 0

        res += encode_6bit(b1 >> 2)
        res += encode_6bit(((b1 & 0x3) << 4) | (b2 >> 4))
        res += encode_6bit(((b2 & 0xF) << 2) | (b3 >> 6))
        res += encode_6bit(b3 & 0x3F)

    return res

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            print(encode_puml(f.read()))
    else:
        with open("diagrams/topology.puml", "r") as f:
            print(encode_puml(f.read()))
