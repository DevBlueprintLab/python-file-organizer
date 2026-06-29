from pathlib import Path 
import os, shutil
print('================\n FILE ORGANAIZER\n================')
folder_path = Path.home() / 'Downloads'
foldernames = ('Images', 'Videos', 'PDFs', 'Documents','Others')
images = ('.png', '.jpeg', '.gif', '.svg', '.jpg', '.avif', '.webp')
videos = ('.mov', '.mp4', '.avi', '.wmv', '.flv', '.webm', '.avchd')
pdfs = ('.pdf', '.adobe')
documents = ('.docx', '.doc', '.dot', '.docm', '.zip', '.txt' )
others = []
images_moved = 0
videos_moved = 0
pdfs_moved = 0
documents_moved = 0
others_moved = 0
total = 0
for foldername in foldernames:
    (folder_path/foldername).mkdir(parents= True, exist_ok = True)
for foldername, subfolders, filenames in os.walk(folder_path):
    skip = False
    for f in foldernames:
        if str(foldername).endswith(f):
            skip = True
            break
    if skip:
        continue
    for filename in filenames:
        source = Path(foldername) / filename
        if filename.lower().endswith(images):
            destination = folder_path /'Images'/filename
            if destination.exists():
                print(f'File {filename} already exists in {destination.parent.name}')
                continue
            print(f'moving image: {filename}')
            shutil.move(source, destination)
            print(f'✓ Moved:\n {filename} -> Images')
            images_moved += 1
            total += 1
        elif filename.lower().endswith(videos):
            destination = folder_path /'Videos'/filename
            if destination.exists():
                print(f'File {filename} already exists in {destination.parent.name}')
                continue
            print(f'moving video: {filename}')
            shutil.move(source, destination)
            print(f'✓ Moved:\n {filename} -> Videos')
            videos_moved += 1
            total += 1
        elif filename.lower().endswith(pdfs):
            destination = folder_path /'PDFs'/filename
            if destination.exists():
                print(f'File {filename} already exists in {destination.parent.name}')
                continue
            print(f'moving pdf: {filename}')
            shutil.move(source, destination)
            print(f'✓ Moved:\n {filename} -> PDFs')
            pdfs_moved += 1
            total += 1
        elif filename.lower().endswith(documents):
            destination = folder_path /'Documents'/filename
            if destination.exists():
                print(f'File {filename} already exists in {destination.parent.name}')
                continue
            print(f'✓ moving document: {filename}')
            shutil.move(source, destination)
            print(f'Moved:\n {filename} -> Documents')
            documents_moved += 1
            total += 1
        else:
            destination = folder_path /'Others'/filename
            if destination.exists():
                print(f'File {filename} already exists in {destination.parent.name}')
                continue
            print(f'moving file: {filename}')
            shutil.move(source, destination)
            print(f'✓ Moved:\n {filename} -> Others')
            others_moved += 1
            total += 1
            other = source.suffix
            others.append(other)
print('Finished!')
print(f'Images moved: {images_moved}')
print(f'Videos moved: {videos_moved}')
print(f'PDFs moved: {pdfs_moved}')
print(f'Documents moved: {documents_moved}')
print(f'Other files moved: {others_moved}')
print(f'Unknown file types found: {set(others)}')
print(f'Total: {total}')