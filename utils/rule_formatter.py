import re

result = ''

def dfs(content, num):
    global result
    item = []
    crl = []
    a = []
    b = []
    for i in range(len(content)):
        if content[i] == "{":
            a.append(content[i])
            crl.append(content[i])
        elif content[i] == "}":
            b.append(content[i])
            crl.append(content[i])
        elif content[i] == ";":
            if len(a) == len(b):
                s = ""
                while crl:
                    s += crl.pop()
                item.append(s[::-1] + ";")
                if a and b:
                    a.pop()
                    b.pop()
            else:
                crl.append(content[i])
        else:
            crl.append(content[i])
    if len(crl):
        s = ""
        while crl:
            s += crl.pop()
            item.append(s[::-1] + ";")
    for i in item:
        if "{" in i and i[:4] != "pcre":
            result+="{}{}{}\n".format("\t" * num, i.split("{")[0], "{")
            dfs("};".join("{".join(i.split("{")[1:]).split("};")[:-1]), num + 1)
            result+="{}{}{}\n".format(
                    "\t" * num, "{".join(i.split("{")[1:]).split("};")[-1], "};")
        else:
            result+="{}{}\n".format("\t" * num, i)
def geshihua(raw_rule):
    global result
    # # 原始规则文本
    # with open(r"111.txt", "r") as f:
    #     raw_rule = f.read()
    print("原始规则：\n{}\n{}".format('*'*50,raw_rule))
    result=''
    # 特殊处理 result
    if "result:{" in raw_rule:
        raw_rule = re.sub(r'result:\{(\d+)\}', r'result:{\1;}', raw_rule)
    if "threshold" in raw_rule:
        raw_rule = re.sub(r'threshold:\{([^}]+)\}', r'threshold:{\1;}', raw_rule)

    content = re.findall(r"\x28(.*?)\x29$", raw_rule)[0]

    head = raw_rule.split(content)[0]
    tail = raw_rule.split(content)[1]

    result+=head+'\n'
    dfs(content, 1)
    result+=tail+'\n'
 
    if "result:{" in result:
        result = re.sub(r'result:\{\s*(\d+);\s*\}', r'result:{\1}', result)
    if "threshold" in result:
        result = re.sub(r'threshold:\{\s*([^}]+);\s*\}', r'threshold:{\1}', result)

    print("\n格式化后的：\n{}\n{}".format('*'*50,result))
    return result

def toline(raw_rule):
    t = "".join(raw_rule.split("\n")).replace("\t", "").replace("    ", "")
    return t+'\n'+"总长（不得超出1024）={}".format(len(t))



import re
from datetime import datetime, timedelta

# encoding: utf-8
import re
from datetime import datetime, timedelta
def replace_c(s, c):
    t = s.replace(c, hex(ord(c))).replace("0x", r"\x")
    return t

def hexEncode(s):
    dic = [";", '"', "'", "$", "(", ")"]
    for d in dic:
        if d in s:
            s = replace_c(s, d)
    print(s)
    return s

def hexToStr(s):
    if isinstance(s, str):
        s = bytes.fromhex(s.replace('\\x', ''))
    print(s.decode("utf8"))  # \u8def
    return s.decode("utf8")

def toUnicode(unicode_string):
    print("*"*100)
    print("原始字符串:\n", unicode_string)
    encoded_string = ''.join(r'\u{:04x}'.format(ord(char)) for char in unicode_string)
    encoded_string =  encoded_string.replace(r"\u007c","|").replace(r"\u",r"\\u")
    print("\n编码后的字节串:\n",encoded_string)
    return encoded_string

def fromUnicode(encoded_string):
    print("*"*100)
    encoded_string = encoded_string.replace(r"\\u",r"\u").replace(r"|",r"\u007c")
    import re
    def replace_match(match):
        return chr(int(match.group(1), 16))
    decoded_string = re.sub(r'\\u([0-9a-fA-F]{4})', replace_match, encoded_string)
    print("解码后的字符串:\n", decoded_string)
    return decoded_string

def encode_to_hex(s, flag="e"):
    keys = ['\\','+','~','*','-','^','_','`','@','<','=','>','%','$','#','!','.', '(', ')', '|', '&',  '{', '}', ',', ':', ';', '"',' ','/',"'","?"]
    values = []
    for i in keys:
        values.append(hex(ord(i)).replace("0x","\\x"))
    values[values.index("\\x20")]=r'\s*'
    if flag == "e":
        for k, v in zip(keys, values):
            s = s.replace(k, v)
        print("-" * 50 + " 编码开始 " + "-" * 50)
    else:
        for v, k in zip(values, keys):
            s = s.replace(v, k)
        print("-" * 50 + " 解码开始 " + "-" * 50)
        if '\x5c\x5c' in s:
            s = s.replace('\x5c\x5c','\x5c')
    print(s)
    print("-" * 150)
    return s

def countTime(r='09:41:28.756', seconds_to_add=60):
    original_time = datetime.strptime(r, '%H:%M:%S.%f')
    new_time = original_time + timedelta(seconds=seconds_to_add)
    print(new_time.strftime('%H:%M:%S.%f'))
    return new_time.strftime('%H:%M:%S.%f')

def countSubTime(time_str1='2024-10-10 10:31:59.942', time_str2='2024-10-08 08:08:05.230'):
    time1 = datetime.strptime(time_str1, '%Y-%m-%d %H:%M:%S.%f')
    time2 = datetime.strptime(time_str2, '%Y-%m-%d %H:%M:%S.%f')
    time_difference = time1 - time2
    print(time_difference)
    return str(time_difference)