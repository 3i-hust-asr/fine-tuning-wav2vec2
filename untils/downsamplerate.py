import audioop
import os
import wave


def downsampleWav(src, dst, inrate=48000, outrate=16000, inchannels=2, outchannels=1):
    if not os.path.exists(src):
        print('Source not found!')
        return False

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    try:
        s_read = wave.open(src, 'r')
        s_write = wave.open(dst, 'w')
    except:
        print('Failed to open files!')
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)
    s_read.close()
    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)
    except:
        print('Failed to downsample wav')
        return False

    try:
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
    except:
        print('Failed to write wav')
        return False

    try:
        s_read.close()
        s_write.close()
    except:
        print('Failed to close wav files')
        return False

    return True

# root = '/home/phuc/Desktop/COE/data_STT_malay/data_1908'
# list_folder = os.listdir(root)
# for folder in list_folder:
#     path_folder = os.path.join(root, folder, 'wavs')
#     list_file_wav = os.listdir(path_folder)
#     for file_wav in list_file_wav:
#         path_file_wav = os.path.join(path_folder, file_wav)
#         if downsampleWav(path_file_wav, os.path.join('data', file_wav)):
#             pass
#         else:
#             print(path_file_wav)

