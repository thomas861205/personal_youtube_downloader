from pytube import YouTube, Playlist
from pprint import pprint
import time
import sys

def check_encoding():
	# Type chcp to check terminal's encoding
	# UTF8: 65001
	# Big5: 950
	print(sys.getdefaultencoding()) # utf-8
	# Change font to "Lucida Console"

def download_playlist(url, dest='bucket/'):
	pl = Playlist(url)
	print('Playlist name: {}'.format(pl.title()))
	yts = list(pl.videos)
	vid_names = [yt.title for yt in yts]
	pprint(vid_names, width=100) # convert generator to list, list of Youtube object
	# pl.download_all()

def download_video(url, yt=None, dest='/bucket'):
	if yt is None:
		yt = YouTube(url)
	print('Video name: {}'.format(yt.title))
	# print('All streams:')
	# pprint(yt.streams.all())
	print('Audio only: ')
	pprint(yt.streams.filter(only_audio=True).order_by('abr')[-1], width=100) # highest audio quality
	# print('MP4: ')
	# pprint(yt.streams.filter(subtype='mp4').all(), width=100)

	# yt.streams.first().download('bucket/') # download best quality
	yt.streams.filter(only_audio=True).order_by('abr')[-1].download('bucket/')

if __name__ == '__main__':
	t0 = time.time()
	url = 'https://www.youtube.com/watch?v=z0bKSb5EmFo'
	download_video(url)

	# anisong_pl = 'https://www.youtube.com/watch?v=1TJSde-byyY&list=PLTcXkoIKuMHoxKhcvzRWmFqK_rEiYFhfE'
	# stanford_cs330 = 'https://www.youtube.com/watch?v=0rZtSwNOTQo&list=PLoROMvodv4rMC6zfYmnD7UG3LVvwaITY5'
	# download_playlist(stanford_cs330)
	elapsed = time.time() - t0
	print("Time elapsed: {:0.5f}s".format(elapsed))
