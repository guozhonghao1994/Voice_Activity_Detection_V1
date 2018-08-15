import numpy as np
import wave
import pyaudio


def Resample(input_signal,src_fs,tar_fs):
    dtype = input_signal.dtype
    audio_len = len(input_signal)
    audio_time_max = 1.0*(audio_len-1) / src_fs
    src_time = 1.0 * np.linspace(0,audio_len,audio_len) / src_fs
    tar_time = 1.0 * np.linspace(0,np.int(audio_time_max*tar_fs),np.int(audio_time_max*tar_fs)) / tar_fs
    output_signal = np.interp(tar_time,src_time,input_signal).astype(dtype)

    return output_signal


def write_wav(path, audio, tar_fs, src_channels):
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(src_channels)
        wf.setsampwidth(2)
        wf.setframerate(tar_fs)
        wf.writeframes(audio)


if __name__ == '__main__':
    # Input filename here:
    wave_file = 'king.wav'
    audio_file = wave.open(wave_file, 'rb')
    audio_data = audio_file.readframes(audio_file.getnframes())
    audio_data_short = np.fromstring(audio_data, np.short)
    src_fs = audio_file.getframerate()
    src_chanels = audio_file.getnchannels()

    #if src_chanels > 1:
        #audio_data_short = audio_data_short[::src_chanels]
    print('input sample rate: %d' %src_fs)
    sample_rate = [8000,16000,32000]
    for i in reversed(sample_rate):
        if i < src_fs:
            tar_fs = i
            break
    print('output sample rate: %d' %tar_fs)

    audio_data_resample = Resample(audio_data_short,src_fs,tar_fs)
    write_wav(path='./{}_{}.wav'.format(wave_file[:-4],tar_fs),audio=audio_data_resample,tar_fs=tar_fs,src_channels=src_chanels)
    print('resample done!')