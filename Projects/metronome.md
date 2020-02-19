# Metronome

If you haven't already:

On the Mac:

```text
pip3 install playsound PyObjC
```

On Windows:

```text
pip install playsound
```

## New libraries

```python
import time
from playsound import playsound
```

### Delaying

You can call `time.sleep()` passing it the number of seconds to delay. You can specify fractions like `0.01` to sleep 100th of a second. Accuracy is usually withinfrom playsound import playsound
 10 to 20 milliseconds.

### Playing a sound

You can use the `playsound` module to simply play one sound file.

To play a sound all the way through before continuing:

```python
playsound("path to file name as a string")
```

To launch a sound but keep right on going:

```python
playsound("path to file name as a string", block=False)
```

## User input

```python
beats_per_minute = int(input('Enter desired beats per minute: '))
accent_beat = int(input('Accent every how many beats (0 disables): '))
```

## Operation

### Figuring out delay from BPM

120 BPM would play a sound twice per second (0.5 seconds between sounds).

From this: 

```python
delay_time = 60.0 / beats_per_minute
```

## Sample output

Imagine the sounds:

```text
Projects $> python3 metronome.py
Enter desired beats per minute: 120
Accent every how many beats (0 disables): 4
Control-c to exit...
tick
tock
tock
tock
tick
tock
tock
tock
tick
^CTraceback (most recent call last):
  File "metronome.py", line 38, in <module>
    time.sleep(beat_interval)
KeyboardInterrupt
Projects $>
```


## This program might not work from the debugger

I'll show you how to run the program directly.

