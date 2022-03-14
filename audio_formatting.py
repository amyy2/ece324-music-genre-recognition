import os
from tabnanny import filename_only
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
import pylab
#from audioplayer import AudioPlayer

# ROCK

# load each mp3 file from directory
os.chdir('../ece324-music-genre-recognition/mp3_files/rock')

for filename in os.listdir(os.getcwd()):

    # split each song into four 30 second segments
    time = 30 * 1000 # seconds to milliseconds
    song = AudioSegment.from_file(filename, format='mp3')
    part_1 = song[0:time]
    part_2 = song[time:2*time]
    part_3 = song[2*time:3*time]
    part_4 = song[3*time:4*time]

    # temporarily save each segment to a directory
    os.chdir('../rock/split_mp3_files')
    part_1.export(filename+'part 1.mp3', format='mp3')
    part_2.export(filename+'part 2.mp3', format='mp3')
    part_3.export(filename+'part 3.mp3', format='mp3')
    part_4.export(filename+'part 4.mp3', format='mp3')

    for audio in os.listdir(os.getcwd()):

        # convert each mp3 file into a numpy array 
        y, sr = librosa.load(audio)
            
        os.chdir('../../../spectrograms/rock')

        # convert numpy array to mel spectrogram and save figure
        plt.figure()
        pylab.axis('off')
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
        plot = librosa.feature.melspectrogram(y=y, sr=sr)
        img = librosa.display.specshow(librosa.power_to_db(plot, ref=np.max), x_axis='time', y_axis='mel', sr=sr, fmax=8192)
        pylab.savefig(audio+'.jpg', bbox_inches=None, pad_inches=0)
        pylab.close()
    
        os.chdir('../../mp3_files/rock/split_mp3_files')
        # remove audio files from temporary directory
        os.remove(audio)
        
    os.chdir('..')

# HIP HOP

# load each mp3 file from directory
os.chdir('../ece324-music-genre-recognition/mp3_files/hip_hop')

for filename in os.listdir(os.getcwd()):

    # split each song into four 30 second segments
    time = 30 * 1000 # seconds to milliseconds
    song = AudioSegment.from_file(filename, format='mp3')
    part_1 = song[0:time]
    part_2 = song[time:2*time]
    part_3 = song[2*time:3*time]
    part_4 = song[3*time:4*time]

    # temporarily save each segment to a directory
    os.chdir('../hip_hop/split_mp3_files')
    part_1.export(filename+'part 1.mp3', format='mp3')
    part_2.export(filename+'part 2.mp3', format='mp3')
    part_3.export(filename+'part 3.mp3', format='mp3')
    part_4.export(filename+'part 4.mp3', format='mp3')

    for audio in os.listdir(os.getcwd()):

        # convert each mp3 file into a numpy array 
        y, sr = librosa.load(audio)
            
        os.chdir('../../../spectrograms/hip_hop')

        # convert numpy array to mel spectrogram and save figure
        plt.figure()
        pylab.axis('off')
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
        plot = librosa.feature.melspectrogram(y=y, sr=sr)
        img = librosa.display.specshow(librosa.power_to_db(plot, ref=np.max), x_axis='time', y_axis='mel', sr=sr, fmax=8192)
        pylab.savefig(audio+'.jpg', bbox_inches=None, pad_inches=0)
        pylab.close()
    
        os.chdir('../../mp3_files/hip_hop /split_mp3_files')
        # remove audio files from temporary directory
        os.remove(audio)
        
    os.chdir('..')

# JAZZ

# load each mp3 file from directory
os.chdir('../ece324-music-genre-recognition/mp3_files/jazz')

