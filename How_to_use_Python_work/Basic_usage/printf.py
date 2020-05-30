#1.  作用：相当于 format() 函数
name = "帅哥"
age = 12
print(f"my name is {name},age is {age}")
# result
# my name is 帅哥,age is 12

#2. r""  的作用是：去除转义字符
# 场景：想复制某个文件夹的目录，假设是 F:\Python_Easy\n4\test.py
# 当你不用 r"" ，你有三种写法

print("F:\Python_Easy\n4\test.py ")
print("F:\\Python_Easy\\n4\\test.py ")
print("F:/Python_Easy/n4/test.py ")

# 而通常如果直接复制目录路径的话，你就粘贴出来的字符串就是第一行代码所示，所有 \ 会当成转义符；而为了消除转义作用，需要手动再加一个 \ ，否则你也得手动改成第三行代码一样

# result
# F:\Python_Easy
# 4    est.py
# F:\Python_Easy\n4\test.py
# F:/Python_Easy/n4/test.py

# 而 r"" 的出现就是为了避免这种情况，如下：
print(r"F:\Python_Easy\n4\test.py ")
# F:\Python_Easy\n4\test.py

#3. b" "的作用是：后面字符串是bytes 类型
print("中文".encode(encoding="utf-8"))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode())
print(r'\xe4\xb8\xad\xe6\x96\x87')

b'\xe4\xb8\xad\xe6\x96\x87'
中文
\xe4\xb8\xad\xe6\x96\x87

#4. 加u的 作用：后面字符串以 Unicode 格式 进行编码

# 实际场景：一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。

# 建议所有编码方式采用 utf8
