import re

def has_leading_zero(str):
    if str == '0':
        return False

    if str[0] != '0':
        return False

    return True

def is_within_range(str):
    num = int(str)

    return num >= 0 and num <= 255


def check_v4(str):
    return (not has_leading_zero(str)) and all(re.search("\d", i)for i in str) and is_within_range(str)

def check_v6(str):
    return (all(re.search("[A-Fa-f0-9]", i) for i in str) and len(str) <= 4)

class IPAddress:
    def validate(self, queryIP):
        v4 = queryIP.split(".")
        v6 = queryIP.split(":")

        if any(i == "" for i in v4):
            return "Neither"

        if any(i == "" for i in v6):
            return "Neither"

        if len(v4) == 4:
            if all(check_v4(i) for i in v4):
                return "IPv4"
        elif len(v6) == 8:
            if all(check_v6(i) for i in v6):
                return "IPv6"

        return "Neither"



inputs = [
    "172.16.254.1", # => IPv4
    "2001:0db8:85a3:0:0:8A2E:0370:7334", # => IPv6
    "256.256.256.256", # => Neither
]

outputs = [
    "IPv4",
    "IPv6",
    "Neither",
]

for i, el in enumerate(inputs):
    assert IPAddress().validate(inputs[i]) == outputs[i]

print('ok')
