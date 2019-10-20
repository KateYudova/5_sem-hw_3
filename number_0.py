"""
addition for three programs
"""
import os
import librosa
import numpy
def get(pathn):
    """
    Get MFCC and create file with it. The same location in dir result
    """
    sig, sr = librosa.load(pathn)
    res = numpy.empty(0)
    res = librosa.feature.mfcc(sig, sr)
    n = pathn.find('test/')
    pathn = pathn[:n] + 'result' + pathn[(n+4):]
    dirs = pathn[:pathn.rfind('/')]
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    numpy.save(pathn[:-4], res)

def srch(curr, ls):
    """
    Searching all files which have format like .wav
    """
    for i in os.listdir(curr):
        path = os.path.join(curr, i)
        if os.path.isdir(path):
            srch(path, ls)
        elif "wav" in i [-3:]:
            ls.append(path)
