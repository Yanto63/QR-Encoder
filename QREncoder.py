### For documentation, see : https://www.thonky.com/qr-code-tutorial/

from QRCodeStandards import *

# DATA_TYPES = { 0 : "Numeric", 1 : "Alphanumeric", 2 : "Binary", 3 : "Kanji"}
# MODE_INDICATORS = { 0 : "0001", 1 : "0010", 2 : "0100", 3 : "1000", 4 : "0111"}
# ERROR_CORRECTION_LEVELS = { 'M' : 0, 'L' : 1, 'H' : 2, 'Q' : 3 }
# #[Data Type(N,A,B,K)][Error correction level(M,L,H,Q)][Version(1,...,40)]
# CAPACITIES = (((34,63,101,149,202,255,293,365,432,513,604,691,796,871,991,1082,1212,1346,1500,1600,1708,1872,2059,2188,2395,2544,2701,2857,3035,3289,3486,3693,3909,4134,4343,4588,4775,5039,5313,5596),(41,77,127,187,255,322,370,461,552,652,772,883,1022,1101,1250,1408,1548,1725,1903,2061,2232,2409,2620,2812,3057,3283,3517,3669,3909,4158,4417,4686,4965,5253,5529,5836,6153,6479,6743,7089),(17,34,58,82,106,139,154,202,235,288,331,374,427,468,530,602,674,746,813,919,969,1056,1108,1228,1286,1425,1501,1581,1677,1782,1897,2022,2157,2301,2361,2524,2625,2735,2927,3057),(27,48,77,111,144,178,207,259,312,364,427,489,580,621,703,775,876,948,1063,1159,1224,1358,1468,1588,1718,1804,1933,2085,2181,2358,2473,2670,2805,2949,3081,3244,3417,3599,3791,3993)),((20,38,61,90,122,154,178,221,262,311,366,419,483,528,600,656,734,816,909,970,1035,1134,1248,1326,1451,1542,1637,1732,1839,1994,2113,2238,2369,2506,2632,2780,2894,3054,3220,3391),(25,47,77,114,154,195,224,279,335,395,468,535,619,667,758,854,938,1046,1153,1249,1352,1460,1588,1704,1853,1990,2132,2223,2369,2520,2677,2840,3009,3183,3351,3537,3729,3927,4087,4296),(10,20,35,50,64,84,93,122,143,174,200,227,259,283,321,365,408,452,493,557,587,640,672,744,779,864,910,958,1016,1080,1150,1226,1307,1394,1431,1530,1591,1658,1774,1852),(16,29,47,67,87,108,125,157,189,221,259,296,352,376,426,470,531,574,644,702,742,823,890,963,1041,1094,1172,1263,1322,1429,1499,1618,1700,1787,1867,1966,2071,2181,2298,2420)),((14,26,42,62,84,106,122,152,180,213,251,287,331,362,412,450,504,560,624,666,711,779,857,911,997,1059,1125,1190,1264,1370,1452,1538,1628,1722,1809,1911,1989,2099,2213,2331),(17,32,53,78,106,134,154,192,230,271,321,367,425,458,520,586,644,718,792,858,929,1003,1091,1171,1273,1367,1465,1528,1628,1732,1840,1952,2068,2188,2303,2431,2563,2699,2809,2953),(7,14,24,34,44,58,64,84,98,119,137,155,177,194,220,250,280,310,338,382,403,439,461,511,535,593,625,658,698,742,790,842,898,958,983,1051,1093,1139,1219,1273),(11,20,32,46,60,74,86,108,130,151,177,203,241,258,292,322,364,394,442,482,509,565,611,661,715,751,805,868,908,982,1030,1112,1168,1228,1283,1351,1423,1499,1579,1663)),((8,16,26,38,52,65,75,93,111,131,155,177,204,223,254,277,310,345,384,410,438,480,528,561,614,652,692,732,778,843,894,947,1002,1060,1113,1176,1224,1292,1362,1435),(10,20,32,48,65,82,95,118,141,167,198,226,262,282,320,361,397,442,488,528,572,618,672,721,784,842,902,940,1002,1066,1132,1201,1273,1347,1417,1496,1577,1661,1729,1817),(4,8,15,21,27,36,39,52,60,74,85,96,109,120,136,154,173,191,208,235,248,270,284,315,330,365,385,405,430,457,486,518,553,590,605,647,673,701,750,784),(7,12,20,28,37,45,53,66,80,93,109,125,149,159,180,198,224,243,272,297,314,348,376,407,440,462,496,534,559,604,634,684,719,756,790,832,876,923,972,1024)))
# #[Version(1...9,10...26,27...40)][Data Type(N,A,B,K)]
# CHARACTER_COUNT_INDICATORS_LENGTHS = ((10,9,8,8),(12,11,16,10),(14,13,16,12))
# #{Version:V.I. String}
# VERSION_INFORMATION_STRINGS = {7:"000111110010010100", 8:"001000010110111100", 9:"001001101010011001", 10:"001010010011010011", 11:"001011101111110110", 12:"001100011101100010", 13:"001101100001000111", 14:"001110011000001101", 15:"001111100100101000", 16:"010000101101111000", 17:"010001010001011101", 18:"010010101000010111", 19:"010011010100110010", 20:"010100100110100110", 21:"010101011010000011", 22:"010110100011001001", 23:"010111011111101100", 24:"011000111011000100", 25:"011001000111100001", 26:"011010111110101011", 27:"011011000010001110", 28:"011100110000011010", 29:"011101001100111111", 30:"011110110101110101", 31:"011111001001010000", 32:"100000100111010101", 33:"100001011011110000", 34:"100010100010111010", 35:"100011011110011111", 36:"100100101100001011", 37:"100101010000101110", 38:"100110101001100100", 39:"100111010101000001", 40:"101000110001101001"}
# ALPHANUMERIC_VALUES = { '0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15, 'G' : 16, 'H' : 17, 'I' : 18, 'J' : 19, 'K' : 20, 'L' : 21, 'M' : 22, 'N' : 23, 'O' : 24, 'P' : 25, 'Q' : 26, 'R' : 27, 'S' : 28, 'T' : 29, 'U' : 30, 'V' : 31, 'W' : 32, 'X' : 33, 'Y' : 34, 'Z' : 35, ' ' : 36, '$' : 37, '%' : 38, '*' : 39, '+' : 40, '-' : 41, '.' : 42, '/' : 43, ':' : 44}

