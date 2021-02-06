#概括字符集

#\d \D
#\w 单词字符 \W
#\s 空白字符 \W
#.匹配除换行符\n之外的其他所有字符
import re
a = 'python 11\t11java&678p\nh\rp'
r = re.findall('\d', a)
print(r)