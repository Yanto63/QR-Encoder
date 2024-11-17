from QRCodeStandards import ERROR_CORRECTION_CODEWORDS_NUMBER, QRCODE_GF256_ANTILOG, QRCODE_GF256_LOG

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