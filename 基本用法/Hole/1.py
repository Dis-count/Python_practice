#  about string operation.
# 1.
a = "some_string"

id(a)

id("some" + "_" + "string") # 注意两个的id值是相同的.

# 2.
a = "wtf"
b = "wtf"

a is b

a = "wtf!"
b = "wtf!"

a is b

a, b = "wtf!", "wtf!"

a is b

# 3.

'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'

'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'

import antigravity
import this
