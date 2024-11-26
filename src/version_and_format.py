def get_version_information_string(version: int) -> str:
    """Returns the version information string according to the given QR-Code version."""
    if version < 7:
        return
    vs = ""
    bin_version = format(version,'b')
    for _ in range(6-len(bin_version)):
        bin_version  = "0" + bin_version
    vs += bin_version
    generator_polynomial_coefficients = "1111100100101"
    # Format string division.
    dividende = vs + "000000000000"
    while dividende[0] == "0":
        dividende = dividende[1:]
    while len(dividende) > 12:
        gpc = generator_polynomial_coefficients
        for _ in range(len(dividende) - len(generator_polynomial_coefficients)):
            gpc += "0"
        dividende = format((int(dividende,base=2)^int(gpc,base=2)),'b')
    for _ in range(12 - len(dividende)):
        dividende = "0" + dividende
    vs += dividende
    return vs

def write_version_information(qr_code: list, version: int):
    """Writes the version information string on the given QR-Code."""
    if version < 7:
        return
    vis = get_version_information_string(version)
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