# #[Error correction level(M,L,H,Q)][Version(1,...,40)]
# DATA_CODEWORDS_NUMBER = ((16,28,44,64,86,108,124,154,182,216,254,290,334,365,415,453,507,563,627,669,714,782,860,914,1000,1062,1128,1193,1267,1373,1455,1541,1631,1725,1812,1914,1992,2102,2216,2334),(19,34,55,80,108,136,156,194,232,274,324,370,428,461,523,589,647,721,795,861,932,1006,1094,1174,1276,1370,1468,1531,1631,1735,1843,1955,2071,2191,2306,2434,2566,2702,2812,2956),(9,16,26,36,46,60,66,86,100,122,140,158,180,197,223,253,283,313,341,385,406,442,464,514,538,596,628,661,701,745,793,845,901,961,986,1054,1096,1142,1222,1276),(13,22,34,48,62,76,88,110,132,154,180,206,244,261,295,325,367,397,445,485,512,568,614,664,718,754,808,871,911,985,1033,1115,1171,1231,1286,1354,1426,1502,1582,1666))
# ERROR_CORRECTION_CODEWORDS_NUMBER = ((10,16,26,18,24,16,18,22,22,26,30,22,22,24,24,28,28,26,26,26,26,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28),(7,10,15,20,26,18,20,24,30,18,20,24,26,30,22,24,28,30,28,28,28,28,30,30,26,28,30,30,30,30,30,30,30,30,30,30,30,30,30,30),(17,28,22,16,22,28,26,26,24,28,24,28,22,24,24,30,28,28,26,28,30,24,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30),(13,22,18,26,18,24,18,22,20,24,28,26,24,20,30,24,28,28,26,30,28,30,30,30,30,28,30,30,30,30,30,30,30,30,30,30,30,30,30,30))
# #[4*(Version(1...40)-1) + Error correction level(M,L,H,Q)][(Blocks in group 1, Grp. 1 blocks size, Blocks in group 2, Grp. 2 blocks size)]
# GROUPS_AND_BLOCKS_TABLE = ((1,16,0,0),(1,19,0,0),(1,9,0,0),(1,13,0,0),(1,28,0,0),(1,34,0,0),(1,16,0,0),(1,22,0,0),(1,44,0,0),(1,55,0,0),(2,13,0,0),(2,17,0,0),(2,32,0,0),(1,80,0,0),(4,9, 0,0),(2,24,0,0),(2,43,0,0),(1,108,0,0),(2,11,2,12),(2,15,2,16),(4,27,0,0),(2,68,0,0),(4,15,0,0),(4,19,0,0),(4,31,0,0),(2,78,0,0),(4,13,1,14),(2,14,4,15),(2,38,2,39),(2,97,0,0),(4,14,2,15),(4,18,2,19),(3,36,2,37),(2,116,0,0),(4,12,4,13),(4,16,4,17),(4,43,1,44),(2,68,2,69),(6,15,2,16),(6,19,2,20),(1,50,4,51),(4,81,0,0),(3,12,8,13),(4,22,4,23),(6,36,2,37),(2,92,2,93),(7,14,4,15),(4,20,6,21),(8,37,1,38),(4,107,0,0),(12,11,4,12),(8,20,4,21),(4,40,5,41),(3,115,1,116),(11,12,5,13),(11,16,5,17),(5,41,5,42),(5,87,1,88),(11,12,7,13),(5,24,7,25),(7,45,3,46),(5,98,1,99),(3,15,13,16),(15,19,2,20),(10,46,1,47),(1,107,5,108),(2,14,17,15),(1,22,15,23),(9,43,4,44),(5,120,1,121),(2,14,19,15),(17,22,1,23),(3,44,11,45),(3,113,4,114),(9,13,16,14),(17,21,4,22),(3,41,13,42),(3,107,5,108),(15,15,10,16),(15,24,5,25),(17,42,0,0),(4,116,4,117),(19,16,6,17),(17,22,6,23),(17,46,0,0),(2,111,7,112),(34,13,0,0),(7,24,16,25),(4,47,14,48),(4,121,5,122),(16,15,14,16),(11,24,14,25),(6,45,14,46),(6,117,4,118),(30,16,2,17),(11,24,16,25),(8,47,13,48),(8,106,4,107),(22,15,13,16),(7,24,22,25),(19,46,4,47),(10,114,2,115),(33,16,4,17),(28,22,6,23),(22,45,3,46),(8,122,4,123),(12,15,28,16),(8,23,26,24),(3,45,23,46),(3,117,10,118),(11,15,31,16),(4,24,31,25),(21,45,7,46),(7,116,7,117),(19,15,26,16),(1,23,37,24),(19,47,10,48),(5,115,10,116),(23,15,25,16),(15,24,25,25),(2,46,29,47),(13,115,3,116),(23,15,28,16),(42,24,1,25),(10,46,23,47),(17,115,0,0),(19,15,35,16),(10,24,35,25),(14,46,21,47),(17,115,1,116),(11,15,46,16),(29,24,19,25),(14,46,23,47),(13,115,6,116),(59,16,1,17),(44,24,7,25),(12,47,26,48),(12,121,7,122),(22,15,41,16),(39,24,14,25),(6,47,34,48),(6,121,14,122),(2,15,64,16),(46,24,10,25),(29,46,14,47),(17,122,4,123),(24,15,46,16),(49,24,10,25),(13,46,32,47),(4,122,18,123),(42,15,32,16),(48,24,14,25),(40,47,7,48),(20,117,4,118),(10,15,67,16),(43,24,22,25),(18,47,31,48),(19,118,6,119),(20,15,61,16),(34,24,34,25))
# #{Exponent:Integer}
# QRCODE_GF256_LOG = {0:1,1:2,2:4,3:8,4:16,5:32,6:64,7:128,8:29,9:58,10:116,11:232,12:205,13:135,14:19,15:38,16:76,17:152,18:45,19:90,20:180,21:117,22:234,23:201,24:143,25:3,26:6,27:12,28:24,29:48,30:96,31:192,32:157,33:39,34:78,35:156,36:37,37:74,38:148,39:53,40:106,41:212,42:181,43:119,44:238,45:193,46:159,47:35,48:70,49:140,50:5,51:10,52:20,53:40,54:80,55:160,56:93,57:186,58:105,59:210,60:185,61:111,62:222,63:161,64:95,65:190,66:97,67:194,68:153,69:47,70:94,71:188,72:101,73:202,74:137,75:15,76:30,77:60,78:120,79:240,80:253,81:231,82:211,83:187,84:107,85:214,86:177,87:127,88:254,89:225,90:223,91:163,92:91,93:182,94:113,95:226,96:217,97:175,98:67,99:134,100:17,101:34,102:68,103:136,104:13,105:26,106:52,107:104,108:208,109:189,110:103,111:206,112:129,113:31,114:62,115:124,116:248,117:237,118:199,119:147,120:59,121:118,122:236,123:197,124:151,125:51,126:102,127:204,128:133,129:23,130:46,131:92,132:184,133:109,134:218,135:169,136:79,137:158,138:33,139:66,140:132,141:21,142:42,143:84,144:168,145:77,146:154,147:41,148:82,149:164,150:85,151:170,152:73,153:146,154:57,155:114,156:228,157:213,158:183,159:115,160:230,161:209,162:191,163:99,164:198,165:145,166:63,167:126,168:252,169:229,170:215,171:179,172:123,173:246,174:241,175:255,176:227,177:219,178:171,179:75,180:150,181:49,182:98,183:196,184:149,185:55,186:110,187:220,188:165,189:87,190:174,191:65,192:130,193:25,194:50,195:100,196:200,197:141,198:7,199:14,200:28,201:56,202:112,203:224,204:221,205:167,206:83,207:166,208:81,209:162,210:89,211:178,212:121,213:242,214:249,215:239,216:195,217:155,218:43,219:86,220:172,221:69,222:138,223:9,224:18,225:36,226:72,227:144,228:61,229:122,230:244,231:245,232:247,233:243,234:251,235:235,236:203,237:139,238:11,239:22,240:44,241:88,242:176,243:125,244:250,245:233,246:207,247:131,248:27,249:54,250:108,251:216,252:173,253:71,254:142,255:1}
# #{Integer:Exponent}
# QRCODE_GF256_ANTILOG = {1:0,2:1,3:25,4:2,5:50,6:26,7:198,8:3,9:223,10:51,11:238,12:27,13:104,14:199,15:75,16:4,17:100,18:224,19:14,20:52,21:141,22:239,23:129,24:28,25:193,26:105,27:248,28:200,29:8,30:76,31:113,32:5,33:138,34:101,35:47,36:225,37:36,38:15,39:33,40:53,41:147,42:142,43:218,44:240,45:18,46:130,47:69,48:29,49:181,50:194,51:125,52:106,53:39,54:249,55:185,56:201,57:154,58:9,59:120,60:77,61:228,62:114,63:166,64:6,65:191,66:139,67:98,68:102,69:221,70:48,71:253,72:226,73:152,74:37,75:179,76:16,77:145,78:34,79:136,80:54,81:208,82:148,83:206,84:143,85:150,86:219,87:189,88:241,89:210,90:19,91:92,92:131,93:56,94:70,95:64,96:30,97:66,98:182,99:163,100:195,101:72,102:126,103:110,104:107,105:58,106:40,107:84,108:250,109:133,110:186,111:61,112:202,113:94,114:155,115:159,116:10,117:21,118:121,119:43,120:78,121:212,122:229,123:172,124:115,125:243,126:167,127:87,128:7,129:112,130:192,131:247,132:140,133:128,134:99,135:13,136:103,137:74,138:222,139:237,140:49,141:197,142:254,143:24,144:227,145:165,146:153,147:119,148:38,149:184,150:180,151:124,152:17,153:68,154:146,155:217,156:35,157:32,158:137,159:46,160:55,161:63,162:209,163:91,164:149,165:188,166:207,167:205,168:144,169:135,170:151,171:178,172:220,173:252,174:190,175:97,176:242,177:86,178:211,179:171,180:20,181:42,182:93,183:158,184:132,185:60,186:57,187:83,188:71,189:109,190:65,191:162,192:31,193:45,194:67,195:216,196:183,197:123,198:164,199:118,200:196,201:23,202:73,203:236,204:127,205:12,206:111,207:246,208:108,209:161,210:59,211:82,212:41,213:157,214:85,215:170,216:251,217:96,218:134,219:177,220:187,221:204,222:62,223:90,224:203,225:89,226:95,227:176,228:156,229:169,230:160,231:81,232:11,233:245,234:22,235:235,236:122,237:117,238:44,239:215,240:79,241:174,242:213,243:233,244:230,245:231,246:173,247:232,248:116,249:214,250:244,251:234,252:168,253:80,254:88,255:175}

