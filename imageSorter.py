import exifread
import shutil
import os

def sortPhotos():
    input_dir = './'

    for name in os.listdir(input_dir):
        if name.endswith('.jpg'):
            f = open(name, 'rb')
            tags = exifread.process_file(f)
            for tag in tags.keys():
                if tag in ('Image DateTime'):
                    checked_dir = str(tags[tag])[0:7]
                    if not os.path.exists(checked_dir):
                        os.mkdir(checked_dir)
                    if checked_dir in str(tags[tag]):
                        output_dir = './' + checked_dir + '/'
                        shutil.move((input_dir + name), (output_dir + name))


sortPhotos()
