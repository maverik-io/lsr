#! /usr/local/bin/python3
import os

dirs = os.listdir(".")

icons = {
    ('md',)                         : "  ",
    ('ai',)                         : "  ",
    ('png', 'jpeg', 'jpg', 'tiff')  : "  ",
    ('py', 'pyc')                   : "  ",
    ('psd',)                        : "  ",
    ('svg',)                        : "  ",
    ('ttf', 'otf')                  : "  ",
    }

print('-='*int(os.get_terminal_size()[0]/2))


def recursive(dirs, path='.', spaces=0):
    for item in dirs:
        if item[0] == '.':
            continue
        if os.path.isdir(path+'/'+item):
            print(spaces*" ▏"+"   "+item)
            recursive(os.listdir(path+'/'+item), path+'/'+item, spaces+1)

        else:
            extension = item.split('.')[-1]
            icon = '  '
            for ext in icons:
                if extension in ext:
                    icon = icons[ext]
            print(spaces*' ▏'+f"  {icon}"+item)

recursive(dirs)
print('-='*int(os.get_terminal_size()[0]/2))
