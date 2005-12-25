""" Python Character Mapping Codec generated from 'MAPPINGS/VENDORS/APPLE/CYRILLIC.TXT' with gencodec.py.

"""#"

import codecs

### Codec APIs

class Codec(codecs.Codec):

    def encode(self,input,errors='strict'):

        return codecs.charmap_encode(input,errors,encoding_map)

    def decode(self,input,errors='strict'):

        return codecs.charmap_decode(input,errors,decoding_table)

class StreamWriter(Codec,codecs.StreamWriter):
    pass

class StreamReader(Codec,codecs.StreamReader):
    pass

### encodings module API

def getregentry():

    return (Codec().encode,Codec().decode,StreamReader,StreamWriter)


### Decoding Table

decoding_table = (
    u'\x00'     #  0x00 -> CONTROL CHARACTER
    u'\x01'     #  0x01 -> CONTROL CHARACTER
    u'\x02'     #  0x02 -> CONTROL CHARACTER
    u'\x03'     #  0x03 -> CONTROL CHARACTER
    u'\x04'     #  0x04 -> CONTROL CHARACTER
    u'\x05'     #  0x05 -> CONTROL CHARACTER
    u'\x06'     #  0x06 -> CONTROL CHARACTER
    u'\x07'     #  0x07 -> CONTROL CHARACTER
    u'\x08'     #  0x08 -> CONTROL CHARACTER
    u'\t'       #  0x09 -> CONTROL CHARACTER
    u'\n'       #  0x0A -> CONTROL CHARACTER
    u'\x0b'     #  0x0B -> CONTROL CHARACTER
    u'\x0c'     #  0x0C -> CONTROL CHARACTER
    u'\r'       #  0x0D -> CONTROL CHARACTER
    u'\x0e'     #  0x0E -> CONTROL CHARACTER
    u'\x0f'     #  0x0F -> CONTROL CHARACTER
    u'\x10'     #  0x10 -> CONTROL CHARACTER
    u'\x11'     #  0x11 -> CONTROL CHARACTER
    u'\x12'     #  0x12 -> CONTROL CHARACTER
    u'\x13'     #  0x13 -> CONTROL CHARACTER
    u'\x14'     #  0x14 -> CONTROL CHARACTER
    u'\x15'     #  0x15 -> CONTROL CHARACTER
    u'\x16'     #  0x16 -> CONTROL CHARACTER
    u'\x17'     #  0x17 -> CONTROL CHARACTER
    u'\x18'     #  0x18 -> CONTROL CHARACTER
    u'\x19'     #  0x19 -> CONTROL CHARACTER
    u'\x1a'     #  0x1A -> CONTROL CHARACTER
    u'\x1b'     #  0x1B -> CONTROL CHARACTER
    u'\x1c'     #  0x1C -> CONTROL CHARACTER
    u'\x1d'     #  0x1D -> CONTROL CHARACTER
    u'\x1e'     #  0x1E -> CONTROL CHARACTER
    u'\x1f'     #  0x1F -> CONTROL CHARACTER
    u' '        #  0x20 -> SPACE
    u'!'        #  0x21 -> EXCLAMATION MARK
    u'"'        #  0x22 -> QUOTATION MARK
    u'#'        #  0x23 -> NUMBER SIGN
    u'$'        #  0x24 -> DOLLAR SIGN
    u'%'        #  0x25 -> PERCENT SIGN
    u'&'        #  0x26 -> AMPERSAND
    u"'"        #  0x27 -> APOSTROPHE
    u'('        #  0x28 -> LEFT PARENTHESIS
    u')'        #  0x29 -> RIGHT PARENTHESIS
    u'*'        #  0x2A -> ASTERISK
    u'+'        #  0x2B -> PLUS SIGN
    u','        #  0x2C -> COMMA
    u'-'        #  0x2D -> HYPHEN-MINUS
    u'.'        #  0x2E -> FULL STOP
    u'/'        #  0x2F -> SOLIDUS
    u'0'        #  0x30 -> DIGIT ZERO
    u'1'        #  0x31 -> DIGIT ONE
    u'2'        #  0x32 -> DIGIT TWO
    u'3'        #  0x33 -> DIGIT THREE
    u'4'        #  0x34 -> DIGIT FOUR
    u'5'        #  0x35 -> DIGIT FIVE
    u'6'        #  0x36 -> DIGIT SIX
    u'7'        #  0x37 -> DIGIT SEVEN
    u'8'        #  0x38 -> DIGIT EIGHT
    u'9'        #  0x39 -> DIGIT NINE
    u':'        #  0x3A -> COLON
    u';'        #  0x3B -> SEMICOLON
    u'<'        #  0x3C -> LESS-THAN SIGN
    u'='        #  0x3D -> EQUALS SIGN
    u'>'        #  0x3E -> GREATER-THAN SIGN
    u'?'        #  0x3F -> QUESTION MARK
    u'@'        #  0x40 -> COMMERCIAL AT
    u'A'        #  0x41 -> LATIN CAPITAL LETTER A
    u'B'        #  0x42 -> LATIN CAPITAL LETTER B
    u'C'        #  0x43 -> LATIN CAPITAL LETTER C
    u'D'        #  0x44 -> LATIN CAPITAL LETTER D
    u'E'        #  0x45 -> LATIN CAPITAL LETTER E
    u'F'        #  0x46 -> LATIN CAPITAL LETTER F
    u'G'        #  0x47 -> LATIN CAPITAL LETTER G
    u'H'        #  0x48 -> LATIN CAPITAL LETTER H
    u'I'        #  0x49 -> LATIN CAPITAL LETTER I
    u'J'        #  0x4A -> LATIN CAPITAL LETTER J
    u'K'        #  0x4B -> LATIN CAPITAL LETTER K
    u'L'        #  0x4C -> LATIN CAPITAL LETTER L
    u'M'        #  0x4D -> LATIN CAPITAL LETTER M
    u'N'        #  0x4E -> LATIN CAPITAL LETTER N
    u'O'        #  0x4F -> LATIN CAPITAL LETTER O
    u'P'        #  0x50 -> LATIN CAPITAL LETTER P
    u'Q'        #  0x51 -> LATIN CAPITAL LETTER Q
    u'R'        #  0x52 -> LATIN CAPITAL LETTER R
    u'S'        #  0x53 -> LATIN CAPITAL LETTER S
    u'T'        #  0x54 -> LATIN CAPITAL LETTER T
    u'U'        #  0x55 -> LATIN CAPITAL LETTER U
    u'V'        #  0x56 -> LATIN CAPITAL LETTER V
    u'W'        #  0x57 -> LATIN CAPITAL LETTER W
    u'X'        #  0x58 -> LATIN CAPITAL LETTER X
    u'Y'        #  0x59 -> LATIN CAPITAL LETTER Y
    u'Z'        #  0x5A -> LATIN CAPITAL LETTER Z
    u'['        #  0x5B -> LEFT SQUARE BRACKET
    u'\\'       #  0x5C -> REVERSE SOLIDUS
    u']'        #  0x5D -> RIGHT SQUARE BRACKET
    u'^'        #  0x5E -> CIRCUMFLEX ACCENT
    u'_'        #  0x5F -> LOW LINE
    u'`'        #  0x60 -> GRAVE ACCENT
    u'a'        #  0x61 -> LATIN SMALL LETTER A
    u'b'        #  0x62 -> LATIN SMALL LETTER B
    u'c'        #  0x63 -> LATIN SMALL LETTER C
    u'd'        #  0x64 -> LATIN SMALL LETTER D
    u'e'        #  0x65 -> LATIN SMALL LETTER E
    u'f'        #  0x66 -> LATIN SMALL LETTER F
    u'g'        #  0x67 -> LATIN SMALL LETTER G
    u'h'        #  0x68 -> LATIN SMALL LETTER H
    u'i'        #  0x69 -> LATIN SMALL LETTER I
    u'j'        #  0x6A -> LATIN SMALL LETTER J
    u'k'        #  0x6B -> LATIN SMALL LETTER K
    u'l'        #  0x6C -> LATIN SMALL LETTER L
    u'm'        #  0x6D -> LATIN SMALL LETTER M
    u'n'        #  0x6E -> LATIN SMALL LETTER N
    u'o'        #  0x6F -> LATIN SMALL LETTER O
    u'p'        #  0x70 -> LATIN SMALL LETTER P
    u'q'        #  0x71 -> LATIN SMALL LETTER Q
    u'r'        #  0x72 -> LATIN SMALL LETTER R
    u's'        #  0x73 -> LATIN SMALL LETTER S
    u't'        #  0x74 -> LATIN SMALL LETTER T
    u'u'        #  0x75 -> LATIN SMALL LETTER U
    u'v'        #  0x76 -> LATIN SMALL LETTER V
    u'w'        #  0x77 -> LATIN SMALL LETTER W
    u'x'        #  0x78 -> LATIN SMALL LETTER X
    u'y'        #  0x79 -> LATIN SMALL LETTER Y
    u'z'        #  0x7A -> LATIN SMALL LETTER Z
    u'{'        #  0x7B -> LEFT CURLY BRACKET
    u'|'        #  0x7C -> VERTICAL LINE
    u'}'        #  0x7D -> RIGHT CURLY BRACKET
    u'~'        #  0x7E -> TILDE
    u'\x7f'     #  0x7F -> CONTROL CHARACTER
    u'\u0410'   #  0x80 -> CYRILLIC CAPITAL LETTER A
    u'\u0411'   #  0x81 -> CYRILLIC CAPITAL LETTER BE
    u'\u0412'   #  0x82 -> CYRILLIC CAPITAL LETTER VE
    u'\u0413'   #  0x83 -> CYRILLIC CAPITAL LETTER GHE
    u'\u0414'   #  0x84 -> CYRILLIC CAPITAL LETTER DE
    u'\u0415'   #  0x85 -> CYRILLIC CAPITAL LETTER IE
    u'\u0416'   #  0x86 -> CYRILLIC CAPITAL LETTER ZHE
    u'\u0417'   #  0x87 -> CYRILLIC CAPITAL LETTER ZE
    u'\u0418'   #  0x88 -> CYRILLIC CAPITAL LETTER I
    u'\u0419'   #  0x89 -> CYRILLIC CAPITAL LETTER SHORT I
    u'\u041a'   #  0x8A -> CYRILLIC CAPITAL LETTER KA
    u'\u041b'   #  0x8B -> CYRILLIC CAPITAL LETTER EL
    u'\u041c'   #  0x8C -> CYRILLIC CAPITAL LETTER EM
    u'\u041d'   #  0x8D -> CYRILLIC CAPITAL LETTER EN
    u'\u041e'   #  0x8E -> CYRILLIC CAPITAL LETTER O
    u'\u041f'   #  0x8F -> CYRILLIC CAPITAL LETTER PE
    u'\u0420'   #  0x90 -> CYRILLIC CAPITAL LETTER ER
    u'\u0421'   #  0x91 -> CYRILLIC CAPITAL LETTER ES
    u'\u0422'   #  0x92 -> CYRILLIC CAPITAL LETTER TE
    u'\u0423'   #  0x93 -> CYRILLIC CAPITAL LETTER U
    u'\u0424'   #  0x94 -> CYRILLIC CAPITAL LETTER EF
    u'\u0425'   #  0x95 -> CYRILLIC CAPITAL LETTER HA
    u'\u0426'   #  0x96 -> CYRILLIC CAPITAL LETTER TSE
    u'\u0427'   #  0x97 -> CYRILLIC CAPITAL LETTER CHE
    u'\u0428'   #  0x98 -> CYRILLIC CAPITAL LETTER SHA
    u'\u0429'   #  0x99 -> CYRILLIC CAPITAL LETTER SHCHA
    u'\u042a'   #  0x9A -> CYRILLIC CAPITAL LETTER HARD SIGN
    u'\u042b'   #  0x9B -> CYRILLIC CAPITAL LETTER YERU
    u'\u042c'   #  0x9C -> CYRILLIC CAPITAL LETTER SOFT SIGN
    u'\u042d'   #  0x9D -> CYRILLIC CAPITAL LETTER E
    u'\u042e'   #  0x9E -> CYRILLIC CAPITAL LETTER YU
    u'\u042f'   #  0x9F -> CYRILLIC CAPITAL LETTER YA
    u'\u2020'   #  0xA0 -> DAGGER
    u'\xb0'     #  0xA1 -> DEGREE SIGN
    u'\u0490'   #  0xA2 -> CYRILLIC CAPITAL LETTER GHE WITH UPTURN
    u'\xa3'     #  0xA3 -> POUND SIGN
    u'\xa7'     #  0xA4 -> SECTION SIGN
    u'\u2022'   #  0xA5 -> BULLET
    u'\xb6'     #  0xA6 -> PILCROW SIGN
    u'\u0406'   #  0xA7 -> CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    u'\xae'     #  0xA8 -> REGISTERED SIGN
    u'\xa9'     #  0xA9 -> COPYRIGHT SIGN
    u'\u2122'   #  0xAA -> TRADE MARK SIGN
    u'\u0402'   #  0xAB -> CYRILLIC CAPITAL LETTER DJE
    u'\u0452'   #  0xAC -> CYRILLIC SMALL LETTER DJE
    u'\u2260'   #  0xAD -> NOT EQUAL TO
    u'\u0403'   #  0xAE -> CYRILLIC CAPITAL LETTER GJE
    u'\u0453'   #  0xAF -> CYRILLIC SMALL LETTER GJE
    u'\u221e'   #  0xB0 -> INFINITY
    u'\xb1'     #  0xB1 -> PLUS-MINUS SIGN
    u'\u2264'   #  0xB2 -> LESS-THAN OR EQUAL TO
    u'\u2265'   #  0xB3 -> GREATER-THAN OR EQUAL TO
    u'\u0456'   #  0xB4 -> CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    u'\xb5'     #  0xB5 -> MICRO SIGN
    u'\u0491'   #  0xB6 -> CYRILLIC SMALL LETTER GHE WITH UPTURN
    u'\u0408'   #  0xB7 -> CYRILLIC CAPITAL LETTER JE
    u'\u0404'   #  0xB8 -> CYRILLIC CAPITAL LETTER UKRAINIAN IE
    u'\u0454'   #  0xB9 -> CYRILLIC SMALL LETTER UKRAINIAN IE
    u'\u0407'   #  0xBA -> CYRILLIC CAPITAL LETTER YI
    u'\u0457'   #  0xBB -> CYRILLIC SMALL LETTER YI
    u'\u0409'   #  0xBC -> CYRILLIC CAPITAL LETTER LJE
    u'\u0459'   #  0xBD -> CYRILLIC SMALL LETTER LJE
    u'\u040a'   #  0xBE -> CYRILLIC CAPITAL LETTER NJE
    u'\u045a'   #  0xBF -> CYRILLIC SMALL LETTER NJE
    u'\u0458'   #  0xC0 -> CYRILLIC SMALL LETTER JE
    u'\u0405'   #  0xC1 -> CYRILLIC CAPITAL LETTER DZE
    u'\xac'     #  0xC2 -> NOT SIGN
    u'\u221a'   #  0xC3 -> SQUARE ROOT
    u'\u0192'   #  0xC4 -> LATIN SMALL LETTER F WITH HOOK
    u'\u2248'   #  0xC5 -> ALMOST EQUAL TO
    u'\u2206'   #  0xC6 -> INCREMENT
    u'\xab'     #  0xC7 -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\xbb'     #  0xC8 -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    u'\u2026'   #  0xC9 -> HORIZONTAL ELLIPSIS
    u'\xa0'     #  0xCA -> NO-BREAK SPACE
    u'\u040b'   #  0xCB -> CYRILLIC CAPITAL LETTER TSHE
    u'\u045b'   #  0xCC -> CYRILLIC SMALL LETTER TSHE
    u'\u040c'   #  0xCD -> CYRILLIC CAPITAL LETTER KJE
    u'\u045c'   #  0xCE -> CYRILLIC SMALL LETTER KJE
    u'\u0455'   #  0xCF -> CYRILLIC SMALL LETTER DZE
    u'\u2013'   #  0xD0 -> EN DASH
    u'\u2014'   #  0xD1 -> EM DASH
    u'\u201c'   #  0xD2 -> LEFT DOUBLE QUOTATION MARK
    u'\u201d'   #  0xD3 -> RIGHT DOUBLE QUOTATION MARK
    u'\u2018'   #  0xD4 -> LEFT SINGLE QUOTATION MARK
    u'\u2019'   #  0xD5 -> RIGHT SINGLE QUOTATION MARK
    u'\xf7'     #  0xD6 -> DIVISION SIGN
    u'\u201e'   #  0xD7 -> DOUBLE LOW-9 QUOTATION MARK
    u'\u040e'   #  0xD8 -> CYRILLIC CAPITAL LETTER SHORT U
    u'\u045e'   #  0xD9 -> CYRILLIC SMALL LETTER SHORT U
    u'\u040f'   #  0xDA -> CYRILLIC CAPITAL LETTER DZHE
    u'\u045f'   #  0xDB -> CYRILLIC SMALL LETTER DZHE
    u'\u2116'   #  0xDC -> NUMERO SIGN
    u'\u0401'   #  0xDD -> CYRILLIC CAPITAL LETTER IO
    u'\u0451'   #  0xDE -> CYRILLIC SMALL LETTER IO
    u'\u044f'   #  0xDF -> CYRILLIC SMALL LETTER YA
    u'\u0430'   #  0xE0 -> CYRILLIC SMALL LETTER A
    u'\u0431'   #  0xE1 -> CYRILLIC SMALL LETTER BE
    u'\u0432'   #  0xE2 -> CYRILLIC SMALL LETTER VE
    u'\u0433'   #  0xE3 -> CYRILLIC SMALL LETTER GHE
    u'\u0434'   #  0xE4 -> CYRILLIC SMALL LETTER DE
    u'\u0435'   #  0xE5 -> CYRILLIC SMALL LETTER IE
    u'\u0436'   #  0xE6 -> CYRILLIC SMALL LETTER ZHE
    u'\u0437'   #  0xE7 -> CYRILLIC SMALL LETTER ZE
    u'\u0438'   #  0xE8 -> CYRILLIC SMALL LETTER I
    u'\u0439'   #  0xE9 -> CYRILLIC SMALL LETTER SHORT I
    u'\u043a'   #  0xEA -> CYRILLIC SMALL LETTER KA
    u'\u043b'   #  0xEB -> CYRILLIC SMALL LETTER EL
    u'\u043c'   #  0xEC -> CYRILLIC SMALL LETTER EM
    u'\u043d'   #  0xED -> CYRILLIC SMALL LETTER EN
    u'\u043e'   #  0xEE -> CYRILLIC SMALL LETTER O
    u'\u043f'   #  0xEF -> CYRILLIC SMALL LETTER PE
    u'\u0440'   #  0xF0 -> CYRILLIC SMALL LETTER ER
    u'\u0441'   #  0xF1 -> CYRILLIC SMALL LETTER ES
    u'\u0442'   #  0xF2 -> CYRILLIC SMALL LETTER TE
    u'\u0443'   #  0xF3 -> CYRILLIC SMALL LETTER U
    u'\u0444'   #  0xF4 -> CYRILLIC SMALL LETTER EF
    u'\u0445'   #  0xF5 -> CYRILLIC SMALL LETTER HA
    u'\u0446'   #  0xF6 -> CYRILLIC SMALL LETTER TSE
    u'\u0447'   #  0xF7 -> CYRILLIC SMALL LETTER CHE
    u'\u0448'   #  0xF8 -> CYRILLIC SMALL LETTER SHA
    u'\u0449'   #  0xF9 -> CYRILLIC SMALL LETTER SHCHA
    u'\u044a'   #  0xFA -> CYRILLIC SMALL LETTER HARD SIGN
    u'\u044b'   #  0xFB -> CYRILLIC SMALL LETTER YERU
    u'\u044c'   #  0xFC -> CYRILLIC SMALL LETTER SOFT SIGN
    u'\u044d'   #  0xFD -> CYRILLIC SMALL LETTER E
    u'\u044e'   #  0xFE -> CYRILLIC SMALL LETTER YU
    u'\u20ac'   #  0xFF -> EURO SIGN
)

