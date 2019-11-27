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
                    # checked_dir_year = str(tags[tag])[0:4]                                    for windows uncomment this
                    # checked_dir_month = str(tags[tag])[5:7]                                   for windows uncomment this
                    # checked_dir_no_semicolor = checked_dir_year + '-' + checked_dir_month     for windows uncomment this
                    checked_dir = str(tags[tag])[0:7]
                    # if not os.path.exists(checked_dir_no_semicolor):                          for windows uncomment this
                    #     os.mkdir(checked_dir_no_semicolor)                                    for windows uncomment this
                    if not os.path.exists(checked_dir):                                         # for windows comment this
                        os.mkdir(checked_dir)                                                   # for windows comment this
                    if checked_dir in str(tags[tag]):
                        # output_dir = './' + checked_dir_no_semicolor + '/'                    for windows uncomment this
                        # f.close()                                                             for windows uncomment this
                        output_dir = './' + checked_dir + '/'                                   # for windows comment this
                        shutil.move((input_dir + name), (output_dir + name))


sortPhotos()
