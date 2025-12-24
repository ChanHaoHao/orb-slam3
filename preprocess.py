import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file_root', type=str, required=True, help='Root directory containing rgb and depth folders')
args = parser.parse_args()
file_root = args.file_root

rgb_files = os.listdir(f"{file_root}/rgb")
rgb_files.sort()
depth_files = os.listdir(f"{file_root}/depth")
depth_files.sort()

print(len(rgb_files), len(depth_files))
n = min(len(rgb_files), len(depth_files))

with open(f"{file_root}/association.txt", 'w') as output_file:
    for i in range(n):
        output_file.write(f"{rgb_files[i][:-4]} rgb/{rgb_files[i]} {depth_files[i][:-4]} depth/{depth_files[i]}\n")