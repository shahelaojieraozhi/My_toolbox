import os


# 返回所有待删文件绝对路径的函数，为了删除文件需要，os.remove必须要绝对路径
def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        # os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result


def main():
    path = './train2017'    # 这里放要删除文件
    list1 = all_path(path)      # list1 返回都是每个txt的绝对路径了如'./train2017\\9_5360_6656_640_640_0_8192_6000.txt, .....'

    remove_path = './train_delete.txt'      # 这是存了他们名字的文件
    with open(remove_path) as f:
        list2 = list(map(lambda s: s.strip(), f.readlines()))
        # list2 返回的是每个待删除文件的名字  如'385_3072_3584_640_640_0_8192_6000'

    list3 = []
    # 得到所有待删除文件的名字并添加到list3中
    for i in range(len(list1)):
        line = os.path.split(list1[i])[-1].split('/')[0]
        # 返回踢除了主目录的文件，相当于只留了文件的完成名字如：'0_1024_4096_640_640_0_8192_6000.txt'
        fname = os.path.splitext(line)[0]
        # 把.txt 去掉，获取'0_1024_4096_640_640_0_8192_6000'
        # 用于判定结果 '0_1024_4096_640_640_0_8192_6000' == '0_1024_4096_640_640_0_8192_6000' 时删除这个文件
        list3.append(fname)

    list4 = []
    # 将待删除文件路径添加到list4中

    for j in range(len(list3)):
        for k in range(len(list2)):
            if list3[j] == list2[k]:
                # 对应上述的——用于判定结果 '0_1024_4096_640_640_0_8192_6000' == '0_1024_4096_640_640_0_8192_6000' 时删除这个文件
                out_path = list1[j]     # out_path 返回的是存了绝对路径的list1 如 './train2017\\0_1024_4096_640_640_0_8192_6000.txt'
                list4.append(out_path)

    for n in range(len(list4)):
        os.remove(list4[n])     # 一个一个删了


if __name__ == '__main__':
    main()
