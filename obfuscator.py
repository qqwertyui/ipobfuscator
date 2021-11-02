import sys
import logging

logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

def ip2dword(ip, octets_merged=4):
    result = ""
    if(octets_merged == 1):
        return "{}.{}.{}.{}".format(ip[0],ip[1],ip[2],ip[3])
    end = str(int.from_bytes(bytes(ip[4-octets_merged:4]), "big"))
    for i in range(0, 4-octets_merged):
        result += str(ip[i])+"."
    if(len(end) == 0):
        result = result[0:-1]
    return (result+end)

def ip2octal(ip, zeros=1):
    result = ""
    for i in ip:
        result += zeros*"0"+oct(i)[2:]+"."
    return result.removesuffix(".")    

def ip2hex(ip, merged=True):
    result = ""
    if(merged):
        for i in ip:
            result += hex(i)+"."
        result = result.removesuffix(".")
    else:
        result = hex(int(ip2dword(ip,4)))
    return result

def ip2mixed(ip):
    result = ip2hex(ip).split(".")[0] + "."
    result += ip2octal(ip,12).split(".")[1] + "."
    result += ip2dword(ip,2).split(".")[2]
    return result

def check_ip(ip):
    if(len(ip) != 4):
        return False
    for i in ip:
        if(i < 1 or i > 254):
            return False
    return True

def main():
    if(len(sys.argv) != 2):
        logging.error("Usage: {} <a.b.c.d>".format(sys.argv[0]))
        sys.exit(1)
    ip = [int(i) for i in sys.argv[1].split(".")]
    if(check_ip(ip) == False):
        logging.error("Invalid ip address")
        sys.exit(2)
    logging.info(ip2dword(ip,4))
    logging.info(ip2dword(ip,3))
    logging.info(ip2dword(ip,2))
    logging.info(ip2dword(ip,1))
    logging.info(ip2octal(ip))
    logging.info(ip2octal(ip,3))
    logging.info(ip2octal(ip,8))
    logging.info(ip2hex(ip, merged=True))
    logging.info(ip2hex(ip, merged=False))
    logging.info(ip2mixed(ip))

if __name__ == "__main__":
    main()