from QRCodeStandards import GROUPS_AND_BLOCKS_TABLE, REQUIRED_REMAINDER_BITS, MODE_INDICATORS, CHARACTER_COUNT_INDICATORS_LENGTHS, DATA_CODEWORDS_NUMBER
from encoding import numeric_encoding, alphanumeric_encoding, byte_encoding, kanji_encoding
from error_correction import get_error_correction

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
    # TODO : change the enconding according to the data type.
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

def write_data(qr_code: list, data:str, data_path: list, version: int):
    """Writes the data provided into the given QR-Code."""
    for i in range(len(data_path)):
        qr_code[data_path[i][0]][data_path[i][1]] = int(data[i])