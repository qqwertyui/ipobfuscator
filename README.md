### ipobfuscator

#### How it works?
Single ip address can be written in multiple ways. The most popular way is to represent ip as 4 octets separated with dots. The others possible ways is to represent ip as a:
- dword (this can be applied to all octets or to few of them)
- represent octets in octal numeric system
- represent octets in hexadecimal numeric system
- mix all those systems


#### Example
For this example I will be using 1.1.1.1:
- dword -> 16843009 (using all octets)
- dword -> 1.65793 (using 3 octets)
- dword -> 1.1.257 (using 2 octets)
- octal base -> 01.01.01.01 (there is no limit for prepending zeros)
- hexadecimal base -> 0x1.0x1.0x1.0x1
- 01.0x1.257 (octal + hexadecimal + dword using 2 octets)

All above addresses are valid and can be interpreted by various software like web browsers (e.g. https://16843009/ has the same effect as https://1.1.1.1) or command line utilites (ping 1.65793) 