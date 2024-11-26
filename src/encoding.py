from QRCodeStandards import ALPHANUMERIC_VALUES

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
    encoded = ""
    for c in string:
        h = ord(c.encode("iso_8859_1","ignore"))
        b = bin(h)[2:]
        for _ in range(8 - len(b)):
            b = "0" + b
        encoded += b
    return encoded

def kanji_encoding(string: str) -> str:
    """Encodes data with the kanji method into binary string."""
    #TODO Kanji encoding method.
