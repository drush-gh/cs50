import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        octets = ip.split(".")
    else:
        return False
    for octet in octets:
        if octet.startswith("0") and not octet == "0":
            return False
        if int(octet) not in range(256):
            return False
    return True

if __name__ == "__main__":
    main()
