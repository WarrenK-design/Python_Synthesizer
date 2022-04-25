### House Keeping ###
# Name           - Warren Kavanagh 
# Student Number - C16463344
# Email          - C16463344@MyTUDublin.ie


## Description ##
#   This file demonstrates of how the Sythesiser developed in this project can be used 
#   to perform additive sythesis. 
#   There are two demos in this file. The firt demo creates a square wave through additive sythesis by 
#   suumming odd harmonics.
#   The second demo shows how the Sythesiser class can create notes and they can be summed together. 

### Imports ###
#   Sythesiser - The Sythesiser class
#   numpy      - https://numpy.org/doc/stable/ 
from Lib.Synthesizer import Sythesiser
import numpy as np

if __name__=="__main__":
    # Create an instance of a Sythesiser 
    synth = Sythesiser()
    # Sampling rate of 44.1KHz
    sr = 44100 
    # showPlots - Boolean set this true if you want plots to be shown as script is run 
    showPlots = True
    
    ### Additive Sythesis - Square wave creation ###
    # NOTE
    #   Additive sythesis can be used to create a square waveform by summing the odd harmonics of a sine sinusoidal waveform
    #   The harmoincs of a waveform are multiples of the fundatemntal frequency (Lowest frequency) in a waveform 
    #   If the fundamental frequency is 100HZ the 2nd harmonic is 200Hz, 3rd is 300Hz and so on 
    #   The summing of the odd harmonics can create a square wave in the time domain and taking the fourier transform 
    #   of this waveform it can be shown that it is composed of the sums of harmonics 
    # fFund - Fundamental frequency of 100 Hz
    fFund = 100
    # numHarm - The number of harmonics to use to create the square wave 
    numHarm = 5
    # sig - Sinousoids will be recursively added to this array to form the square wave 
    sig = np.zeros(sr)
    # sigs - Dictionary to store the individual summed sinusoids so they can be plotted at the end 
    sigs = {}
    # For loop cumulatively adds each of the harmonics together to form the square wave and perform additive synthesis 
    for i in range(1,numHarm*2,2):
        # f - The frequency of the given harmonic 
        f = fFund*i
        # Create the signal using the frequency 
        sigTemp,ts = synth.createSignal(f,sr,type='sine',a=1/i)
        # Add the current signal to the previous signal - This is the additive sythesis here 
        sig+=sigTemp
        # Plot and save the plot of the individual harmonics in the time and frequency domain 
        synth.plotSignal(sigTemp,ts,f'Harmonic {i} - Frequency {f}Hz',lim=1/fFund,path=f'./plots/additive/squareWave/time_domain/individual_harmonics/Harmonic_{i}.jpg',show=showPlots)
        # Plot the frequency of the individual harmonics 
        synth.plotMagnitudeSpecHertz(sigTemp,sr,f'Harmonic {i} - Frequency {f}Hz',path=f'./plots/additive/squareWave/frequency_domain/individual_harmonics/amplitude/Harmonic_{i}.jpg',show=showPlots,lim=1000)
        synth.plotMagnitudeSpecHertz(sigTemp,sr,f'Harmonic {i} - Frequency {f}Hz',path=f'./plots/additive/squareWave/frequency_domain/individual_harmonics/decibels/Harmonic_{i}.jpg',show=showPlots,db=True,lim=1000)
        # Plot the frequency of the running sum of harmonics 
        synth.plotMagnitudeSpecHertz(sig,sr,f'Harmonic {i} Added',path=f'./plots/additive/squareWave/frequency_domain/summed/amplitude/Harmonic_{i}.jpg',show=showPlots,lim=1000)
        synth.plotMagnitudeSpecHertz(sig,sr,f'Harmonic {i} Added',path=f'./plots/additive/squareWave/frequency_domain/summed/decibels/Harmonic_{i}.jpg',show=showPlots,db=True,lim=1000)
        # Write the individual harmonics to a wav file 
        synth.writeToWav(f'./audio/additive/square/individual_harmonics/Frequency_{f}_Harmonic_{i}.wav',sigTemp,sr)
        # Write the running sum to a wav file 
        synth.writeToWav(f'./audio/additive/square/summed_harmonics/Harmonic_{i}_Sum.wav',sig,sr)
        # Plot the running sum 
        synth.plotSignal(sig,ts,f'Harmonic {i} Added ',lim=1/fFund,path=f'./plots/additive/squareWave/time_domain/summed/Harmonic_{i}.jpg',show=False)
        # Add the current running sum to the sigs dictionary, it is used later to plot how the signal changes whith each harmonic added
        # We need to pass by value here not reference that is why list is used 
        sigs[i] = list(sig)
    # Create a time array for plotting 
    ts = synth.createTimeArray(sig,sr)
    # Create the labels to be used in the legend in the plot 
    labels = [f'Sum of {x} Harmonics' for x in range(1,numHarm+1)]
    # Create a one dimensional array from the array of dictionarys 
    harms = [value for key,value in sigs.items()]
    # Plot the evolution of how the square wave is created by summing each of the harmonics 
    synth.compareTimeDomain(harms,ts,labels,'Square Wave Through Additive Synthesis',lim=1/fFund,outputFile='./plots/additive/squareWave/Sum_Of_Hamronics.jpg',show=showPlots)
    # Plot the frequency spectrum of the final signal
    synth.plotMagnitudeSpecHertz(np.array(harms[-1]),sr,'Frequency Spectrum of square wave',show=showPlots,path='./plots/additive/squareWave/frequency_domain/summed/amplitude/Final_Frequency_Spectrum.jpg',lim=1000)
    synth.plotMagnitudeSpecHertz(np.array(harms[-1]),sr,'Frequency Spectrum of square wave Decibels',show=showPlots,path='./plots/additive/squareWave/frequency_domain/summed/decibels/Final_Frequency_Spectrum.jpg',db=True,lim=1000)


    ### Additive Sythesis - Adding Notes together ###
    # NOTE
    #  This section demonstrates how additive sythesis can be used to create new audio sounds by summing sine waves
    #  The sythesiser class developed as part of this project can be used to create notes which are just a sinusoid of a certain
    #  frequency. We can then add these notes together to create a new sound. The notes are created using a lookup table in Lib/notes.json
    # Create a few different notes
    # noteTime - The duration for each of the notes in seconds
    noteTime = 3 
    notes = [
        {'note':'Db','octave':5,'t':noteTime,'a':1,'type':'cosine'},
        {'note':'F','octave':6,'t':noteTime,'a':1,'type':'cosine'},
        {'note':'B','octave':5,'t':noteTime,'a':1,'type':'cosine'},  
        {'note':'Ab','octave':6,'t':noteTime,'a':1,'type':'cosine'},
        {'note':'E','octave':7,'t':noteTime,'a':1,'type':'cosine'},
    ]
    # noteSig - Will contain the final mixed signal 
    noteSig = np.zeros(sr*noteTime)
    # Iterate through each of the notes creating a sinusoid for each 
    for note in notes:
        # Create the sinusoid for the note 
        sig, ts = synth.createNote(sr,note['note'],note['octave'],a=note['a'],t=note['t'],type=note['type'])
        # Plot and save the plot of the individual note{synth.notes[note['note']][note['octave']]}lim=(1/synth.notes[note["note"]][note["octave"]])*10
        synth.plotSignal(sig,ts,f'Note {note["note"]} Octave {note["octave"]} - Freqeuncy {synth.notes[note["note"]][note["octave"]]}',path=f'./plots/additive/notes/time_domain/Note_{note["note"]}_Octave_{note["octave"]}.jpg',show=showPlots,lim=0.1)
        # Create a wav file of the individual note so it can be listened to 
        synth.writeToWav(f'./audio/additive/notes/Note_{note["note"]}_Octave_{note["octave"]}_Freqeuncy_{synth.notes[note["note"]][note["octave"]]}_Hz.wav',sig,sr)
        # Additive Sythesise - Add the current signal to the previous signal to create a running cumlative sum 
        noteSig+=sig

    # Create a time array for plotting the notes
    tsNotes = synth.createTimeArray(noteSig,sr)
    # Plot the summed sinusoids over the full lenght of 3 seconds and then zoom into 0.10 seconds
    synth.plotSignal(noteSig,tsNotes,'Time domain of summed notes',path='./plots/additive/notes/time_domain/summedNotesOver3Seconds.jpg',show=showPlots)
    synth.plotSignal(noteSig,tsNotes,'Time domain of summed notes',path='./plots/additive/notes/time_domain/summedNotesOver010Seconds.jpg',lim=0.1,show=showPlots)  
    # Plot the frequency sepctrum of the signal in db and amplitude
    synth.plotMagnitudeSpecHertz(noteSig,sr,'Frequency Spectrum of summed notes\n554.37 Hz, 987.77 Hz, 1396.91 Hz, 1661.22 Hz and 2637.02 Hz',show=showPlots,path='./plots/additive/notes/frequency_domain/decibels/notes_db.jpg',db=True)
    synth.plotMagnitudeSpecHertz(noteSig,sr,'Frequency Spectrum of summed notes\n554.37 Hz, 987.77 Hz, 1396.91 Hz, 1661.22 Hz and 2637.02 Hz',show=showPlots,path='./plots/additive/notes/frequency_domain/amplitudes/notes_db.jpg',lim=3000)
    # Write the summed signal out to a wav file
    synth.writeToWav('./audio/additive/notes/summed_signal.wav',noteSig,sr)