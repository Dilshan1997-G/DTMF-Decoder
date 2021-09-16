import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


# read the audio samples

sample_rate_1 ,signal_1  = wavfile.read("tone01.wav")
sample_rate_2 ,signal_2  = wavfile.read("tone02.wav")
sample_rate_3 ,signal_3  = wavfile.read("tone03.wav")

sampling_time_1 = 1/sample_rate_1
no_data_1 = signal_1.shape[0]
tmax_1 = sampling_time_1 * (no_data_1-1)

sampling_time_2 = 1/sample_rate_2
no_data_2 = signal_2.shape[0]
tmax_2 = sampling_time_2 * (no_data_2-1)

sampling_time_3 = 1/sample_rate_3
no_data_3 = signal_2.shape[0]
tmax_3 = sampling_time_3*(no_data_3-1)

#---------------------------------------------------------------------------------------------

# creating time Axix
time_1 = np.arange(0,tmax_1+sampling_time_1,sampling_time_1)
time_2 = np.arange(0,tmax_2+sampling_time_2,sampling_time_2)
time_3 = np.arange(0,tmax_3+sampling_time_3,sampling_time_3)

plt.subplot(1,3,1)
plt.plot(time_1,signal_1)
plt.title(" tone 1")
plt.grid()
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

plt.subplot(1,3,2)
plt.plot(time_2,signal_2)
plt.title(" tone 2")
plt.grid()
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

plt.subplot(1,3,3)
plt.plot(time_3,signal_3)
plt.title(" tone 3")
plt.grid()
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()

#-------------------------------------------------------------------------------------

# play the sound 
sd.play(signal_1,sample_rate_1)
sd.play(signal_2,sample_rate_2)
sd.play(signal_3,sample_rate_3)

#-------------------------------------------------------------------------------------
# drawing the spectrogram for get the relation between time and frequency

Pxx_1,freqs_1,bins_1,im_1 = plt.specgram(signal_1,Fs=sample_rate_1)
plt.colorbar()
plt.title("Spectrum 1 for tone 01: Time(s) vs Frequency")
plt.xlabel("Time(s)")
plt.ylabel("Frewuency(Hz)")
plt.show()

Pxx_2,freqs_2,bins_2,im_2 = plt.specgram(signal_2,Fs=sample_rate_2)
plt.colorbar()
plt.title("Spectrum 2 for tone 02: Time(s) vs Frequency")
plt.xlabel("Time(s)")
plt.ylabel("Frewuency(Hz)")
plt.show()

Pxx_3,freqs_3,bins_3,im_3 = plt.specgram(signal_3,Fs=sample_rate_3)
plt.colorbar()
plt.title("Spectrum 3 for tone 03: Time(s) vs Frequency")
plt.xlabel("Time(s)")
plt.ylabel("Frewuency(Hz)")
plt.show()


"""

----tone01 Frequencies accordig to the spectrogram-----

no 1 = 950, 1350 --> 0
no 2 = 850, 1225 --> 7
no 3 = 700, 1225 --> 1
no 4 = 700, 1475 --> 3
no 5 = 775, 1350 --> 5
no 6 = 865, 1480 --> 9
no 7 = 775, 1350 --> 5
no 8 = 950, 1350 --> 0
no 9 = 775, 1225 --> 4
no 10 = 780,1480 --> 6

Tell Number = 0713595046





----tone02 Frequencies accordig to the spectrogram-----

no 1 = 950,1350 --> 0
no 2 =  700,1225--> 1
no 3 =  725,1200--> 1
no 4 =  725,1350--> 2
no 5 =  1350,850--> 8
no 6 =  775,1475--> 6
no 7 =  775,1225--> 4
no 8 =  775,1350--> 5
no 9 =  875,1225--> 7
no 10 = 875,1475--> 9

Tell Number =0112864579




-----tone03 Frequencies accordig to the spectrogram-----

no 1 = 950,1350 --> 0
no 2 = 850,1225 --> 7
no 3 = 700,1225 --> 1
no 4 = 850,1250 --> 8
no 5 = 700,1475 --> 3
no 6 = 700,1225 --> 1
no 7 = 700,1475 --> 3
no 8 = 775,1225 --> 3
no 9 = 775,1225 --> 4
no 10 = 700, 1475--> 3

Tell Number = 071359504





* values were noted from no 1 to no 10, by just looking at the yellow line values in each seperation
* then rounded the nopted values to DTMF values
* then noted the coresponding numbers
* finally write the Tell  Number

"""









