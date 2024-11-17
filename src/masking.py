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