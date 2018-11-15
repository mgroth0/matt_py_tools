import tarfile
import os

source_dir = '/Users/matt/Desktop/registered/todo/matt_py_tools'

output_filename = 'matt_py_tools.tar.gz'


def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

print('here1')
if __name__ == '__main__':
    print('here2')
    make_tarfile(output_filename, source_dir)