from pydub import AudioSegment
from main import get_filenames
from pprint import pprint
import gc

def webm_convert_mp3(songname):
	webm_audio = AudioSegment.from_file('bucket/{}.webm'.format(songname), format='webm')
	# raw_audio = AudioSegment.from_file("audio.wav", format="raw",
	#                                    frame_rate=44100, channels=2, sample_width=2)
	webm_audio.export('mp3/{}.mp3'.format(songname), format='mp3')
	del webm_audio
	gc.collect()
	print('{}.mps'.format(songname))

if __name__ == '__main__':
	filenames = get_filenames()
	for idx, songname in enumerate(filenames):
		print('({}/{}) '.format(idx+1, len(filenames)), end='')
		webm_convert_mp3(songname)