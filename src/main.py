### For documentation, see : https://www.thonky.com/qr-code-tutorial/

from sys import argv

from QRCodeStandards import *
from drawing_constant import draw_positioning, draw_alignment, draw_timing, draw_dark_module
from version_and_format import write_version_information, write_format_information
from data_processing import get_data, write_data
from masking import select_mask, apply_mask
from tools import get_writing_path, determine_version_and_ecl, flatten, display_qr_code

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
    write_data(qr_code,get_data(data,data_type,ecl,version),data_area)
    mask = select_mask(qr_code,data_area)
    apply_mask(qr_code,mask,data_area)
    write_format_information(qr_code,ecl,mask)
    return qr_code

if __name__ == "__main__":
    if len(argv) > 2 or (len(argv) == 2 and argv[1] != "-d"):
        print("Use the raw command to print the QR-Code in you terminal.\nUse -h to display this help.\nUse -d to disply it using matplotlib.")
    else:
        message = input("Type your message here: ")
        qrcode = qr_generator(message,2,'H')
        if len(argv) == 2 and argv[1] == "-d":
            from display import display_enhanced
            display_enhanced(qrcode)
        else:
            display_qr_code(qrcode)
