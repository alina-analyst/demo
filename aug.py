from PIL import Image
import os

os.chdir('/Users/alinazaripova/Downloads/black_isolators/')  # поменяем директорию на ту, где у нас расположены картинки


for fname in os.listdir(os.getcwd()):  # os.listdir - соответственно, есть ли что-нибудь, у нас, в папке,
 try:
    Image.open(fname).save(os.path.splitext(fname)[0] + '.jpg')  # а os.getcwd() - папка, в которую мы однажды перешли
    print('Converted {0} to {1}.jpg'.format(fname, os.path.splitext(fname)[0]))
 except (Exception):
        print('Sorry, we have no pictures.')