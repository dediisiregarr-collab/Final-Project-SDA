import re

def tokenize(html):
    # Mengambil tag HTML dan teks di dalamnya
    tokens = re.findall(r'<[^>]+>|[^<>]+', html)

    # Menghapus spasi kosong
    tokens = [token.strip() for token in tokens if token.strip()]

    return tokens

# Testing Parser
if __name__ == "__main__":
    html = "<div><p>Hello</p></div>"
    print(tokenize(html))