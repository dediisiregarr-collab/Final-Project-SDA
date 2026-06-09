def classify_error(message):

    msg = message.lower()

    if "belum ditutup" in msg:
        return "Unclosed Tag"

    if "ditutup dengan" in msg:
        return "Mismatched Tag"

    if "tidak memiliki pasangan" in msg:
        return "Missing Opening Tag"

    return "Unknown Error"