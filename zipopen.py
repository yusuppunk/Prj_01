# -*- coding:utf-8 -*-
import gzip
import os
import tarfile
import zipfile
import rarfile
import optparse

'''
gz： 即gzip，通常只能压缩一个文件。与tar结合起来就可以实现先打包，再压缩。
tar： linux系统下的打包工具，只打包，不压缩
tgz：即tar.gz。先用tar打包，然后再用gz压缩得到的文件
zip： 不同于gzip，虽然使用相似的算法，可以打包压缩多个文件，不过分别压缩文件，压缩率低于tar。
rar：打包压缩文件，最初用于DOS，基于window操作系统。压缩率比zip高，但速度慢，随机访问的速度也慢
'''

def un_gz(file_name,NewName=None):
    '''
    gz文件一般只压缩一个文件

    解压.gz文件
    :param filename:要解压的文件
    :return:
    '''
    g_file = gzip.GzipFile(file_name)               #创建一个gz对象
    if NewName == None:
        f_name = file_name.replace(".gz", "")  # 这个是解压后的文件名，去掉.gz就可以
        open(f_name,'w+').write(g_file.read())          #把提取出来的文件保存下来
    else:
        open(NewName, 'w+').write(g_file.read())  # 把提取出来的文件保存下来
    g_file.close()
    print("[*] Done!")
def un_tar(file_name,NewName=None):
    '''
    abc.tar.gz解压出来是abc.tar，所以还要解压一次
    *：tgz与tar.gz是同行一个格式，老版本DOS扩展最多支持三个字符，故用tgz表示
    然后，tar里面有多个文件，先读取所有文件名，再解压
    :param file_name:压缩包的名字
    :return:
    '''
    tar = tarfile.open(file_name)
    names = tar.getnames()
    if NewName == None:
        if os.path.isdir(file_name + "_files"):
            pass
        else:
            os.mkdir(file_name + "_files/")
        #由于解压出来是好多文件，先建立一个同名文件夹，再把出来的东西都放进去
        for name in names:
            tar.extract(name,file_name + "_files/")
    else:
        if os.path.isdir(NewName):
            pass
        else:
            os.mkdir(NewName)
        #由于解压出来是好多文件，先建立一个同名文件夹，再把出来的东西都放进去
        for name in names:
            tar.extract(name,NewName)
    tar.close()
    print("[*] Done!")
def un_zip(file_name,NewName=None):
    '''
    与tar相似，先读取压缩包里的名字，没名字特么不能解压
    :param file_name: 如果看不懂这个东西你还是关掉这个文件吧
    :return:
    '''
    zip_file = zipfile.ZipFile(file_name)
    if NewName == None:
        if os.path.isdir(file_name + '_files'):
            pass
        else:
            os.mkdir(file_name + '_files')
        for names in zip_file.namelist():
            zip_file.extract(names,file_name + '_files/')
    else:
        if os.path.isdir(NewName):
            pass
        else:
            os.mkdir(NewName)
        for names in zip_file.namelist():
            zip_file.extract(names,NewName)
    zip_file.close()
    print("[*] Done!")
def un_rar(file_name,NewName=None):
    rar = rarfile.RarFile(file_name)
    #rar = rarfile(fil_name)
    if NewName == None:
        if os.path.isdir(file_name + '_files'):
            pass
        else:
            os.mkdir(file_name + '_fiels')
        os.chdir(file_name + '_files')
        rar.extractall()
    else:
        if os.path.isdir(NewName):
            pass
        else:
            os.mkdir(NewName)
        os.chdir(NewName)
        rar.extractall()
    rar.close()
    print("[*] Done!")

def main():
    parser = optparse.OptionParser('usage %prog:\n\t-t\t<file type>\n\t-n\t<file name>\n\t-N\t<new file name>\nExcample:python zipopen.py -t zip -n abc.zip')
    parser.add_option('-t',dest='type',type='string',help='target file type:    gz/tar/zip/rar')
    parser.add_option('-n', dest='name', type='string', help='target file name:    abc.tar.gz')
    parser.add_option('-N',dest='NewName',type='string',help='the name of new file or directory')
    (options,args) = parser.parse_args()
    type = options.type
    name = options.name
    NewName = options.NewName
    if (type == None) or (name == None):
        print(parser.usage)
        exit(0)
    if type == 'gz':
        if NewName == None:
            un_gz(name)
        else:
            un_gz(name, NewName=NewName)
    elif type == 'tar':
        if NewName == None:
            un_tar(name)
        else:
            un_tar(name, NewName=NewName)
    elif type == 'zip':
        if NewName == None:
            un_zip(name)
        else:
            un_zip(name, NewName=NewName)
    elif type == 'rar':
        if NewName == None:
            un_rar(name)
        else:
            un_rar(name, NewName=NewName)


if __name__=='__main__':
    main()