# #{Version:Remainder bits}
# REQUIRED_REMAINDER_BITS = {1:0,2:7,3:7,4:7,5:7,6:7,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:3,15:3,16:3,17:3,18:3,19:3,20:3,21:4,22:4,23:4,24:4,25:4,26:4,27:4,28:3,29:3,30:3,31:3,32:3,33:3,34:3,35:0,36:0,37:0,38:0,39:0,40:0}

def get_positioning_patterns_positions(version: int) -> tuple:
    """Returns the positioning patterns positions according to the version of the QR-Code."""
    longest_coord = 13 + 4 * version
    return ((3,3),(3,longest_coord),(longest_coord,3))

def draw_dot_pattern(qr_code: list, pos_y: int, pos_x: int, radius: int):
    """Draws a single dot-like pattern in a given QR-Code at specified coordinates, using a provided radius."""
    start_y, start_x = pos_y - radius, pos_x - radius
    end_y, end_x = pos_y + radius, pos_x + radius
    white_line_1_y, white_line_1_x = start_y + 1, start_x + 1
    white_line_2_y, white_line_2_x = end_y  - 1, end_x - 1
    for i in range(start_y,end_y+1):
        if i != white_line_1_y and i != white_line_2_y:
            for j in range(start_x,end_x+1):
                if (j != white_line_1_x and j != white_line_2_x) or i == start_y or i == end_y:
                    qr_code[i][j] = 1
                else:
                    qr_code[i][j] = 0
        else:
            qr_code[i][start_x] = 1
            qr_code[i][end_x] = 1
            for j in range(start_x+1,end_x):
                qr_code[i][j] = 0

