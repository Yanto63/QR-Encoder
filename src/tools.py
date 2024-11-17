from QRCodeStandards import CAPACITIES

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

def determine_version_and_ecl(data: str, data_type: int, ecl: int) -> int:
    """Determines the necessary version and error correction level according to the quantity of data to be stored."""
    data_length = len(data)
    version = 40
    while version > 0 and CAPACITIES[data_type][ecl][version-1] > data_length:
        version -= 1
    return version + 1

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

def display_qr_code(qr_code: list):
    """Displays the given QR-Code."""
    for _ in range(4):
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
    for _ in range(4):
        print("")