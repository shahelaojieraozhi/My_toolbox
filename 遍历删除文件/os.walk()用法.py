import os

# # 使用os.walk扫描目录
# for curDir, dirs, files in os.walk("./os.walk_test"):
#     print("====================")
#     print("现在的目录：" + curDir)
#     print("该目录下包含的子目录：" + str(dirs))
#     print("该目录下包含的文件：" + str(files))

# # 使用os.walk自底向上扫描目录
# import os
#
# for curDir, dirs, files in os.walk("./os.walk_test", topdown=False):
#     print("====================")
#     print("现在的目录：" + curDir)
#     print("该目录下包含的子目录：" + str(dirs))
#     print("该目录下包含的文件：" + str(files))

# 我们还可以利用os.walk输出test文件夹下所有的文件：

# # 使用os.walk输出某个目录下的所有文件
# import os
#
# for curDir, dirs, files in os.walk("./os.walk_test"):
#     for file in files:
#         print(os.path.join(curDir, file))

# 同样地，我们也可以利用os.walk输出test文件夹下所有的子目录（子文件夹）：

# 使用os.walk输出所有的目录
import os

for curDir, dirs, files in os.walk("./os.walk_test"):
    for dir in dirs:
        print(dir)