### Encoding Map

encoding_map = {
    0x0000: 0x00,       #  CONTROL CHARACTER
    0x0001: 0x01,       #  CONTROL CHARACTER
    0x0002: 0x02,       #  CONTROL CHARACTER
    0x0003: 0x03,       #  CONTROL CHARACTER
    0x0004: 0x04,       #  CONTROL CHARACTER
    0x0005: 0x05,       #  CONTROL CHARACTER
    0x0006: 0x06,       #  CONTROL CHARACTER
    0x0007: 0x07,       #  CONTROL CHARACTER
    0x0008: 0x08,       #  CONTROL CHARACTER
    0x0009: 0x09,       #  CONTROL CHARACTER
    0x000A: 0x0A,       #  CONTROL CHARACTER
    0x000B: 0x0B,       #  CONTROL CHARACTER
    0x000C: 0x0C,       #  CONTROL CHARACTER
    0x000D: 0x0D,       #  CONTROL CHARACTER
    0x000E: 0x0E,       #  CONTROL CHARACTER
    0x000F: 0x0F,       #  CONTROL CHARACTER
    0x0010: 0x10,       #  CONTROL CHARACTER
    0x0011: 0x11,       #  CONTROL CHARACTER
    0x0012: 0x12,       #  CONTROL CHARACTER
    0x0013: 0x13,       #  CONTROL CHARACTER
    0x0014: 0x14,       #  CONTROL CHARACTER
    0x0015: 0x15,       #  CONTROL CHARACTER
    0x0016: 0x16,       #  CONTROL CHARACTER
    0x0017: 0x17,       #  CONTROL CHARACTER
    0x0018: 0x18,       #  CONTROL CHARACTER
    0x0019: 0x19,       #  CONTROL CHARACTER
    0x001A: 0x1A,       #  CONTROL CHARACTER
    0x001B: 0x1B,       #  CONTROL CHARACTER
    0x001C: 0x1C,       #  CONTROL CHARACTER
    0x001D: 0x1D,       #  CONTROL CHARACTER
    0x001E: 0x1E,       #  CONTROL CHARACTER
    0x001F: 0x1F,       #  CONTROL CHARACTER
    0x0020: 0x20,       #  SPACE
    0x0021: 0x21,       #  EXCLAMATION MARK
    0x0022: 0x22,       #  QUOTATION MARK
    0x0023: 0x23,       #  NUMBER SIGN
    0x0024: 0x24,       #  DOLLAR SIGN
    0x0025: 0x25,       #  PERCENT SIGN
    0x0026: 0x26,       #  AMPERSAND
    0x0027: 0x27,       #  APOSTROPHE
    0x0028: 0x28,       #  LEFT PARENTHESIS
    0x0029: 0x29,       #  RIGHT PARENTHESIS
    0x002A: 0x2A,       #  ASTERISK
    0x002B: 0x2B,       #  PLUS SIGN
    0x002C: 0x2C,       #  COMMA
    0x002D: 0x2D,       #  HYPHEN-MINUS
    0x002E: 0x2E,       #  FULL STOP
    0x002F: 0x2F,       #  SOLIDUS
    0x0030: 0x30,       #  DIGIT ZERO
    0x0031: 0x31,       #  DIGIT ONE
    0x0032: 0x32,       #  DIGIT TWO
    0x0033: 0x33,       #  DIGIT THREE
    0x0034: 0x34,       #  DIGIT FOUR
    0x0035: 0x35,       #  DIGIT FIVE
    0x0036: 0x36,       #  DIGIT SIX
    0x0037: 0x37,       #  DIGIT SEVEN
    0x0038: 0x38,       #  DIGIT EIGHT
    0x0039: 0x39,       #  DIGIT NINE
    0x003A: 0x3A,       #  COLON
    0x003B: 0x3B,       #  SEMICOLON
    0x003C: 0x3C,       #  LESS-THAN SIGN
    0x003D: 0x3D,       #  EQUALS SIGN
    0x003E: 0x3E,       #  GREATER-THAN SIGN
    0x003F: 0x3F,       #  QUESTION MARK
    0x0040: 0x40,       #  COMMERCIAL AT
    0x0041: 0x41,       #  LATIN CAPITAL LETTER A
    0x0042: 0x42,       #  LATIN CAPITAL LETTER B
    0x0043: 0x43,       #  LATIN CAPITAL LETTER C
    0x0044: 0x44,       #  LATIN CAPITAL LETTER D
    0x0045: 0x45,       #  LATIN CAPITAL LETTER E
    0x0046: 0x46,       #  LATIN CAPITAL LETTER F
    0x0047: 0x47,       #  LATIN CAPITAL LETTER G
    0x0048: 0x48,       #  LATIN CAPITAL LETTER H
    0x0049: 0x49,       #  LATIN CAPITAL LETTER I
    0x004A: 0x4A,       #  LATIN CAPITAL LETTER J
    0x004B: 0x4B,       #  LATIN CAPITAL LETTER K
    0x004C: 0x4C,       #  LATIN CAPITAL LETTER L
    0x004D: 0x4D,       #  LATIN CAPITAL LETTER M
    0x004E: 0x4E,       #  LATIN CAPITAL LETTER N
    0x004F: 0x4F,       #  LATIN CAPITAL LETTER O
    0x0050: 0x50,       #  LATIN CAPITAL LETTER P
    0x0051: 0x51,       #  LATIN CAPITAL LETTER Q
    0x0052: 0x52,       #  LATIN CAPITAL LETTER R
    0x0053: 0x53,       #  LATIN CAPITAL LETTER S
    0x0054: 0x54,       #  LATIN CAPITAL LETTER T
    0x0055: 0x55,       #  LATIN CAPITAL LETTER U
    0x0056: 0x56,       #  LATIN CAPITAL LETTER V
    0x0057: 0x57,       #  LATIN CAPITAL LETTER W
    0x0058: 0x58,       #  LATIN CAPITAL LETTER X
    0x0059: 0x59,       #  LATIN CAPITAL LETTER Y
    0x005A: 0x5A,       #  LATIN CAPITAL LETTER Z
    0x005B: 0x5B,       #  LEFT SQUARE BRACKET
    0x005C: 0x5C,       #  REVERSE SOLIDUS
    0x005D: 0x5D,       #  RIGHT SQUARE BRACKET
    0x005E: 0x5E,       #  CIRCUMFLEX ACCENT
    0x005F: 0x5F,       #  LOW LINE
    0x0060: 0x60,       #  GRAVE ACCENT
    0x0061: 0x61,       #  LATIN SMALL LETTER A
    0x0062: 0x62,       #  LATIN SMALL LETTER B
    0x0063: 0x63,       #  LATIN SMALL LETTER C
    0x0064: 0x64,       #  LATIN SMALL LETTER D
    0x0065: 0x65,       #  LATIN SMALL LETTER E
    0x0066: 0x66,       #  LATIN SMALL LETTER F
    0x0067: 0x67,       #  LATIN SMALL LETTER G
    0x0068: 0x68,       #  LATIN SMALL LETTER H
    0x0069: 0x69,       #  LATIN SMALL LETTER I
    0x006A: 0x6A,       #  LATIN SMALL LETTER J
    0x006B: 0x6B,       #  LATIN SMALL LETTER K
    0x006C: 0x6C,       #  LATIN SMALL LETTER L
    0x006D: 0x6D,       #  LATIN SMALL LETTER M
    0x006E: 0x6E,       #  LATIN SMALL LETTER N
    0x006F: 0x6F,       #  LATIN SMALL LETTER O
    0x0070: 0x70,       #  LATIN SMALL LETTER P
    0x0071: 0x71,       #  LATIN SMALL LETTER Q
    0x0072: 0x72,       #  LATIN SMALL LETTER R
    0x0073: 0x73,       #  LATIN SMALL LETTER S
    0x0074: 0x74,       #  LATIN SMALL LETTER T
    0x0075: 0x75,       #  LATIN SMALL LETTER U
    0x0076: 0x76,       #  LATIN SMALL LETTER V
    0x0077: 0x77,       #  LATIN SMALL LETTER W
    0x0078: 0x78,       #  LATIN SMALL LETTER X
    0x0079: 0x79,       #  LATIN SMALL LETTER Y
    0x007A: 0x7A,       #  LATIN SMALL LETTER Z
    0x007B: 0x7B,       #  LEFT CURLY BRACKET
    0x007C: 0x7C,       #  VERTICAL LINE
    0x007D: 0x7D,       #  RIGHT CURLY BRACKET
    0x007E: 0x7E,       #  TILDE
    0x007F: 0x7F,       #  CONTROL CHARACTER
    0x00A0: 0xCA,       #  NO-BREAK SPACE
    0x00A3: 0xA3,       #  POUND SIGN
    0x00A7: 0xA4,       #  SECTION SIGN
    0x00A9: 0xA9,       #  COPYRIGHT SIGN
    0x00AB: 0xC7,       #  LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00AC: 0xC2,       #  NOT SIGN
    0x00AE: 0xA8,       #  REGISTERED SIGN
    0x00B0: 0xA1,       #  DEGREE SIGN
    0x00B1: 0xB1,       #  PLUS-MINUS SIGN
    0x00B5: 0xB5,       #  MICRO SIGN
    0x00B6: 0xA6,       #  PILCROW SIGN
    0x00BB: 0xC8,       #  RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00F7: 0xD6,       #  DIVISION SIGN
    0x0192: 0xC4,       #  LATIN SMALL LETTER F WITH HOOK
    0x0401: 0xDD,       #  CYRILLIC CAPITAL LETTER IO
    0x0402: 0xAB,       #  CYRILLIC CAPITAL LETTER DJE
    0x0403: 0xAE,       #  CYRILLIC CAPITAL LETTER GJE
    0x0404: 0xB8,       #  CYRILLIC CAPITAL LETTER UKRAINIAN IE
    0x0405: 0xC1,       #  CYRILLIC CAPITAL LETTER DZE
    0x0406: 0xA7,       #  CYRILLIC CAPITAL LETTER BYELORUSSIAN-UKRAINIAN I
    0x0407: 0xBA,       #  CYRILLIC CAPITAL LETTER YI
    0x0408: 0xB7,       #  CYRILLIC CAPITAL LETTER JE
    0x0409: 0xBC,       #  CYRILLIC CAPITAL LETTER LJE
    0x040A: 0xBE,       #  CYRILLIC CAPITAL LETTER NJE
    0x040B: 0xCB,       #  CYRILLIC CAPITAL LETTER TSHE
    0x040C: 0xCD,       #  CYRILLIC CAPITAL LETTER KJE
    0x040E: 0xD8,       #  CYRILLIC CAPITAL LETTER SHORT U
    0x040F: 0xDA,       #  CYRILLIC CAPITAL LETTER DZHE
    0x0410: 0x80,       #  CYRILLIC CAPITAL LETTER A
    0x0411: 0x81,       #  CYRILLIC CAPITAL LETTER BE
    0x0412: 0x82,       #  CYRILLIC CAPITAL LETTER VE
    0x0413: 0x83,       #  CYRILLIC CAPITAL LETTER GHE
    0x0414: 0x84,       #  CYRILLIC CAPITAL LETTER DE
    0x0415: 0x85,       #  CYRILLIC CAPITAL LETTER IE
    0x0416: 0x86,       #  CYRILLIC CAPITAL LETTER ZHE
    0x0417: 0x87,       #  CYRILLIC CAPITAL LETTER ZE
    0x0418: 0x88,       #  CYRILLIC CAPITAL LETTER I
    0x0419: 0x89,       #  CYRILLIC CAPITAL LETTER SHORT I
    0x041A: 0x8A,       #  CYRILLIC CAPITAL LETTER KA
    0x041B: 0x8B,       #  CYRILLIC CAPITAL LETTER EL
    0x041C: 0x8C,       #  CYRILLIC CAPITAL LETTER EM
    0x041D: 0x8D,       #  CYRILLIC CAPITAL LETTER EN
    0x041E: 0x8E,       #  CYRILLIC CAPITAL LETTER O
    0x041F: 0x8F,       #  CYRILLIC CAPITAL LETTER PE
    0x0420: 0x90,       #  CYRILLIC CAPITAL LETTER ER
    0x0421: 0x91,       #  CYRILLIC CAPITAL LETTER ES
    0x0422: 0x92,       #  CYRILLIC CAPITAL LETTER TE
    0x0423: 0x93,       #  CYRILLIC CAPITAL LETTER U
    0x0424: 0x94,       #  CYRILLIC CAPITAL LETTER EF
    0x0425: 0x95,       #  CYRILLIC CAPITAL LETTER HA
    0x0426: 0x96,       #  CYRILLIC CAPITAL LETTER TSE
    0x0427: 0x97,       #  CYRILLIC CAPITAL LETTER CHE
    0x0428: 0x98,       #  CYRILLIC CAPITAL LETTER SHA
    0x0429: 0x99,       #  CYRILLIC CAPITAL LETTER SHCHA
    0x042A: 0x9A,       #  CYRILLIC CAPITAL LETTER HARD SIGN
    0x042B: 0x9B,       #  CYRILLIC CAPITAL LETTER YERU
    0x042C: 0x9C,       #  CYRILLIC CAPITAL LETTER SOFT SIGN
    0x042D: 0x9D,       #  CYRILLIC CAPITAL LETTER E
    0x042E: 0x9E,       #  CYRILLIC CAPITAL LETTER YU
    0x042F: 0x9F,       #  CYRILLIC CAPITAL LETTER YA
    0x0430: 0xE0,       #  CYRILLIC SMALL LETTER A
    0x0431: 0xE1,       #  CYRILLIC SMALL LETTER BE
    0x0432: 0xE2,       #  CYRILLIC SMALL LETTER VE
    0x0433: 0xE3,       #  CYRILLIC SMALL LETTER GHE
    0x0434: 0xE4,       #  CYRILLIC SMALL LETTER DE
    0x0435: 0xE5,       #  CYRILLIC SMALL LETTER IE
    0x0436: 0xE6,       #  CYRILLIC SMALL LETTER ZHE
    0x0437: 0xE7,       #  CYRILLIC SMALL LETTER ZE
    0x0438: 0xE8,       #  CYRILLIC SMALL LETTER I
    0x0439: 0xE9,       #  CYRILLIC SMALL LETTER SHORT I
    0x043A: 0xEA,       #  CYRILLIC SMALL LETTER KA
    0x043B: 0xEB,       #  CYRILLIC SMALL LETTER EL
    0x043C: 0xEC,       #  CYRILLIC SMALL LETTER EM
    0x043D: 0xED,       #  CYRILLIC SMALL LETTER EN
    0x043E: 0xEE,       #  CYRILLIC SMALL LETTER O
    0x043F: 0xEF,       #  CYRILLIC SMALL LETTER PE
    0x0440: 0xF0,       #  CYRILLIC SMALL LETTER ER
    0x0441: 0xF1,       #  CYRILLIC SMALL LETTER ES
    0x0442: 0xF2,       #  CYRILLIC SMALL LETTER TE
    0x0443: 0xF3,       #  CYRILLIC SMALL LETTER U
    0x0444: 0xF4,       #  CYRILLIC SMALL LETTER EF
    0x0445: 0xF5,       #  CYRILLIC SMALL LETTER HA
    0x0446: 0xF6,       #  CYRILLIC SMALL LETTER TSE
    0x0447: 0xF7,       #  CYRILLIC SMALL LETTER CHE
    0x0448: 0xF8,       #  CYRILLIC SMALL LETTER SHA
    0x0449: 0xF9,       #  CYRILLIC SMALL LETTER SHCHA
    0x044A: 0xFA,       #  CYRILLIC SMALL LETTER HARD SIGN
    0x044B: 0xFB,       #  CYRILLIC SMALL LETTER YERU
    0x044C: 0xFC,       #  CYRILLIC SMALL LETTER SOFT SIGN
    0x044D: 0xFD,       #  CYRILLIC SMALL LETTER E
    0x044E: 0xFE,       #  CYRILLIC SMALL LETTER YU
    0x044F: 0xDF,       #  CYRILLIC SMALL LETTER YA
    0x0451: 0xDE,       #  CYRILLIC SMALL LETTER IO
    0x0452: 0xAC,       #  CYRILLIC SMALL LETTER DJE
    0x0453: 0xAF,       #  CYRILLIC SMALL LETTER GJE
    0x0454: 0xB9,       #  CYRILLIC SMALL LETTER UKRAINIAN IE
    0x0455: 0xCF,       #  CYRILLIC SMALL LETTER DZE
    0x0456: 0xB4,       #  CYRILLIC SMALL LETTER BYELORUSSIAN-UKRAINIAN I
    0x0457: 0xBB,       #  CYRILLIC SMALL LETTER YI
    0x0458: 0xC0,       #  CYRILLIC SMALL LETTER JE
    0x0459: 0xBD,       #  CYRILLIC SMALL LETTER LJE
    0x045A: 0xBF,       #  CYRILLIC SMALL LETTER NJE
    0x045B: 0xCC,       #  CYRILLIC SMALL LETTER TSHE
    0x045C: 0xCE,       #  CYRILLIC SMALL LETTER KJE
    0x045E: 0xD9,       #  CYRILLIC SMALL LETTER SHORT U
    0x045F: 0xDB,       #  CYRILLIC SMALL LETTER DZHE
    0x0490: 0xA2,       #  CYRILLIC CAPITAL LETTER GHE WITH UPTURN
    0x0491: 0xB6,       #  CYRILLIC SMALL LETTER GHE WITH UPTURN
    0x2013: 0xD0,       #  EN DASH
    0x2014: 0xD1,       #  EM DASH
    0x2018: 0xD4,       #  LEFT SINGLE QUOTATION MARK
    0x2019: 0xD5,       #  RIGHT SINGLE QUOTATION MARK
    0x201C: 0xD2,       #  LEFT DOUBLE QUOTATION MARK
    0x201D: 0xD3,       #  RIGHT DOUBLE QUOTATION MARK
    0x201E: 0xD7,       #  DOUBLE LOW-9 QUOTATION MARK
    0x2020: 0xA0,       #  DAGGER
    0x2022: 0xA5,       #  BULLET
    0x2026: 0xC9,       #  HORIZONTAL ELLIPSIS
    0x20AC: 0xFF,       #  EURO SIGN
    0x2116: 0xDC,       #  NUMERO SIGN
    0x2122: 0xAA,       #  TRADE MARK SIGN
    0x2206: 0xC6,       #  INCREMENT
    0x221A: 0xC3,       #  SQUARE ROOT
    0x221E: 0xB0,       #  INFINITY
    0x2248: 0xC5,       #  ALMOST EQUAL TO
    0x2260: 0xAD,       #  NOT EQUAL TO
    0x2264: 0xB2,       #  LESS-THAN OR EQUAL TO
    0x2265: 0xB3,       #  GREATER-THAN OR EQUAL TO
}
