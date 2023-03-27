# chatgptによるavgimg_creation.pyの改良版
from PIL import Image
import os
import sys
import numpy as np
import argparse
import multiprocessing as mp

def parse_args():
    parser = argparse.ArgumentParser(description='Compute the average of TIFF images in a directory.')
    parser.add_argument('input_dir', help='The directory containing input TIFF images')
    parser.add_argument('--output_dir', '-o', default='avg', help='The directory to save the output average image')
    parser.add_argument('--output_format', '-f', default='tiff', help='The format of the output average image (default: tiff)')
    parser.add_argument('--num_processes', '-p', type=int, default=4, help='The number of processes to use for computation (default: 4)')
    return parser.parse_args()

def compute_mean_image(args):
    file = args[0]
    input_dir = args[1]
    img = Image.open(os.path.join(input_dir, file))
    img_array = np.array(img)
    return img_array / len(os.listdir(input_dir))

def main():
    args = parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir
    output_format = args.output_format
    num_processes = args.num_processes

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get list of TIFF files in input directory
    filenames = [f for f in os.listdir(input_dir) if f.endswith('.tif')]
    filenames.sort()

    # Split list of TIFF files into chunks for multiprocessing
    chunks = [filenames[i:i+num_processes] for i in range(0, len(filenames), num_processes)]

    # Create multiprocessing pool
    pool = mp.Pool(processes=num_processes)

    # Compute mean image for each chunk in parallel
    results = pool.map(compute_mean_image, [(file, input_dir) for file in filenames])

    # Combine results into single mean image
    avg_img_arr = np.sum(results, axis=0)
    avg_img = Image.fromarray(avg_img_arr.astype(np.uint16))

    # Save mean image
    output_path = os.path.join(output_dir, f'{os.path.basename(input_dir)}_avg.{output_format}')
    avg_img.save(output_path)
    print(f'Mean image saved to {output_path}')

if __name__ == '__main__':
    main()
