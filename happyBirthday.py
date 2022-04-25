### House Keeping ###
# Name           - Warren Kavanagh 
# Student Number - C16463344
# Email          - C16463344@MyTUDublin.ie

## Description ##
#   This file is just a short demonstration of the createSong functionality of the Sythesiser class
#   developed in this project. It uses the sythesier to create the song happy birthday.

### Imports ###
# Sythesiser - A class developed for this project which acts as a python implmentation of a sythesiser 
from Lib.Synthesizer import Sythesiser

if __name__ == "__main__":
    # Create an instance of a Sythesiser 
    synth = Sythesiser()
    # Sampling rate of 44.1KHz
    sr = 44100
    # showPlots - Boolean set this true if you want plots to be shown as script is run 
    showPlots = True

    ## happyBirthdayNotes ##
    # Array of dictionary items which contains the notes for the happy birtday song
    # This will be supplied as input to the createSong function in the synth class
    # Each element in the array is a dictionary which relates to a single note in the song 
    # Each dictionary has associated with it:
    #   note   - The name of the note, acceptable values are "C" "Db" "D" "Eb" "E" "F" "Gb" "G" "Ab" "A" "Bb" "B" ,see Lib/notes.json for lookups on these notes which createSong uses
    #   octave - The octave relating to the note, integer from 0 to 8 
    #   t      - The duration of the note in seconds 
    #   a      - the amplitude of the note 
    #   type   - The shape of the waveform of the note, acceptable values are cosine, sine, sawtooth or square. 
    happyBirthdayNotes = [
        {'note':'C','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'C','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'D','octave':4,'t':1,'a':1,'type':'cosine'},  
        {'note':'C','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'F','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'E','octave':4,'t':1,'a':1,'type':'cosine'},     
        {'note':'C','octave':4,'t':1,'a':1,'type':'cosine'},        
        {'note':'C','octave':4,'t':1,'a':1,'type':'cosine'}, 
        {'note':'D','octave':4,'t':1,'a':1,'type':'cosine'},   
        {'note':'C','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'G','octave':4,'t':1,'a':1,'type':'cosine'},        
        {'note':'F','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'C','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'C','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'C','octave':5,'t':1,'a':1,'type':'cosine'},
        {'note':'A','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'F','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'E','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'D','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'Bb','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'Bb','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'A','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'F','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'G','octave':4,'t':1,'a':1,'type':'cosine'},
        {'note':'F','octave':4,'t':1,'a':1,'type':'cosine'}
    ]  
    ### Create Song ###
    # Creates the song using the dictionary of notes above 
    # The notes are played in the order of the dictionary 
    # The final output is written to   
    song, ts = synth.createSong(happyBirthdayNotes,44100,'./audio/songs/HappyBirthday.wav')

    ### Plot the frequency spectrum and time domain 
    synth.plotMagnitudeSpecHertz(song,44100,'Happy Birthday - Frequency Domain',path='./plots/song/frequency_domain/amplitudes/HappyBirthday_Song.jpg',show=showPlots,lim=1000)
    synth.plotMagnitudeSpecHertz(song,44100,'Happy Birthday - Frequency Domain Decibels',path='./plots/song/frequency_domain/decibels/HappyBirthday_Song.jpg',show=showPlots,db=True)
    synth.plotSignal(song,ts,'Happy Birthday - Time Domain',path='./plots/song/time_domain/HappyBirthday_Song.jpg',show=showPlots)



