import os

dirname = './train2017'
for maindir, subdir, file_name_list in os.walk(dirname):
    for filename in file_name_list:
        apath = os.path.join(maindir, filename)
    for subdir in subdir:

        apath1 = os.path.join(subdir, filename)


