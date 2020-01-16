

import re

msgs = '显示第 1 到第 1023 条记录，总共 18条记录'

result = re.match('^显示.*到.*?(\d+)',msgs).group(1)

print(result)