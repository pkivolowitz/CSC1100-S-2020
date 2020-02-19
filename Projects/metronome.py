import time
from playsound import playsound

'''	On the Mac:
	pip3 install playsound PyObjC
	On Windows:
	pip install playsound
'''

beats_per_minute = int(input('Enter desired beats per minute: '))
minimum_beats_per_minute = 60
maximum_beats_per_minute = 600

if beats_per_minute < minimum_beats_per_minute:
	print(minimum_beats_per_minute, 'BPM is the minimum allowable input')
	exit()
if beats_per_minute > 600:
	print(maximum_beats_per_minute, 'BPM is the maximum allowable input')
	exit()

accent_beat = int(input('Accent every how many beats (0 disables): '))

print('Control-c to exit...')

#	Convert BPM to sleep time

beat_interval = 60.0 / beats_per_minute
beat_counter = 0

while True:
	if accent_beat > 0 and beat_counter % accent_beat == 0:
		playsound('m1.wav', block=False)
		print('tick')
	else:
		playsound('m2.wav', block=False)
		print('tock')
	beat_counter += 1
	time.sleep(beat_interval)
