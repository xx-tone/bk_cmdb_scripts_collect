import os
import re
import zipfile


DST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts')
Zips_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zipfiles')


def get_dst_dir(x):
    """
    下载的文件路径下以 <name>-uuid.zip 去除后面的内容
    :param x:
    :return:
    """
    matchd = re.match('(.*?)-[0-9a-z]+\.zip', x)
    y = matchd.group(1) if matchd else x
    dst_dir = os.path.join(DST_DIR, y)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    return dst_dir


def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip file! >> ' + zip_src)


def zip_files(_dir=Zips_DIR):
    for x in os.listdir(_dir):
        zip_src = os.path.join(_dir, x)
        unzip_file(zip_src, get_dst_dir(x))


if __name__ == "__main__":
    zip_files()
