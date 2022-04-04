import os
from tabnanny import filename_only
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
import pylab

# load each mp3 file from directory
os.chdir('../ece324-music-genre-recognition/mp3_files/rnb')

for i in range(1, len(os.listdir(os.getcwd()))):

    print(i, os.listdir(os.getcwd())[i])
    filename = os.listdir(os.getcwd())[i]

    # split each song into two 60 second segments
    time = 60 * 1000 # seconds to milliseconds
    song = AudioSegment.from_file(os.listdir(os.getcwd())[i], format='mp3')
    part_1 = song[0:time]
    part_2 = song[time:2*time]

    # temporarily save each segment to a directory
    os.chdir('../rnb/split_mp3_files')
    part_1.export(filename+'part 1.mp3', format='mp3')
    part_2.export(filename+'part 2.mp3', format='mp3')

    for audio in os.listdir(os.getcwd()):

        # convert each mp3 file into a numpy array 
        y, sr = librosa.load(audio)
            
        os.chdir('../../../spectrograms/rnb')

        # convert numpy array to mel spectrogram and save figure
        plt.figure()
        pylab.axis('off')
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
        plot = librosa.feature.melspectrogram(y=y, sr=sr)
        img = librosa.display.specshow(librosa.power_to_db(plot, ref=np.max), x_axis='time', y_axis='mel', sr=sr, fmax=8192)
        pylab.savefig(audio+'.jpg', bbox_inches=None, pad_inches=0)
        pylab.close()
    
        os.chdir('../../mp3_files/rnb/split_mp3_files')
        # remove audio files from temporary directory
        os.remove(audio)
        
    os.chdir('..')
    os.remove(filename)