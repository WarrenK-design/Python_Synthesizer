### House Keeping ###
# Name           - Warren Kavanagh 
# Student Number - C16463344
# Email          - C16463344@MyTUDublin.ie

## Description ##
#   This file shows how the Sythesizer class created for this project can be used to perform 
#   subtractive sythesis by extracting cymbal audio from one wav file and bass audio from another wave file 
#   with each wav file consisting of multiple instruments. 
#   The extracted invidual instrument audios are then used in additive sythesis to create a new signal which 
#   is the combination of both signals 

### Imports ###
# Sythesiser - A class developed for this project which acts as a python implmentation of a sythesiser 
from Lib.Synthesizer import Sythesiser

if __name__ == '__main__':
    # Get an instance of the Sythesiser
    synth = Sythesiser()
    # showPlots - Boolean set this true if you want plots to be shown as script is run 
    showPlots = True

    ### Signal One (Subtractive Sythesis) - Get the cymbals from this signal by using filters ###
    # NOTE:
    #   This section of code uses the Sythesiser class to perform subtractive sythesis 
    #   It is taking an audio file which contains drums, bass and cymbols and subtracting the 
    #   frequency components which relate to the drums and bass to just retain the symbols
    #   The orginal audio can be listened to in the file /audio/subtractive/input/Audio_One.wav
    # ** Step 1 - Read in the wav file which contains the audio we will subtract away from 
    wavSignalOne, wavSROne, tsOne= synth.readWavFile('./audio/subtractive/input/Audio_One.wav',44100,time=True)
    # ** Step 2 - Plot the orginal frquency spectrum and time domain of the wav file 
    synth.plotMagnitudeSpecHertz(wavSignalOne,wavSROne,'Audio One - Orginal Frequency Spectrum',path='./plots/subtractive/input/frequency_domain/amplitudes/Audio_One.jpg',show=showPlots)
    synth.plotMagnitudeSpecHertz(wavSignalOne,wavSROne,'Audio One - Orginal Frequency Spectrum Db',path='./plots/subtractive/input/frequency_domain/decibels/Audio_One.jpg',show=showPlots,db=True)
    synth.plotSignal(wavSignalOne,tsOne,'Audio One - Orginal Time Domain',path='./plots/subtractive/input/time_domain/Audio_One.jpg',show=showPlots)
    # ** Step 3 - Filter
    #   In this step we are filtering out components from the signal in the lower frequency range 
    #   The Cymbal content that we want to extract lies in the high frequency ranges of 3000 Hz to 5000 Hz
    #   The lower frequency ranges contain the drum and bass content that needs to be removed
    #   The function filterByInstrument can be used to give what intrument it is that needs to be extracted from audio
    #   It uses a lookup table contained in the file Lib/instrumentBreakFreq.json to look up the frequency ranges for a given instrument
    #   It then applies a bandpass filter using the frequency ranges as the break points for the bandpass filter 
    #   It does not work with all audio files but is a good estimate. 
    # Filter the signal with a bandpass filter and break frequencys of 3000 and 5000 Hz associated with the Cymbal/Hi-hat instrument
    filtSigOne = synth.filterByInstrument(wavSignalOne,wavSROne,'Cymbal/Hi-hat')
    # ** Step 4 - Show a comparison of before and after the filtering in the frequency and time domain 
    synth.compareFrequencySpec([wavSignalOne,filtSigOne],['Original','Filtered'],wavSROne,'Audio One - Before and After Bandpass filtering 3kHz to 5kHz Decibels',outputFile='./plots/subtractive/output/frequency_domain/decibels/Audio_One_Filtered_Before_After.jpg',db=True,show=showPlots)
    synth.compareFrequencySpec([wavSignalOne,filtSigOne],['Original','Filtered'],wavSROne,'Audio One - Before and After Bandpass filtering 3kHz to 5kHz',outputFile='./plots/subtractive/output/frequency_domain/amplitudes/Audio_One_Filtered_Before_After.jpg',show=showPlots)
    synth.compareTimeDomain([wavSignalOne,filtSigOne],tsOne,['Original','Filtered'],'Audio One - Before and After Bandpass filtering 3kHz to 5kHz',outputFile='./plots/subtractive/output/time_domain/Audio_One_Filtered_Before_After.jpg',show=showPlots)
    # ** Step 5 - Plot the final processed signal indivdually 
    synth.plotMagnitudeSpecHertz(filtSigOne,wavSROne,'Audio One - Final Processed Signal',path='./plots/subtractive/output/frequency_domain/amplitudes/Audio_One_Final_Processed_Sig.jpg',show=showPlots)
    synth.plotMagnitudeSpecHertz(filtSigOne,wavSROne,'Audio One - Final Processed Signal Db',path='./plots/subtractive/output/frequency_domain/decibels/Audio_One_Final_Processed_Sig.jpg',show=showPlots,db=True)
    synth.plotSignal(filtSigOne,tsOne,'Audio One - Final Processed Signal',path='./plots/subtractive/output/time_domain/Audio_One_Final_Processed_Sig.jpg',show=showPlots)
    # ** Step 5 - Now write the filtered signal out to a wav file, only the Cymbal component should be present 
    synth.writeToWav('./audio/subtractive/output/Audio_One_Filtered.wav',filtSigOne,wavSROne)

    ### Signal Two (Subtractive Sythesis) - Get the bass from this signal using filters ###
    # NOTE:
    #   This section performs subtractive sythesis again however on a differnt audio file.
    #   The audio file contains bass, kettle bells and another piano like sound
    #   The bass is going to be extracted from this audio using subractive sythesis through filtering
    #   The low frequency range of the bass will be kept and the higher frequency range of the other instruments removed  
    #   This is acheived by putting the signal through a low pass filter with a break frequency of 100 HZ
    #   The original audio can be listened to in the file 
    # **Step 1 - Read in the signal from the wav file /audio/subtractive/input/Audio_Two.wav
    #   wavSignalTwo - One Dimensional array conatining signal amplitudes
    #   wavSRTwo     - Sampling frequency used for sampling the wav file, 44100 kHz set in input 
    #   tsTwo        - One Dimensional array containing timestamps for samples  
    wavSignalTwo, wavSRTwo, tsTwo= synth.readWavFile('./audio/subtractive/input/Audio_Two.wav',44100,time=True)
    # **Step 2 - Plot the frequency spectrum to see the frequency components that need to be removed and plot the time domain 
    synth.plotMagnitudeSpecHertz(wavSignalTwo,wavSRTwo,'Audio Two - Orginal Frequency Spectrum',path='./plots/subtractive/input/frequency_domain/amplitudes/Audio_Two.jpg',show=showPlots)
    synth.plotMagnitudeSpecHertz(wavSignalTwo,wavSRTwo,'Audio Two - Orginal Frequency Spectrum Db',path='./plots/subtractive/input/frequency_domain/decibels/Audio_Two.jpg',show=showPlots,db=True)
    synth.plotSignal(wavSignalTwo,tsTwo,'Audio Two - Orginal Time Domain',path='./plots/subtractive/input/time_domain/Audio_Two.jpg',show=showPlots)
    # **Step 3 - Filter
    #   The bass sound that needs to be extracted is in the lower frequency range with a notable peak at the 
    #   50 Hz region. There is a "Bass" frequency range lookup in the Lib/instrumentBreakFreq.json file however from anaysing the 
    #   signal instead of using this and filtering by intrument, a low pass filter with a -3db break frequency was chosen. The filter is a 
    #   2nd order butterworth filter with a roll off rate of 40db/Decade
    # filtSigTwo - An array containing the lowpass filtered version of wavSignalTwo 
    filtSigTwo = synth.filter(wavSignalTwo,wavSRTwo,'lowpass',100,2)
    # **Step 4 - Compare the frequency and time domain before and after filtering of the signal 
    synth.compareFrequencySpec([wavSignalTwo,filtSigTwo],['Original','Filtered'],wavSRTwo,'Audio Two - Before and After LP Filter with 100Hz Break Frequency Decibels',db=True,outputFile='./plots/subtractive/output/frequency_domain/decibels/Audio_Two_Filtered_Before_After.jpg',show=showPlots)
    synth.compareFrequencySpec([wavSignalTwo,filtSigTwo],['Original','Filtered'],wavSRTwo,'Audio Two - Before and After LP Filter with 100Hz Break Frequency',outputFile='./plots/subtractive/output/frequency_domain/amplitudes/Audio_Two_Filtered_Before_After.jpg',show=showPlots)
    synth.compareTimeDomain([wavSignalTwo,filtSigTwo],tsTwo,['Original','Filtered'],'Audio Two - Before and After Lowpass filter with 100Hz Break Frequency',outputFile='./plots/subtractive/output/time_domain/Audio_Two_Filtered_Before_After.jpg',show=showPlots)
    # ** Step 5 - Write the unamplified filtered signal to a wav file to listen to it 
    synth.writeToWav('./audio/subtractive/output/Audio_Two_Filtered_Before_Amp.wav',filtSigTwo,wavSRTwo)
    # **Step 6 - Amplification, boost the bass in the signal 
    amplifiedFiltSigTwo = filtSigTwo*10
    # ** Step 7 - Compare the orginal, filtered and amplified versions of the signal 
    synth.compareFrequencySpec([wavSignalTwo,filtSigTwo,amplifiedFiltSigTwo],['Original','Filtered','Amplified Filtered'],wavSRTwo,'Audio Two - Orginal, Filtered and Amplified Signal',outputFile='./plots/subtractive/output/frequency_domain/decibels/Audio_Two_Filtered_Before_After_and Amplification.jpg',db=True,show=showPlots)
    synth.compareFrequencySpec([wavSignalTwo,filtSigTwo,amplifiedFiltSigTwo],['Original','Filtered','Amplified Filtered'],wavSRTwo,'Audio Two - Orginal, Filtered and Amplified Signal',outputFile='./plots/subtractive/output/frequency_domain/amplitudes/Audio_Two_Filtered_Before_After_and Amplification.jpg',show=showPlots)
    synth.compareTimeDomain([wavSignalTwo,filtSigTwo,amplifiedFiltSigTwo],tsTwo,['Original','Filtered','Amplified Filtered'],'Audio Two - Orginal, Filtered and Amplified Signal',outputFile='./plots/subtractive/output/time_domain/Audio_Two_Filtered_Before_After_and Amplification.jpg',show=showPlots)
    # **Step 8 - plot the final signal 
    synth.plotMagnitudeSpecHertz(amplifiedFiltSigTwo,wavSRTwo,'Audio Two - Final Processed Signal',path='./plots/subtractive/output/frequency_domain/amplitudes/Audio_Two_Final_Processed_Sig.jpg',show=showPlots)
    synth.plotMagnitudeSpecHertz(amplifiedFiltSigTwo,wavSRTwo,'Audio Two - Final Processed Signal Db',path='./plots/subtractive/output/frequency_domain/decibels/Audio_Two_Final_Processed_Sig.jpg',show=showPlots,db=True)
    synth.plotSignal(amplifiedFiltSigTwo,tsTwo,'Audio Two - Final Processed Signal',path='./plots/subtractive/output/time_domain/Audio_Two_Final_Processed_Sig.jpg',show=showPlots)   
    # **Step 9 - Write the signal out to an audio file 
    synth.writeToWav('./audio/subtractive/output/Audio_Two_Filtered.wav',amplifiedFiltSigTwo,wavSRTwo)


    ### Additive Sythesis - Add the signals together ###
    # NOTE:
    #   This portion uses additive sythesis to create a new audio signal by adding the two signals extracted from 
    #   subractive sythesis. The audio of the cymbal extracted from Audio One and the bass extracted from Audio Two is added 
    #   together to form a new signal. 
    # **Step 1 - Mix the signals
    #   In this step the signals are mixed together. As they are both numpy arrays, the shorther signals will have to be padded out.
    #   This function can either pad the signal out with silience i.e 0's in the array or it can create a loop effect to pad out the 
    #   signal reusing samples from the audio. In this case the cymbal was longer than the bass audio so the bass was padded out reusing 
    #   samples from it to create a looping bass effect 
    # mixSig - A one dimensional array containg the amplitudes of filtSigOne and filtSigTwo added together
    # tsMix  - A one dimensional array of timestamps for the signal 
    mixSig, tsMix = synth.mixAudio([filtSigOne,amplifiedFiltSigTwo],44100)
    # Plot the mixed signal 
    synth.plotSignal(mixSig,tsMix,'Original Mixed Signal',path='./plots/subtractive/output/time_domain/Original_mixed_signal.jpg',show=showPlots)
    # Write the original mixed signal to a wav file 
    synth.writeToWav('./audio/subtractive/output/original_mix.wav',mixSig,44100)
    # **Step 2 - Extend the audio 
    #   The audio is quite short so it can be extended out 20 seconds so an idea of what the audio may sound like as a backing track
    #   in a song may sound like
    # extendedSig - The mixSig audio however it is now extended out by 20 seconds 
    extendedSig = synth.extendSig(mixSig,20,44100)
    # **Step 3 - Create a time array for the new signal so it can be plotted 
    extendedSigTs = synth.createTimeArray(extendedSig,44100)
    # **Step 4 - Plot the time domain and frequency domain of the new extended signal 
    synth.plotMagnitudeSpecHertz(extendedSig,44100,'Mixed Signal - Audio One (Cymbal) and Audio Two (Bass) Combined',path='./plots/subtractive/output/frequency_domain/amplitudes/Final_Processed_Sig.jpg',show=showPlots)
    synth.plotMagnitudeSpecHertz(extendedSig,44100,'Mixed Signal - Audio One (Cymbal) and Audio Two (Bass) Combined',path='./plots/subtractive/output/frequency_domain/decibels/Final_Processed_Sig.jpg',show=showPlots,db=True)
    synth.plotSignal(extendedSig,extendedSigTs,'Mixed Signal - Audio One (Cymbal) and Audio Two (Bass) Combined',path='./plots/subtractive/output/time_domain/Final_processed_Sig.jpg',show=showPlots)
    # **Step 5 - Plot the unmixed versiosn and the mixed versions
    # Need to first extend the audio of amplifiedFiltSigTwo by padding with zeros (repeat=False) 
    # so it is the same lenght as mixSig and filtSigOne so it can be plotted on same axis
    timeToExtend = (len(mixSig) - len(amplifiedFiltSigTwo))/44100
    amplifiedFiltSigTwoExtend = synth.extendSig(amplifiedFiltSigTwo,timeToExtend,44100,repeat=False)
    synth.compareFrequencySpec([filtSigOne,amplifiedFiltSigTwoExtend,mixSig],['Filtered Audio One','Filtered Audio Two','Mix of Filtered Audio One and Two'],44100,'Mixed Audio - Frequency Domain comparsion of Audio one, Two and Final',show=showPlots,outputFile='./plots/subtractive/output/frequency_domain/amplitudes/Audio_Final_Comparison.jpg')
    synth.compareFrequencySpec([filtSigOne,amplifiedFiltSigTwoExtend,mixSig],['Filtered Audio One','Filtered Audio Two','Mix of Filtered Audio One and Two'],44100,'Mixed Audio - Frequency Domain comparsion of Audio one, Two and Final',db=True,show=showPlots,outputFile='./plots/subtractive/output/frequency_domain/decibels/Audio_Final_Comparison.jpg')
    synth.compareTimeDomain([filtSigOne,amplifiedFiltSigTwoExtend,mixSig],tsMix,['Filtered Audio One','Filtered Audio One','Mix of Filtered Audio One and Two'],'Mixed Audio - Time Domain comparsion of Audio one, Two and Final',outputFile='./plots/subtractive/output/time_domain/Audio_Final_Comparison.jpg',show=showPlots)
    # ** Step 6 - Write the final audio out to the wav file
    synth.writeToWav('./audio/subtractive/output/final.wav',extendedSig,44100)
    