for filename in os.listdir(os.getcwd()):

    # split each song into four 30 second segments
    time = 30 * 1000 # seconds to milliseconds
    song = AudioSegment.from_file(filename, format='mp3')
    part_1 = song[0:time]
    part_2 = song[time:2*time]
    part_3 = song[2*time:3*time]
    part_4 = song[3*time:4*time]

    # temporarily save each segment to a directory
    os.chdir('../jazz/split_mp3_files')
    part_1.export(filename+'part 1.mp3', format='mp3')
    part_2.export(filename+'part 2.mp3', format='mp3')
    part_3.export(filename+'part 3.mp3', format='mp3')
    part_4.export(filename+'part 4.mp3', format='mp3')

    for audio in os.listdir(os.getcwd()):

        # convert each mp3 file into a numpy array 
        y, sr = librosa.load(audio)
            
        os.chdir('../../../spectrograms/jazz')

        # convert numpy array to mel spectrogram and save figure
        plt.figure()
        pylab.axis('off')
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
        plot = librosa.feature.melspectrogram(y=y, sr=sr)
        img = librosa.display.specshow(librosa.power_to_db(plot, ref=np.max), x_axis='time', y_axis='mel', sr=sr, fmax=8192)
        pylab.savefig(audio+'.jpg', bbox_inches=None, pad_inches=0)
        pylab.close()
    
        os.chdir('../../mp3_files/jazz/split_mp3_files')
        # remove audio files from temporary directory
        os.remove(audio)
        
    os.chdir('..')

# EDM

# load each mp3 file from directory
os.chdir('../ece324-music-genre-recognition/mp3_files/edm')

for filename in os.listdir(os.getcwd()):

    # split each song into four 30 second segments
    time = 30 * 1000 # seconds to milliseconds
    song = AudioSegment.from_file(filename, format='mp3')
    part_1 = song[0:time]
    part_2 = song[time:2*time]
    part_3 = song[2*time:3*time]
    part_4 = song[3*time:4*time]

    # temporarily save each segment to a directory
    os.chdir('../edm/split_mp3_files')
    part_1.export(filename+'part 1.mp3', format='mp3')
    part_2.export(filename+'part 2.mp3', format='mp3')
    part_3.export(filename+'part 3.mp3', format='mp3')
    part_4.export(filename+'part 4.mp3', format='mp3')

    for audio in os.listdir(os.getcwd()):

        # convert each mp3 file into a numpy array 
        y, sr = librosa.load(audio)
            
        os.chdir('../../../spectrograms/edm')

        # convert numpy array to mel spectrogram and save figure
        plt.figure()
        pylab.axis('off')
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
        plot = librosa.feature.melspectrogram(y=y, sr=sr)
        img = librosa.display.specshow(librosa.power_to_db(plot, ref=np.max), x_axis='time', y_axis='mel', sr=sr, fmax=8192)
        pylab.savefig(audio+'.jpg', bbox_inches=None, pad_inches=0)
        pylab.close()
    
        os.chdir('../../mp3_files/edm/split_mp3_files')
        # remove audio files from temporary directory
        os.remove(audio)
        
    os.chdir('..')

# COUNTRY

# load each mp3 file from directory
os.chdir('../ece324-music-genre-recognition/mp3_files/country')

for filename in os.listdir(os.getcwd()):

    # split each song into four 30 second segments
    time = 30 * 1000 # seconds to milliseconds
    song = AudioSegment.from_file(filename, format='mp3')
    part_1 = song[0:time]
    part_2 = song[time:2*time]
    part_3 = song[2*time:3*time]
    part_4 = song[3*time:4*time]

    # temporarily save each segment to a directory
    os.chdir('../country/split_mp3_files')
    part_1.export(filename+'part 1.mp3', format='mp3')
    part_2.export(filename+'part 2.mp3', format='mp3')
    part_3.export(filename+'part 3.mp3', format='mp3')
    part_4.export(filename+'part 4.mp3', format='mp3')

    for audio in os.listdir(os.getcwd()):

        # convert each mp3 file into a numpy array 
        y, sr = librosa.load(audio)
            
        os.chdir('../../../spectrograms/country')

        # convert numpy array to mel spectrogram and save figure
        plt.figure()
        pylab.axis('off')
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
        plot = librosa.feature.melspectrogram(y=y, sr=sr)
        img = librosa.display.specshow(librosa.power_to_db(plot, ref=np.max), x_axis='time', y_axis='mel', sr=sr, fmax=8192)
        pylab.savefig(audio+'.jpg', bbox_inches=None, pad_inches=0)
        pylab.close()
    
        os.chdir('../../mp3_files/country/split_mp3_files')
        # remove audio files from temporary directory
        os.remove(audio)
        
    os.chdir('..')

