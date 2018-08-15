# Voice_Activity_Detection
This is an implement of voice activity detction based on google webrtc. 
A `VAD <https://en.wikipedia.org/wiki/Voice_activity_detection>`_
classifies a piece of audio data as being voiced or unvoiced. It can
be useful for telephony and speech recognition.

The VAD that Google developed for the `WebRTC <https://webrtc.org/>`_
project is reportedly one of the best available, being fast, modern
and free.

# How to use it
## step1
install all required packages by `pip install -r requirements.txt`
check if there is c++ library surport on your PC.

## step2
put your raw audio file into the webrtcvad folder. Run vad with `python vad.py <aggressive level(0/1/2/3)> <frame length(10/20/30)> <padding duration(100-5000 recommended, depends on your purpose)> <filepath>`

# Things to know
1. multichnnel audio accepted.

2. sample rate of 8000Hz,16000Hz, 32000Hz are accepted. If your sample rate is not among those 3, please resample your file by using `resample.py`

3. `.pcm` and `.wav` are accepted. If not, please transfer format before doing vad.

4. Wisely choose your own aggressive level, frame duration and padding duration. They affect final result hugely.

5. A one sec mute is to be attached at the beginning and the end of each chunk file. For another length, please adapt the parameter in `def(padding)` in `vad.py`

# Example
![image](https://github.com/guozhonghao1994/Voice_Activity_Detection/blob/master/example.png)
`king_32000.wav` is a 2-channels, 32000Hz sample rate audio file. Run vad by `python vad.py 0 30 500 king_32000.wav`.
We can see 10 parts are seperated out from original file. For those noise parts mistakenly recognized as "voiced", we can either manually throw them away or write another code to filt them out. 


