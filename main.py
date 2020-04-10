# To do:
# ------------------------------------------
# - filename comparison somewhat bugged
# - deal with songs in the playlist that is set to private or deleted or restricted from certain region
# .webm -> .mp3

from pytube import YouTube, Playlist
from pprint import pprint
import time
import sys
import os

def check_encoding():
	# Type chcp to check terminal's encoding
	# UTF8: 65001
	# Big5: 950
	print(sys.getdefaultencoding()) # utf-8
	# Change font to "Lucida Console"

def get_filenames(path='bucket/', file_extention='.webm'):
	filenames = []
	# r=root, d=directories, f = files
	for r, d, f in os.walk(path):
		for filename in f:
			if file_extention in filename:
				# print(os.path.join(r, filename)) # full path up to root
				filename = filename[:-len(file_extention)] # get rid of file extension
				# print(filename)
				filenames.append(filename)

	return filenames

def download_playlist(url, dest='bucket/', skip=0):
	filenames = get_filenames(path=dest)
	print('Total {} files in {}.'.format(len(filenames), dest))
	print()

	pl = Playlist(url)
	print('Playlist name: {}'.format(pl.title()))
	print()
	
	yts = []
	vid_names = []
	t0 = time.time()
	for idx, yt in enumerate(pl.videos):
		if idx < skip:
			continue
		yts.append(yt)
		vid_name = yt.title
		vid_names.append(vid_name)
		print('{}. {}'.format(idx+1, vid_name))

		if vid_name in filenames:
			print('Already in {}.'.format(dest))
		else:
			download_video(yt=yt)
		t1 = time.time()
		print("  Time elapsed: {:0.5f}s".format(t1 - t0))
		print()
		
		t0 = t1
	# pl.download_all()

def download_video(url=None, yt=None, dest='/bucket'):
	t0 = time.time()
	if yt is None:
		yt = YouTube(url)
	print('Video name: {}'.format(yt.title))
	# print('All streams:')
	# pprint(yt.streams.all())
	print('Best Audio: ')
	print('  {}'.format(yt.streams.filter(only_audio=True).order_by('abr')[-1])) # highest audio quality
	# print('MP4: ')
	# pprint(yt.streams.filter(subtype='mp4').all(), width=100)

	# yt.streams.first().download('bucket/') # download best quality
	try:
		yt.streams.filter(only_audio=True).order_by('abr')[-1].download('bucket/')
	except:
		print('Download failed.', end='')
	else:
		print('Download succeeded.', end='')
	finally:
		print(" Time elapsed: {:0.5f}s".format(time.time() - t0))

if __name__ == '__main__':
	t0 = time.time()
	dest = 'bucket/'
	# url = 'https://www.youtube.com/watch?v=z0bKSb5EmFo'
	# download_video(url)

	anisong_pl = 'https://www.youtube.com/watch?v=1TJSde-byyY&list=PLTcXkoIKuMHoxKhcvzRWmFqK_rEiYFhfE'
	download_playlist(anisong_pl, skip=0)
	filenames = get_filenames()
	print('Total {} files in {}.'.format(len(filenames), dest))
	# pprint(filenames)
	print("  Time elapsed: {:0.5f}s".format(time.time() - t0))