def draw_separator(qr_code: list, pos_y: int, pos_x: int) -> None:
    """Draws a separator pattern on the given QR-Code at specified coordinates."""
    if pos_y-4 > 0:
        for i in range(pos_x-4,pos_x+5):
            if i>=0 and i<len(qr_code[0]):
                qr_code[pos_y-4][i] = 0
    if pos_y+4 < len(qr_code):
        for i in range(pos_x-4,pos_x+5):
            if i>=0 and i<len(qr_code[0]):
                qr_code[pos_y+4][i] = 0
    if pos_x-4 > 0:
        for i in range(pos_y-4,pos_y+5):
            if i>=0 and i<len(qr_code):
                qr_code[i][pos_x-4] = 0
    if pos_x+4 < len(qr_code[0]):
        for i in range(pos_y-4,pos_y+5):
            if i>=0 and i<len(qr_code):
                qr_code[i][pos_x+4] = 0

def draw_positioning(qr_code: list, version: int):
    """Draws the positioning patterns of a QR-Code."""
    for p in get_positioning_patterns_positions(version):
        draw_dot_pattern(qr_code,p[0],p[1],3)
        draw_separator(qr_code,p[0],p[1])

def do_positioning_and_alignment_intersect(po: tuple, al: tuple) -> bool:
    """Determines if positioning and alignment patterns intersect each others."""
    if abs(po[0]-al[0]) < 7 and abs(po[1]-al[1]) < 7:
        return True
    return False

