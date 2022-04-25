### House Keeping ###
# Name           - Warren Kavanagh 
# Student Number - C16463344
# Email          - C16463344@MyTUDublin.ie

## Description ##
#   The class Sythesiser is to act as a python implmentation of a sythesiser
#   The functions which are implmented within this class can be used then to demonstrate
#   both additive and subtractive sythesis
#   Each function has a doctstring which explain what the function does, the inputs of the 
#   function and what the return value is.  


### Imports ###
# json       - https://docs.python.org/3/library/json.html
# numpy      - https://numpy.org/doc/stable/
# signal     - https://docs.scipy.org/doc/scipy/reference/signal.html 
# matplotlib - https://matplotlib.org/stable/api/index
# librosa    - https://librosa.org/doc/latest/index.html
# soundFile  - https://pysoundfile.readthedocs.io/en/latest/
# math       - https://docs.python.org/3/library/math.html 
import json
import numpy as np 
from scipy import signal
import matplotlib.pyplot as plt
import librosa
import soundfile as sf
import math 

class Sythesiser:

    def __init__(self):
        '''
        Description:
            Initialiser function, reads in the notes file for the frequencys of notes 
            and stores them in class variables notes.
        '''
        # Open the notes file, contains lookup table for frequency notes 
        f1 = open('./Lib/notes.json')
        # Store the notes in python dictionary 
        self.notes = json.load(f1)
        # Open the instrument break frequencys, used for filtering by instrument type 
        f2 = open('./Lib/instrumentBreakFreq.json')
        # Store the breakfreqeuncies in a array dictionary 
        self.intrumentBreakFreq = json.load(f2)


    def createSignal(self,f,fs,a=1,t=1,type='cosine'):
        '''
        Description:
            Acts like an oscillator in the Sythesiser. It creates a signal of specified frequency,
            amplitude and over a certain time. The shape of the waveform can also be specified. 
        Inputs:
            f    - Freqeuncy of the signal in Hertz
            fs   - The sampling freqeuncy of the signal in Hertz
            a    - The amplitude of the signal 
            t    - The duratiopn of the signal in seconds 
            type - The signal type which will effect its shape. Inputs can be cosine, sine, sawtooth or square. 
        Returns:
            s  - Array containing the signal samples amplitudes.
            ts - Array containing timestamps of where samples where taken.  
        '''
        # Create a time array 
        ts = np.arange(0,t,1/fs)
        if type == 'cosine':
            # Create a cosine wave and return the samples in s and the time samples in ts
            s = a*np.cos(2*np.pi*f*ts)
            return s, ts
        elif type == 'sine':
            # Create a sine wave and return the samples in s and the time samples in ts
            s = s = a*np.sin(2*np.pi*f*ts)   
            return s, ts
        elif type == 'sawtooth':
            # Create a sawtooth wave and return the samples in s and the time samples in ts
            s = a*signal.sawtooth(2*np.pi*f*ts) 
            return s, ts 
        elif type == 'square':
            # Create a square wave and return the samples in s and the time samples in ts
            s = a*signal.square(2*np.pi*f*ts)
            return s, ts


    def createNote(self,fs,note,octave,a=1,t=1,type='cosine'):
        '''
        Description:
            Creates sinusoid which corresponds to the frequency of a musical note. 
            This is done using the lookup table in the file notes.json
        Inputs:
            fs     - Sampling frequency specified in hertz
            note   - The name of the note. Acceptable inputs are one of the following "C" "Db" "D" "Eb" "E" "F" "Gb" "G" "Ab" "A" "Bb" "B" 
            octave - The octave of the nore. Single number in the range 0 - 8
            a      - Amplitude of the signal
            t      - Duration in seconds of the signal 
            type   - The shape of the wave form. Inputs can be cosine, sine, sawtooth or square.  
        Returns:
            s - Array of amplitudes for this signal.
            ts - Array of timestamps where samples where taken. 
        '''
        # Create the array of timestamps 
        ts = np.arange(0,t,1/fs)
        # Get the frequency of the chosen note
        f = self.notes[note][octave]
        if type == 'cosine':
            # Create a cosine wave 
            s = a*np.cos(2*np.pi*f*ts)
            return s, ts
        elif type == 'sine':
            # Create a sine wave 
            s = s = a*np.sin(2*np.pi*f*ts)   
            return s, ts
        elif type == 'sawtooth':
            # Create a sawtooth wave 
            s = a*signal.sawtooth(2*np.pi*f*ts) 
            return s, ts 
        elif type == 'square':
            # Create a square wave 
            s = a*signal.square(2*np.pi*f*ts)
        return s, ts



    def plotSignal(self,sig,t,title,lim=None,path=None,show=True):
        '''
        Description:
            Plots a supplied signal in the time domain.
        Inputs:
            sig - Array containing signal amplitudes for the y-axis coordinates  
            t   - Array containing time points for the x-axis coordinates  
            title - Title for the plot 
            lim - Optional limit to only plot the signal over a particular time range
            path - Optional path to save the figure to, include file name in path.
            show - If set true will show the plot, if set false will not show the plot. 
        '''
        # Create the plot
        plt.plot()
        # Fill x and y axis coords
        plt.plot(t,sig)
        # Put label on x-axis
        plt.xlabel('Time (s)')
        # Put label on y-axis
        plt.ylabel('Amplitude')
        # Put title on fig 
        plt.title(title)
        if lim:
            # Cut limit of x-axis
            plt.xlim([0,lim])
        if path:
            # Save the figure to file 
            plt.savefig(path)
        if show:
            # Show the plot 
            plt.show()
        # Close the figure, if dont do this figures wil be plotted over eachother 
        plt.close()

    def plotMagnitudeSpecHertz(self,sig,fs,title,path=None,show=True,db=False,lim=None):
        '''
        Description:
            Plots the magnitude spectrum of a signal passed is Herzts 
        Inputs:
            sig   - Array containing signal amplitudes 
            fs    - The sample rate of the signal Hertz
            title - The title for the graph 
            path  - Path to save the plot to
            show  - Set true to show the plot, false will not show the plot 
            db    - Boolean, if set true will use the db scale for plots
            lim   - A limit specified in hertz to limit the X-Axis to  
        '''
        # Set plt title and axis labels
        plt.title(title)
        plt.xlabel('Frequency (Hz)')
        # Check if on db scale or not
        if db:
            plt.ylabel('Amplitude (dB)')
        else:
            plt.ylabel('Amplitude')
        # Get the fft of the signal 
        sigFFT = np.fft.fft(sig)
        # Get the frequency samples for the fft, 
        # first input is signal size for window length and second is sample spacing use 1/sample rate
        freqSamples = np.fft.fftfreq(sig.size,d=1/fs)
        # The negtaive frequencys will be first and produces a constant line on graph if do not shift samples 
        sigFFT = np.fft.fftshift(sigFFT)
        freqSamples = np.fft.fftshift(freqSamples)
        # Get the absolute value of fft 
        absFFT = abs(sigFFT)
        # Check if want db scle for amplitudes 
        if db:
            # The reference intentisy is the max val, for PCM audio used in this project will be sinudsoids of amplitude 1 
            ref = max(absFFT)
            # Get the fft on the decibel scale
            decibelFFT = 20*np.log10(absFFT/ref)
            # Plot the the freqSamples (Hz) vs fft abs amplitudes
            plt.plot(freqSamples,decibelFFT)
        else:
            # Not on the db scale plot raw amplitudes
            plt.plot(freqSamples,absFFT)   
        # Dont plot negative frequencys produced by fftfreq double spectrum, plot up to max positive freq sample or the limit specified
        if lim:
            plt.xlim([0,lim])
        else:
            plt.xlim([0,freqSamples.max()])
        if path:
            # Save the figure to file 
            plt.savefig(path)
        if show:
            # Show the plot 
            plt.show()
        # Close the plot
        plt.close()


    def readWavFile(self,path,fs,duration=None,offset=None,time=False):
        ''''
        Description:
            Reads in a wav file from a specified path and returns the wav file array. 
            Optionally returns also the time array samples 
        Inputs:
            path - The path including the file name for the file to read in 
            fs   - The sampling rate 
            duration - Only read a certain amount of the audio in. Specified in seconds. 
            offset   - The offset to start reading the file in at 
            time - Boolean, if set to true will return an array of timestamps
        Return:
            wavSignal - Array containing signal amplitudes. 
            wavSR     - The sample rate used to read in the signal 
            ts        - Array of timestamps for samples. 
        '''
        wavSignal, wavSR = librosa.load(path,duration=duration,offset=offset,sr=fs)
        if time:
            lenAudio = len(wavSignal)/wavSR
            ts = np.arange(0,lenAudio,1/wavSR)
            return wavSignal, wavSR, ts
        else:
            return wavSignal, wavSR

    def writeToWav(self,path,sig,sr):
        '''
        Description:
            Writes a signal out to a wav file
        Inputs:
            path - The path including the file name of the output file
            sig  - The signal to write to a file, an array of signal amplitudes
            sr   - The sampling rate 
        '''
        sf.write(path,sig,sr)


    def createSong(self,notes,fs,outputFile=None):
        '''
        Description:
            This function creates a song by sepcfying the notes to play there amplitudes and what order 
            to play them in. The song is then written to the utput file and returned. 
        Inputs:
            notes      - Array of dictionarys where each dictionary is a note. Each dictionary must have the elements 
                            note    - The name of the note either "C" "Db" "D" "Eb" "E" "F" "Gb" "G" "Ab" "A" "Bb" "B" 
                            octave  - The octave of the note. Single number in the range 0 - 8
                            t       - The duration of the note in seconds 
                            a       - The amplitude of the note 
                            type    - Type of wave form. Either cosine, sine, sawtooth or square. 
            fs         - The Sampling rate in Hertz 
            outputFile - Stirng of the outputFile destination
        Returns:
            song - An array containing the amplitudes of the full song signal
            ts   - Array of timestamps for the samples of the signal taken   
        '''
        # songNotes - Array which will hold each of the signals representing notes 
        songNotes = []
        # For each note create a sinusoid 
        for note in notes:
            # Create the sinusoid using createNote
            sig, ts = self.createNote(fs,note['note'],note['octave'],a=note['a'],t=note['t'],type=note['type'])
            # Append the sinusoid to the array of notes 
            songNotes.append(sig)
        # Flatten the list of notes
        flat_list = [item for sublist in songNotes for item in sublist]
        # Concatenate the array of notes to create a song 
        song = np.concatenate(songNotes)
        # If output file specified then save to the outputfile
        if outputFile:
            sf.write(outputFile,flat_list,fs)
        # Get the length of the audio and use it to calculate timestamp points 
        lenAudio = len(song)/fs
        ts = np.arange(0,lenAudio,1/fs)
        # Return the song array and the timestamp array 
        return song, ts


    def filter(self,sig,fs,type,breakFreq,order):
        '''
        Description:
            Filters a signal using a butterworth filter.
            The type of filter used depends upon the "type" supplied 
        Inputs:
            signal    - Array containing samples of the signal 
            fs        - Sampling frequency of the signal, Hertz
            type      - The type of filter either lowpass, highpass, bandpass or bandstop
            breakFreq - The -3db point of the filter, i.e the break frequency Hertz. Number if filter is lowpass or highpass. Array of two numbers if filter is bandpass or bandstop.
            order     - The filter order, the higher the order the steeper the roll off rate in dB per decade
        Returns:
            filteredSig - The filtered version of the input signal 

        '''
        # Get the b and a coeffcients, give sampling frequency fs to specify breakFreq is in Hertz
        b,a = signal.butter(N=order,Wn=breakFreq,btype=type,fs=fs)
        # Filter the signal 
        filteredSig = signal.lfilter(b,a,sig)
        # Return the filtered signal 
        return filteredSig


    def notchFilter(self,sig,fs,fo,q):
        '''
        Description:
            This implements a notch filter. When there is a particular frequency that needs to be removed or a very 
            small bandwidth of freqeuncys need to be removed this should be used.
        Inputs:
            sig - An array containing the signal to be filtered 
            fs  - The sampling frequency of the signal
            fo  - The frequency to be removed
            q   - The quality factor of the notch filter, determines how wide the bandwidth of the filter is
        '''
        # Get the b and a coeffcients 
        b, a = signal.iirnotch(fo,q,fs)
        # Use the b and a coeffcients to apply the filter 
        filteredSig = signal.lfilter(b,a,sig)
        # Return the signal 
        return filteredSig


    def filterByInstrument(self,sig,fs,instrument,order=1):
        '''
        Description:
            This function filters frequencys by intrument using an approximation of frequency ranges 
            retrieved from https://www.zytrax.com/tech/audio/audio.html
        Inputs:
            sig        - Array containing the signals amplitudes. 
            fs         - The sampling rate of the signal 
            instrument - The instrument to filter, see the file instrumentBreakFreq to see the acceptable inputs. 
            order      - The order of the filter. 
        Returns:
            filteredSig - Returns a filtered signal 
        '''
        # Get the break frequency for intrusment 
        breakFreqs = self.intrumentBreakFreq[instrument]
        # Band stop filter over these frequency ranges 
        return self.filter(sig,fs,'bandpass',breakFreqs,order)


    def compareFrequencySpec(self,sigs,labels,fs,title,legendLoc ="lower right",outputFile=None,db=False,show=True):
        '''
        Description:
            Plots the frequency spectrum of a number of signals on the same plot. 
            Used to compare the same signal before ts been filtered and after it has been filtered. 
        Inputs:
            sigs         - Array of signals to calculate the Fourier Transform for
            labels       - Array of the labels which will appear on the plots legend, must be in same order as sigs array
            fs           - The sampling frequency to use, each signal must use the same sampling frequency  
            title        - The title of the graph 
            legendLoc    - Location of the legend on the graph 
            outputFile   - The location to save the figure to 
            db           - Boolean, if set true will plot on the DB scale 
            show         - Boolean, if set true will show the plot when running the code 
        '''
        plt.xlabel('Frequency (Hz)')
        if db:
            plt.ylabel('Amplitude (dB)')
        else:
            plt.ylabel('Amplitude')
        plt.title(title)
        # If you want db then need to calculate the ref first
        ref = self.calculateRefForDB(sigs) if db else 0
        for sig in sigs:
            # Get the fft of the signal 
            sigFFT = np.fft.fft(sig)
            # Get the frequency samples for the fft, 
            # first input is signal size for window length and second is sample spacing use 1/sample rate
            freqSamples = np.fft.fftfreq(sig.size,d=1/fs)
            # The negtaive frequencys will be first and produces a constant line on graph if do not shift samples 
            sigFFT = np.fft.fftshift(sigFFT)
            freqSamples = np.fft.fftshift(freqSamples)
            # Get the absolute value of fft 
            absFFT = abs(sigFFT)
            # If db scale plot db's 
            if db:
                # Get the fft on the decibel scale
                decibelFFT = 20*np.log10(absFFT/ref)
                plt.plot(freqSamples,decibelFFT)
            else:
                # Just plot the magnitudes 
                plt.plot(freqSamples,absFFT)
        # Dont plot negative frequencys produced by fftfreq double spectrum, plot up to max positive freq sample
        plt.xlim([0,freqSamples.max()])
        # Add the legends to the graph 
        plt.legend(labels,loc=legendLoc)
        # Save the plot if output file set 
        if outputFile:
            # Save the figure to outputFile 
            plt.savefig(outputFile)
        # Show the plot
        if show:
            plt.show()
        plt.close()

    def calculateRefForDB(self,sigs):
        '''
        Description:
            When plotting multiple signals on DB scale they need to be all compared against the same reference. 
            This function get the reference by finding the max value from the signals needed to be comapared. 
            Used especially when signals are amplified and do not lie within the region 0 to 1 in time domain
        Inputs:
            sigs - An array of signals which will be comapred 
        Returns:
            ref - The reference to use when calulating DB
        '''
        # Iitilise the ref to 0 
        ref = 0 
        for sig in sigs:
            # Get the fft of the signal 
            sigFFT = np.fft.fft(sig)
            # Get the absolute value of fft 
            absFFT = abs(sigFFT)
            # If the current max is greaest set the ref 
            if ref < max(absFFT):
                    # The reference intentisy is the max val, for PCM audio used in this project will be sinudsoids of amplitude 1 
                    ref = max(absFFT)
        return ref 


    def compareTimeDomain(self,sigs,t,labels,title,legendLoc ="lower right",lim=None,outputFile=None,show=True):
        '''
        Desctiption:
            Compares signals of the same length in the time domain.
            Can be used to see how a signal has changed in the time domain after filtering/amplification.
        Inputs:
            sigs       - Array of signals to compare, each element is an array realting to an individual signal
            t          - Array of the time domain to be used for each signal. Each signal will be plotted agianst this time domain. 
            labels     - Array conatining the labels for the plot, need to be in the same order as sigs array 
            title      - The title of the graph 
            legnedLoc  - The location of the legend on the graph 
            lim        - A limit can be set to limit the time the signal is plotted over 
            outputFile - The file to save the plot to, set only if you want to save it 
            show       - Boolean whether to show the plot as script is running  
        '''
        # Create the plot
        plt.plot()
         # Put label on x-axis
        plt.xlabel('Time (s)')
        # Put label on y-axis
        plt.ylabel('Amplitude')
        # Put title on fig 
        plt.title(title)
        for sig in sigs:
            # Fill x and y axis coords
            plt.plot(t,sig)
        # Add the legends to the graph 
        plt.legend(labels,loc=legendLoc)
        if lim:
            # Cut limit of x-axis
            plt.xlim([0,lim])
        if outputFile:
            # Save the figure to file 
            plt.savefig(outputFile)
        if show:
            # Show the plot 
            plt.show()
        # Close the figure, if dont do this figures wil be plotted over eachother 
        plt.close()


    def extendSig(self,sig,t,fs,repeat=True):
        '''
        Description:
            Will extend a signal by a specific number of seconds by repeating parts of the signal 
        Inputs:
            sig    - An array containing the signal to repeat 
            t      - The number of seconds to extend the signal by 
            fs     - The sampling frequency
            repeat - If set to true will reuse the samples to extend the signal creating a looped effect. False it just adds 0's to pad. 
        Return:
            extendedSig - An array contining the extended signal amplitudes 
        '''
        # Calculate the number of samples needed for the extension time 
        samplesNeeded = int(fs*t)
        # Check to loop the sound in extneding the signal 
        if repeat:
            # If the lenght of the original audio is greater the lenth of samples needed then just take these samples from original 
            if len(sig) >= samplesNeeded:
                # Index the original and take these samples 
                samples = sig[0:samplesNeeded]
                # Create the new audio file 
                extendedSig = np.concatenate([sig,samples])
                # Return the extended signal 
                return extendedSig
            else:
                # There arent enough samples to just take straight from the audio, need to repeat samples 
                # Calculate how many repeats it will take to get enough samples
                repeatSamples = math.ceil(samplesNeeded/len(sig))
                # Repeat the orginal signal "repeat" number of times
                repeatedSig = np.tile(sig,repeatSamples)
                # Index the samples needed 
                samples = repeatedSig[0:samplesNeeded]
                # Extend the signal by this number of samples 
                extendedSig = np.concatenate([sig,samples])
                # Return the signal 
                return extendedSig
        else:
            # Not looping the song just padding with 0's to extend
            extendedSig = np.concatenate([sig,np.zeros(samplesNeeded)])
            return extendedSig

    def mixAudio(self,sigs,fs,loopPad=True):
        '''
        Description:
            Takes multiple signals and mixes them together to create a signal output signal 
        Inputs:
            sigs    - An array of signals to be mixed together
            fs      - The Sampling frequency used to sample the audio
            loopPad - Boolean, if set false will pad signals with zero, if true will loop signals to fill length  
        Returns:
            finalSig - The mixed signal array containing amplitudes 
            ts       - A time array containing timestamps for the signal samples 
        '''
        # Calculate the lenght of the longest signal in the sigs array 
        longestSigLen = (len(max(sigs,key=len)))
        # newSigs - This is an array which will hold all the signals of equal lenght when they are padded 
        newSigs = [] 
        # Iterate through each of the signals to be mixed 
        for sig in sigs:
                # If the signal is not the longest signal then it needs to be padded out to be mixed 
                if len(sig) != longestSigLen:
                    # If loop padding is specified then the signal can be looped to achieve padding of lenght 
                    if loopPad: 
                        # Audio needs to be exetended by certain length
                        timeToExtened = (longestSigLen - len(sig))/fs
                        # Extend the audio by repeating it using the extendSig function, append it to the newSigs array 
                        newSigs.append(self.extendSig(sig,timeToExtened,fs))
                    else: # No loop padding specified, pad with zeros 
                        newSigs.append(np.concatenate([sig,np.zeros(longestSigLen - len(sig))]))
                else:
                    # Audio does not need to be extneded as it is the longest signal 
                    newSigs.append(sig)
        # Final sig will be the resulting final signal, initiliase it full of zeros
        finalSig = np.zeros(longestSigLen)
        # Iterate through each of the signals and add them to finalsig 
        for sig in newSigs:
            finalSig+=sig
        # Calculate the lenght of the audio
        lenAudio = len(finalSig)/fs
        # Use the lenght and sampling freq to create a array of timesatamps for the signal 
        ts = np.arange(0,lenAudio,1/fs)
        # Return the final sig and timestamps        
        return finalSig,ts        

    def createTimeArray(self,sig,fs):
        '''
        Description:
            Creates a time array for a signal passed to it for a given sample frequency. 
        Inputs:
            sig - One dimensional array containing signal amplitudes 
            fs  - The sampling frequency used to sample the signal 
        Returns:
            ts - A one dimensional array containg timestamps
        '''
        # Calculate the lenght of the audio
        lenAudio = len(sig)/fs
        # Use the lenght and sampling freq to create a array of timesatamps for the signal 
        ts = np.arange(0,lenAudio,1/fs)
        return ts
