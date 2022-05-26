# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:26:15 2022

@author: Ale
"""

import argparse
from moviepy.editor import VideoFileClip

# Split Videoclip

parser = argparse.ArgumentParser(description='Split Videoclip in parts')
parser.add_argument('-i', '--img_path',
                    help='Please specify path for image', required=True)
parser.add_argument(
    '-p', '--parts', help='Please specify number of parts to divide', required=True)
opt = parser.parse_args()
pathIn = opt.img_path
parts = int(opt.parts)


def main(pathIn, parts):
    video = VideoFileClip(pathIn)
    duration = video.duration
    fps = video.fps
    duration_part = duration / parts
    for i in range(parts):
        start = i * duration_part
        end = (i+1) * duration_part
        part = video.subclip(start, end)
        part.to_videofile('output/part_'+str(i)+".mp4", fps, remove_temp=True)
    print('Video splitted succesfully.')

if __name__ == '__main__':
    main(pathIn, parts)