def get_alignment_patterns_positions(version: int) -> tuple:
    """Returns the alignment patterns positions according to the version of the QR-Code."""
    coordinates = []
    if version > 1:
        intervals = (version // 7) + 1  # Number of gaps between alignment patterns
        distance = 4 * version + 4  # Distance between first and last alignment pattern
        step = round(distance / intervals)  # Round equal spacing to nearest integer
        step += step%2  # Round step to next even number
        coordinates.append(6)  # First coordinate is always 6 (can't be calculated with step)
        for i in range(1, intervals+1):
            coordinates.append(6 + distance - step * (intervals - i))  # Start ri/bo and go le/up
    final_coordinates = []
    for i in coordinates:
        for j in coordinates:
            final_coordinates.append((i,j))
    return tuple(final_coordinates)

def draw_alignment(qr_code: list, version: int):
    """Draws the alignment patterns of a QR-Code."""
    po_pos = get_positioning_patterns_positions(version)
    al_pos = get_alignment_patterns_positions(version)
    for al_p in al_pos:
        is_valid = True
        for po_p in po_pos:
            if do_positioning_and_alignment_intersect(po_p,al_p):
                is_valid = False
                break
        if is_valid:
            draw_dot_pattern(qr_code,al_p[1],al_p[0],2)

def draw_timing(qr_code: list, version: int):
    """Draws the timing pattern on the provided QR-Code."""
    po_pos = get_positioning_patterns_positions(version)
    y = po_pos[0][0] + 3
    x = po_pos[0][1] + 5
    stop = po_pos[1][1] - 4
    flipper = True
    while x < stop:
        if flipper:
            qr_code[y][x] = 1
        else:
            qr_code[y][x] = 0
        flipper = not flipper
        x += 1
    y += 2
    x = po_pos[0][1] + 3
    stop = po_pos[2][0] - 4
    flipper = True
    while y < stop:
        if flipper:
            qr_code[y][x] = 1
        else:
            qr_code[y][x] = 0
        flipper = not flipper
        y += 1

def draw_dark_module(qr_code: list) -> None:
    """Draws the dark module on the given QR-Code."""
    qr_code[-8][8] = 1

def write_version_information(qr_code: list, version: int):
    """Writes the version information string on the given QR-Code."""
    if version < 7:
        return
    vis = VERSION_INFORMATION_STRINGS[version]
    # TODO : Could compute the version information string instead of listing all of them...
    start = 4 * version + 6
    for i in range(6):
        for j in range(3):
            digit = int(vis[-(3 * i + j + 1)])
            qr_code[i][start + j] = digit
            qr_code[start + j][i] = digit

def get_format_information_string(ecl: int, mask: int) -> str:
    """Returns the format information string according to the given parameters."""
    fs = ""
    bin_ecl = format(ecl,'b')
    for _ in range(2-len(bin_ecl)):
        bin_ecl  = "0" + bin_ecl
    fs += bin_ecl
    bin_mask = format(mask,'b')
    for _ in range(3-len(bin_mask)):
        bin_mask = "0" + bin_mask
    fs += bin_mask
    generator_polynomial_coefficients = "10100110111"
    # Format string division.
    dividende = fs + "0000000000"
    while dividende[0] == "0":
        dividende = dividende[1:]
    while len(dividende) > 10:
        gpc = generator_polynomial_coefficients
        for _ in range(len(dividende) - len(generator_polynomial_coefficients)):
            gpc += "0"
        dividende = format((int(dividende,base=2)^int(gpc,base=2)),'b')
    for _ in range(10 - len(dividende)):
        dividende = "0" + dividende
    fs += dividende
    # XOR with a mask.
    xor_mask_string = "101010000010010"
    fs = format((int(fs,base=2)^int(xor_mask_string,base=2)),'b')
    for _ in range(15 - len(fs)):
        fs = "0" + fs
    return fs

def write_format_information(qr_code: list, ecl:int, mask: int):
    """Writes the format information string on the given QR-Code."""
    fs = get_format_information_string(ecl,mask)
    for i in range(6):
        qr_code[8][i] = int(fs[i])
        qr_code[i][8] = int(fs[-i - 1])
    qr_code[8][7] = int(fs[6])
    qr_code[8][8] = int(fs[7])
    qr_code[7][8] = int(fs[8])
    for i in range(7):
        qr_code[-i - 1][8] = int(fs[i])
    for i in range(8):
        qr_code[8][-8 + i] = int(fs[i + 7])

def numeric_encoding(string: str) -> str:
    """Encodes data with the numeric method into binary string."""
    data = ["" for i in range(len(string)//3)]
    if len(string)%3:
        data.append("")
    for i in range(len(string)):
        data[i//3] += string[i]
    for i in range(len(data)):
        print(data[i])
        tmp = data[i]
        for c in tmp:
            print(c)
            if c == '0':
                data[i] = data[i][1:]
            else:
                break
        print(data[i])
    encoded = ""
    print(data)
    for d in data:
        e = format(int(d),'b')
        match len(d):
            case 1:
                for _ in range(4 - len(e)):
                    encoded += "0"
            case 2:
                for _ in range(7 - len(e)):
                    encoded += "0"
            case 3:
                for _ in range(10 - len(e)):
                    encoded += "0"
        encoded += e
    return encoded

def alphanumeric_encoding(string: str) -> str:
    """Encodes data with the alphanumeric method into binary string."""
    data = ["" for i in range((len(string)//2)+(len(string)%2))]
    for i in range(len(string)):
        data[i//2] += string[i]
    int_data = []
    for d in data:
        if len(d) == 2:
            int_data.append((45 * ALPHANUMERIC_VALUES[d[0]]) + ALPHANUMERIC_VALUES[d[1]])
        else:
            int_data.append(ALPHANUMERIC_VALUES[d[0]])
    encoded = ""
    for i in range(len(int_data)):
        e = format(int_data[i],'b')
        if len(data[i]) == 1:
            for _ in range(6 - len(e)):
                encoded += "0"
        else:
            for _ in range(11 - len(e)):
                encoded += "0"
        encoded += e
    return encoded

def byte_encoding(string: str) -> str:
    """Encodes data with the byte method into binary string."""
    #TODO Byte encoding method.

def kanji_encoding(string: str) -> str:
    """Encodes data with the kanji method into binary string."""
    #TODO Kanji encoding method.

def get_generator_polynomial_coefficient_exponents(ecl: int, version: int) -> list:
    """Returns the exponants of the generator polynomial coefficients corresponding to the provided QR-Code version and error correction level."""
    generator_polynomial_coefficient_exponents = [0,0]
    for i in range(2,ERROR_CORRECTION_CODEWORDS_NUMBER[ecl][version-1]+1):
        temp_term_dict = {0:[]}
        for j in range(len(generator_polynomial_coefficient_exponents)):
            temp_coefficient = generator_polynomial_coefficient_exponents[j]
            temp_term_dict[j + 1] = [temp_coefficient]
            temp_coefficient += (i - 1)
            if temp_coefficient > 255:
                temp_coefficient %= 255
            temp_term_dict[j].append(temp_coefficient)
            if len(temp_term_dict[j]) == 2:
                generator_polynomial_coefficient_exponents[j] = QRCODE_GF256_ANTILOG[QRCODE_GF256_LOG[temp_term_dict[j][0]] ^ QRCODE_GF256_LOG[temp_term_dict[j][1]]]
            else:
                generator_polynomial_coefficient_exponents[j] = temp_term_dict[j][0]
        generator_polynomial_coefficient_exponents.append(0)
    return generator_polynomial_coefficient_exponents

def divide_message_polynomial_by_generator_polymonial(message_polynomial_coefficients: list, generator_polynomial_coefficient_exponents: list) -> list:
    """Returns the result of the division between the two provided polynomials. It can then be used as error correction codewords."""
    gen_pol_coe_exp_len = len(generator_polynomial_coefficient_exponents)
    mes_pol_coe_len = len(message_polynomial_coefficients)
    mpc = [0 for _ in range(mes_pol_coe_len+gen_pol_coe_exp_len-1)]
    for i in range(mes_pol_coe_len):
        mpc[i+gen_pol_coe_exp_len-1] = message_polynomial_coefficients[i]
    gpce = [None for _ in range(mes_pol_coe_len+gen_pol_coe_exp_len-1)]
    for i in range(gen_pol_coe_exp_len):
        gpce[i+mes_pol_coe_len-1] = generator_polynomial_coefficient_exponents[i]
    for i in range(mes_pol_coe_len):
        coeff = QRCODE_GF256_ANTILOG[mpc[-1]]
        tmp_pol = [gpce[j] for j in range(len(gpce))]
        for j in range(len(tmp_pol)):
            if tmp_pol[j] is not None:
                tmp_pol[j] += coeff
                if tmp_pol[j] > 255:
                    tmp_pol[j] %= 255
                tmp_pol[j] = QRCODE_GF256_LOG[tmp_pol[j]]
            else:
                tmp_pol[j] = 0
        for j in range(len(mpc)):
            mpc[j] ^= tmp_pol[j]
        mpc.pop()
        gpce.pop(0)
    return mpc

def get_error_correction(data: list, ecl: int, version: int) -> list:
    """Returns the error correction codewords of the QR-Code, represented in a table."""
    e_c = [[[] for j in range(len(data[i]))] for i in range(len(data))]
    for i in range(len(e_c)):
        if e_c[i] != []:
            for j in range(len(e_c[i])):
                message_polynomial_coefficients = [int(e,base=2) for e in data[i][j]]
                message_polynomial_coefficients.reverse()
                generator_polynomial_coefficient_exponents = get_generator_polynomial_coefficient_exponents(ecl,version)
                ec_codewords = divide_message_polynomial_by_generator_polymonial(message_polynomial_coefficients,generator_polynomial_coefficient_exponents)
                ec_codewords.reverse()
                e_c[i][j] = [format(c,'b') for c in ec_codewords]
                for k in range(len(e_c[i][j])):
                    tmp = e_c[i][j][k]
                    for _ in range(8-len(tmp)):
                        tmp = "0" + tmp
                    e_c[i][j][k] = tmp
    return e_c

def break_data_into_codewords(data: str, version: int, ecl: int) -> list:
    """Converts a string of data into the corresponding codeword table."""
    return [
        [
            [
                data[
                    i*(GROUPS_AND_BLOCKS_TABLE[4*(version-1)+ecl][0]*GROUPS_AND_BLOCKS_TABLE[4*(version-1)+ecl][1]*8)+j*(GROUPS_AND_BLOCKS_TABLE[4*(version-1)+ecl][(i*2)+1]*8)+(k*8)
                    :
                    i*(GROUPS_AND_BLOCKS_TABLE[4*(version-1)+ecl][0]*GROUPS_AND_BLOCKS_TABLE[4*(version-1)+ecl][1]*8)+j*(GROUPS_AND_BLOCKS_TABLE[4*(version-1)+ecl][(i*2)+1]*8)+(k*8)+8
                ]
                for k in range(GROUPS_AND_BLOCKS_TABLE[4*(version-1)+ecl][(i*2)+1])
            ]
            for j in range(GROUPS_AND_BLOCKS_TABLE[4*(version-1)+ecl][i*2])
        ]
    for i in range(2)]

def structure_data(data_codewords: list, ec_codewords: list, version: int) -> str:
    """Returns the entire QR-Code data with error correction properly structured as a string of 0 and 1."""
    data = ""
    if len(data_codewords[0]) == 1:
        for c in data_codewords[0][0]:
            data += c
        for c in ec_codewords[0][0]:
            data += c
    else:
        greatest_len = len(data_codewords[0][0])
        if len(data_codewords[1]) != 0:
            if len(data_codewords[1][0]) > greatest_len:
                greatest_len = len(data_codewords[1][0])
        for i in range(greatest_len):
            for j in range(len(data_codewords[0])):
                if len(data_codewords[0][j]) > i:
                    data += data_codewords[0][j][i]
            if len(data_codewords[1]) != 0:
                for j in range(len(data_codewords[0])):
                    if len(data_codewords[0][j]) > i:
                        data += data_codewords[0][j][i]
        for i in range(len(ec_codewords[0][0])):
            for j in range(len(ec_codewords[0])):
                data += ec_codewords[0][j][i]
            if len(ec_codewords[1]) != 0:
                for j in range(len(ec_codewords[0])):
                    data += ec_codewords[0][j][i]
    for i in range(REQUIRED_REMAINDER_BITS[version]):
        data += "0"
    return data

def get_data(data: str, data_type: int, ecl: int, version: int) -> str:
    """Returns the data converted to binary and organised into codewords, ready to be written within the QR-Code."""
    d = ""
    d += MODE_INDICATORS[data_type]
    char_count_indicator = format(len(data),'b')
    cci_length = 0
    if version < 10:
        cci_length = CHARACTER_COUNT_INDICATORS_LENGTHS[0][data_type]
    elif version < 27:
        cci_length = CHARACTER_COUNT_INDICATORS_LENGTHS[1][data_type]
    else:
        cci_length = CHARACTER_COUNT_INDICATORS_LENGTHS[2][data_type]
    for _ in range(cci_length - len(char_count_indicator)):
        d += "0"
    d += char_count_indicator
    d += alphanumeric_encoding(data)
    terminator_length = (DATA_CODEWORDS_NUMBER[ecl][version-1] * 8) - len(d)
    if terminator_length > 4:
        terminator_length = 4
    for _ in range(terminator_length):
        d += "0"
    pad = len(d)%8
    for _ in range(pad):
        d += "0"
    remaining = DATA_CODEWORDS_NUMBER[ecl][version-1] - (len(d) // 8)
    for _ in range(remaining//2):
        d += "1110110000010001"
    for _ in range(remaining%2):
        d += "11101100"
    data_codewords = break_data_into_codewords(d,version,ecl)
    # print("Groups: ",len(data_codewords))
    # print("Blocks in group 1: ",len(data_codewords[0]))
    # print("Blocks in group 2: ",len(data_codewords[1]))
    # print("Codewords in group 1's blocks: ",len(data_codewords[0][0]))
    ec_codewords = get_error_correction(data_codewords,ecl,version)
    structured_data = structure_data(data_codewords,ec_codewords,version)
    return structured_data

def get_writing_path(qr_code: list, version: int) -> list:
    """Returns a list of the path to follow to write in the QR-Code."""
    path = []
    going_up = True
    even = False
    vertical_mode = False
    x = len(qr_code[0])-1
    y = len(qr_code)-1
    while x >= 0:
        path.append([y,x])
        if vertical_mode:
            if going_up:
                y -= 1
                if qr_code[y][x+1] == -1: # End of vertical mode.
                    x += 1
                    vertical_mode = False
                    even = False
                elif y == 6: # Reaching Horizontal timing line while next to an alignment pattern.
                    y -= 1
            else:
                y += 1
                if y == 6: # Reaching Horizontal timing line while next to the version information zone.
                    x += 1
                    y += 1
                    vertical_mode = False
                    even = False
        else:
            if even:
                x += 1
                if going_up:
                    y -= 1
                    if vertical_mode:
                        if y == 6: # Reaching Horizontal timing line.
                            y -= 1
                    else:
                        if y == 8 and (x <= 8 or x >= len(qr_code[0])-8): # Reaching Format information line while going up.
                            x -= 2
                            y += 1
                            going_up = False
                            if x == 6: # Reaching Vertical timing line.
                                x -= 1
                        elif y == 6: # Reaching Horizontal timing line.
                            y -= 1
                            if version >= 7 and x >= len(qr_code[0])-11: # Reaching top Version information zone.
                                y = 0
                                x -= 3
                                vertical_mode = True
                                going_up = False
                        elif y < 0: # Reaching edge of QR-Code.
                            x -= 2
                            y += 1
                            going_up = False
                        elif qr_code[y][x] == 1: # Reaching Alignment pattern.
                            if qr_code[y][x-1] == 1: # If not on the side.
                                y -= 5
                            else: # If on the side.
                                x -= 1
                                vertical_mode = True
                else:
                    y += 1
                    if y == len(qr_code)-8 and x <= 8: # Reaching Separator or dark module while going down.
                        x -= 2
                        y -= 1
                        going_up = True
                    elif version >= 7 and y >= len(qr_code)-11 and x <= 5: # Reaching bottom Version information zone.
                        x -= 2
                        y -= 1
                        going_up = True
                    elif y >= len(qr_code): # Reaching edge of QR-Code.
                        x -= 2
                        y -= 1
                        going_up = True
                        if x <= 8: # Reaching Format information line while going left.
                            y -= 8
                    elif y == 6: # Reaching Horizontal timing line.
                        y += 1
                    elif qr_code[y][x] == 1: # Reaching Alignment pattern.
                        y += 5
            else:
                x -= 1
            even = not even
    return path

def write_data(qr_code: list, data:str, data_path: list, version: int):
    """Writes the data provided into the given QR-Code."""
    for i in range(len(data_path)):
        qr_code[data_path[i][0]][data_path[i][1]] = int(data[i])

def determine_version_and_ecl(data: str, data_type: int, ecl: int) -> int:
    """Determines the necessary version and error correction level according to the quantity of data to be stored."""
    data_length = len(data)
    version = 40
    while version > 0 and CAPACITIES[data_type][ecl][version-1] > data_length:
        version -= 1
    return version + 1

def apply_mask(qr_code: list, mask: int, data_path: list) -> None:
    """Applies a given mask on the provided QR-Code."""
    for i, j in data_path:
        selected = False
        match mask:
            case 0:
                if (i+j)%2 == 0:
                    selected = True
            case 1:
                if i%2 == 0:
                    selected = True
            case 2:
                if j%3 == 0:
                    selected = True
            case 3:
                if (i+j)%3 == 0:
                    selected = True
            case 4:
                if ((i//2)+(j//3))%2 == 0:
                    selected = True
            case 5:
                if ((i*j)%2)+((i*j)%3) == 0:
                    selected = True
            case 6:
                if (((i*j)%2)+((i*j)%3))%2 == 0:
                    selected = True
            case 7:
                if (((i+j)%2)+((i*j)%3))%2 == 0:
                    selected = True
            case (_):
                print(f"Wrong mask number! Expected between 0 and 7, got {mask}.")
                return
        if selected:
            qr_code[i][j] = pow((qr_code[i][j]-1),2)

def mask_evaluation_1(qr_code: list) -> int:
    """Evaluates the first penalty condition on the given QR-Code."""
    penalty = 3
    total = 0
    for i in range(len(qr_code)):
        it = 0
        while it < len(qr_code[i]) - 4:
            if qr_code[i][it + 1] == qr_code[i][it]:
                if qr_code[i][it + 2] == qr_code[i][it]:
                    if qr_code[i][it + 3] == qr_code[i][it]:
                        if qr_code[i][it + 4] == qr_code[i][it]:
                            total += penalty
                            it += 5
                            while it < len(qr_code[i]) and qr_code[i][it] == qr_code[i][it - 1]:
                                total += 1
                                it += 1
                        else:
                            it += 4
                    else:
                        it += 3
                else:
                    it += 2
            else:
                it += 1
    for i in range(len(qr_code[0])):
        it = 0
        while it < len(qr_code) - 4:
            if qr_code[it + 1][i] == qr_code[it][i]:
                if qr_code[it + 2][i] == qr_code[it][i]:
                    if qr_code[it + 3][i] == qr_code[it][i]:
                        if qr_code[it + 4][i] == qr_code[it][i]:
                            total += penalty
                            it += 5
                            while it < len(qr_code) and qr_code[it][i] == qr_code[it - 1][i]:
                                total += 1
                                it += 1
                        else:
                            it += 4
                    else:
                        it += 3
                else:
                    it += 2
            else:
                it += 1
    return total

def mask_evaluation_2(qr_code: list) -> int:
    """Evaluates the second penalty condition on the given QR-Code."""
    penalty = 3
    total = 0
    for i in range(len(qr_code) - 1):
        for j in range(len(qr_code[i]) - 1):
            if qr_code[i][j + 1] == qr_code[i][j]:
                if qr_code[i + 1][j] == qr_code[i][j]:
                    if qr_code[i + 1][j + 1] == qr_code[i][j]:
                        total += penalty
    return total

def mask_evaluation_3(qr_code: list) -> int:
    """Evaluates the third penalty condition on the given QR-Code."""
    penalty = 40
    total = 0
    pattern = [1,0,1,1,1,0,1,0,0,0,0]
    for row in qr_code:
        it = 0
        reverse_factor = 1
        for e in row:
            if it == 0:
                if e == pattern[it]:
                    reverse_factor = 1
                    it += 1
                elif e == pattern[-it - 1]:
                    reverse_factor = -1
                    it += 1
            else:
                if e == pattern[reverse_factor * (it + (1 - ((reverse_factor * reverse_factor) + reverse_factor)//2))]: # [it] or [- (it+1)] depending on the sign of the reverse factor (1 or -1).
                    it += 1
                    if it == len(pattern):
                        total += penalty
                        it = 0
                else:
                    it = 0
    for i in range(len(qr_code[0])):
        it = 0
        reverse_factor = 1
        for row in qr_code:
            if it == 0:
                if row[i] == pattern[it]:
                    reverse_factor = 1
                    it += 1
                elif row[i] == pattern[-it - 1]:
                    reverse_factor = -1
                    it += 1
            else:
                if row[i] == pattern[reverse_factor * (it + (1 - ((reverse_factor * reverse_factor) + reverse_factor)//2))]: # [it] or [- (it+1)] depending on the sign of the reverse factor (1 or -1).
                    it += 1
                    if it == len(pattern):
                        total += penalty
                        it = 0
                else:
                    it = 0
    return total

def mask_evaluation_4(qr_code: list) -> int:
    """Evaluates the fourth penalty condition on the given QR-Code."""
    nb_modules = len(qr_code)*len(qr_code[0])
    nb_dark_modules = 0
    for row in qr_code:
        for e in row:
            if e == 1:
                nb_dark_modules += 1
    percent = (nb_dark_modules / nb_modules) * 100
    prev_multiple_of_5 = 5 * (percent//5)
    next_multiple_of_5 = percent + ((5 - (percent % 5))%5)
    penalty_nb_1 = abs(prev_multiple_of_5 - 50) // 5
    penalty_nb_2 = abs(next_multiple_of_5 - 50) // 5
    result = penalty_nb_1
    if penalty_nb_2 < penalty_nb_1:
        result = penalty_nb_2
    return result * 10

def select_mask(qr_code: list, data_path: list) -> int:
    """Returns the number of the best mask to use on the given QR-Code, based on the standard QR-CODE rules."""
    best_mask = 0
    lowest_penalty = 0      # Bad calculus : (2 * (len(qr_code) * (len(qr_code)-2))) + (3 * ((len(qr_code)-1) * (len(qr_code)-1))) + (40 * (2 * (2 * (len(qr_code))))) + (100)
    for mask in range(8):
        tmp_qr = []
        penalty = 0
        for i in range(len(qr_code)):
            tmp_qr.append([])
            for j in range(len(qr_code[i])):
                tmp_qr[i].append(qr_code[i][j])
        apply_mask(tmp_qr,mask,data_path)
        penalty += mask_evaluation_1(tmp_qr)
        penalty += mask_evaluation_2(tmp_qr)
        penalty += mask_evaluation_3(tmp_qr)
        penalty += mask_evaluation_4(tmp_qr)
        if mask == 0:
            lowest_penalty = penalty
        elif penalty < lowest_penalty:
            lowest_penalty = penalty
            best_mask = mask
    return best_mask

def qr_generator(data: str, data_type: int, error_correction_level: chr) -> list:
    """Generates a QR-Code of specified size containing the provided data of specified data type."""
    # if version > 40 or version < 1:
    #     print(f"Wrong QR-Code version! Expected between 1 and 40, got {version}.")
    #     return None
    if error_correction_level not in ('L','M','Q','H'):
        print(f"Invalid error correction level. Expected one of (L, M, Q, H), got : {error_correction_level}")
        return None
    if data_type > 3 or data_type < 0:
        print(f"Wrong data type! Expected between 0 and 3, got {data_type}.")
        return None
    ecl = ERROR_CORRECTION_LEVELS[error_correction_level]
    version = determine_version_and_ecl(data, data_type, ecl)
    if version > 40:
        print(f"Too many data to store! For {DATA_TYPES[data_type]} data, with error correction level {error_correction_level}, the maximum amount of data storable is {CAPACITIES[data_type][ERROR_CORRECTION_LEVELS[error_correction_level]][39]}, got {len(data)}.")
        return None
    print("##### Version: ",version)
    print("##### Error Correction Level: ",error_correction_level)
    size = 17 + 4 * version
    qr_code = [[-1 for j in range(size)] for i in range(size)]
    draw_positioning(qr_code, version)
    draw_alignment(qr_code,version)
    draw_timing(qr_code,version)
    draw_dark_module(qr_code)
    write_version_information(qr_code,version)
    data_area = get_writing_path(qr_code,version)
    write_data(qr_code,get_data(data,data_type,ecl,version),data_area,version)
    mask = select_mask(qr_code,data_area)
    apply_mask(qr_code,mask,data_area)
    write_format_information(qr_code,ecl,mask)
    return qr_code

def flatten(tab: list) -> list:
    """Flattens a table into a list of depth 1."""
    res = []
    for e in tab:
        if isinstance(e, list):
            for v in flatten(e):
                res.append(v)
        else:
            res.append(e)
    return res

def print_tab(tab: list):
    """Prints a list in a more readable way."""
    for row in tab:
        print(row)

def mask_it(tab,mask):
    """Mask da tab real quick."""
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            selected = False
            match mask:
                case 0:
                    if (i+j)%2 == 0:
                        selected = True
                case 1:
                    if i%2 == 0:
                        selected = True
                case 2:
                    if j%3 == 0:
                        selected = True
                case 3:
                    if (i+j)%3 == 0:
                        selected = True
                case 4:
                    if ((i//2)+(j//3))%2 == 0:
                        selected = True
                case 5:
                    if ((i*j)%2)+((i*j)%3) == 0:
                        selected = True
                case 6:
                    if (((i*j)%2)+((i*j)%3))%2 == 0:
                        selected = True
                case 7:
                    if (((i+j)%2)+((i*j)%3))%2 == 0:
                        selected = True
                case (_):
                    print(f"Wrong mask number! Expected between 0 and 7, got {mask}.")
                    return
            if selected:
                tab[i][j] = pow((tab[i][j]-1),2)

def display_qr_code(qr_code: list):
    """Displays the given QR-Code."""
    print("")
    print("")
    for row in qr_code:
        print("\t",end="")
        for digit in row:
            if digit == 1:
                print("■",end="")
            elif digit == 0:
                print(" ",end="")
            elif digit == 2:
                print("⬤",end="")
            else:
                print("X",end="")
            print(" ",end="")
        print("")
    print("")
    print("")

DATA = "HELLO THERE."
QRCODE = qr_generator(DATA,1,'H')
display_qr_code(QRCODE)
