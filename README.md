# ece324-music-genre-recognition
ECE324 course project

The python file [audio_formatting.py](audio_formatting.py) contains the code used to convert the downloaded MP3 files to mel spectrograms.

The folder [spectrograms](spectrograms) contains a subfolder for each genre where the generated mel spectrograms are saved.

The python file [cnn_model.py](cnn_model.py) contains the code used by the initial convolutional neural network model we created.

The dataset .zip file is larger than 1GB, and as a result cannot be uploaded to github. It can however be downloaded at the following link: https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification/activity. It contains the data and audio files used to train the neural network.

*IMPORTANT NOTE:* In the cnn_model file, there is a line for extracting the necessary data from a google drive. In the event that this code does not run properly, it may be necessary to upload the unzipped file into a google drive and change the following two lines to suit the new file path: 

df = pd.read_csv("drive/My Drive/U of T/Year 3/ECE324/Data/features_3_sec.csv")

audio_recording="drive/My Drive/U of T/Year 3/ECE324/Data/genres_original/hiphop/hiphop.00001.wav"

It may also be possible to load the data directly into an active colab session (should that be used), but upon testing there were problems with this approach. If the .py file is loaded directly into a python editor (for instance PyCharm), then the two lines above will _certainly_ need to be changed to accomodate the path.
