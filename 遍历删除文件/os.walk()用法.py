import os

# dirname = './train2017'
# for maindir, subdir, file_name_list in os.walk(dirname):
#     for filename in file_name_list:
#         apath = os.path.join(maindir, filename)
#         print(apath)

# 使用os.walk扫描目录
for curDir, dirs, files in os.walk("./os.walk_test"):
    print("====================")
    print("现在的目录：" + curDir)
    print("该目录下包含的子目录：" + str(dirs))
    print("该目录下包含的文件：" + str(files))