# CLASSICAL

# load each mp3 file from directory
os.chdir('../ece324-music-genre-recognition/mp3_files/classical')

for filename in os.listdir(os.getcwd()):

    # split each song into four 30 second segments
    time = 30 * 1000 # seconds to milliseconds
    song = AudioSegment.from_file(filename, format='mp3')
    part_1 = song[0:time]
    part_2 = song[time:2*time]
    part_3 = song[2*time:3*time]
    part_4 = song[3*time:4*time]

    # temporarily save each segment to a directory
    os.chdir('../classical/split_mp3_files')
    part_1.export(filename+'part 1.mp3', format='mp3')
    part_2.export(filename+'part 2.mp3', format='mp3')
    part_3.export(filename+'part 3.mp3', format='mp3')
    part_4.export(filename+'part 4.mp3', format='mp3')

    for audio in os.listdir(os.getcwd()):

        # convert each mp3 file into a numpy array 
        y, sr = librosa.load(audio)
            
        os.chdir('../../../spectrograms/classical')

        # convert numpy array to mel spectrogram and save figure
        plt.figure()
        pylab.axis('off')
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
        plot = librosa.feature.melspectrogram(y=y, sr=sr)
        img = librosa.display.specshow(librosa.power_to_db(plot, ref=np.max), x_axis='time', y_axis='mel', sr=sr, fmax=8192)
        pylab.savefig(audio+'.jpg', bbox_inches=None, pad_inches=0)
        pylab.close()
    
        os.chdir('../../mp3_files/classical/split_mp3_files')
        # remove audio files from temporary directory
        os.remove(audio)
        
    os.chdir('..')

# POP

# load each mp3 file from directory
os.chdir('../ece324-music-genre-recognition/mp3_files/pop')

for filename in os.listdir(os.getcwd()):

    # split each song into four 30 second segments
    time = 30 * 1000 # seconds to milliseconds
    song = AudioSegment.from_file(filename, format='mp3')
    part_1 = song[0:time]
    part_2 = song[time:2*time]
    part_3 = song[2*time:3*time]
    part_4 = song[3*time:4*time]

    # temporarily save each segment to a directory
    os.chdir('../pop/split_mp3_files')
    part_1.export(filename+'part 1.mp3', format='mp3')
    part_2.export(filename+'part 2.mp3', format='mp3')
    part_3.export(filename+'part 3.mp3', format='mp3')
    part_4.export(filename+'part 4.mp3', format='mp3')

    for audio in os.listdir(os.getcwd()):

        # convert each mp3 file into a numpy array 
        y, sr = librosa.load(audio)
            
        os.chdir('../../../spectrograms/pop')

        # convert numpy array to mel spectrogram and save figure
        plt.figure()
        pylab.axis('off')
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
        plot = librosa.feature.melspectrogram(y=y, sr=sr)
        img = librosa.display.specshow(librosa.power_to_db(plot, ref=np.max), x_axis='time', y_axis='mel', sr=sr, fmax=8192)
        pylab.savefig(audio+'.jpg', bbox_inches=None, pad_inches=0)
        pylab.close()
    
        os.chdir('../../mp3_files/pop/split_mp3_files')
        # remove audio files from temporary directory
        os.remove(audio)
        
    os.chdir('..')