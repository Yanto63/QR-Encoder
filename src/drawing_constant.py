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