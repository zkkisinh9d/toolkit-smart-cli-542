import os, sys

prefix = sys.argv[1] if len(sys.argv) > 1 else 'file'
for i, f in enumerate(sorted(os.listdir('.'))):
    if os.path.isfile(f) and not f.startswith('.'):
        os.rename(f, f'{prefix}_{i:03d}{os.path.splitext(f)[1]}')
