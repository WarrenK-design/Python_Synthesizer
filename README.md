# Audio Assignment - Python Synthesizer
This repository holds the code for the audio assignment project. 
The project developed a Synthesizer class for audio manipulation in Python and used it to perform additive and subtractive synthesis. 

This readme file details how to run the project and the files/directorys in the repo. 

## Installation
Packages have to be installed first for the code to run. The ````requirements.txt``` file for dependecies can be used to install the dependencies for the project. 

```
pip install -r requirements.txt
```

## Run Files 
There are three run files in total which relate to the demos show in the presentation.

1. **additiveSynth.py** - Demo of additive sythesis 
2. **subtractiveSynth.py** - Demo of subtractive synthesis
3. **happyBirthday.py** - Demo on song creation 

### additiveSynth.py
To run the file use the following command. 
```
python .\additiveSyth.py
```
It outputs wav audio files to the directory `audio\additive`.

The directory `audio\additive\notes` contains the audio files for additive synthesis of notes demo. 

The directory `audio\additive\square` conatains the audio files for the additive sythesis to generate a square wave.

It outputs plots to the directory `plots\additive`.

The directory `plots\additive\notes` contains plots for the additive synthesis of notes demo.

The directory `plots\additive\squareWave` contains plots for the additive synthesis to generate a square wave. 

### subtractiveSynth.py 
To run the file use the following command. 
```
python .\subtractiveSynth.py 
```
It outputs and uses input wav audio files to/from the directory `audio\subtractive`.

The directory `audio\subtractive\input` contains the input raw audio files used. 

The directory `audio\subtractive\output` contains the output audio files. 

It outputs plots to the directory `plots\subtractive`.

The directory `plots\subtractive\input` contains plots related to the input audio files used. 

The directory `plots\subtractive\output` contains plots related to the output audio files.

### happyBirthday.py
To run the file use the following command. 
```
python .\happyBirthday.py 
```
It outputs audio to the file `audio\songs\HappyBirthday.wav`

The directory `plots\song` conatins output plots. 

## Lib Directory 
The lib firectory contains three files. 

1. **Synthesizer.py** - This contains the class of the Python Synthesizer developed in this project. 
2. **notes.json**     - Conatins a lookup table for note/octave frequencies. Obtained [here](https://gist.github.com/i-Robi/8684800).
3. **instrumentBreakFreq.json** - Contains a lookup table to be used as a reference for filtering intruments using a band pass filter. Obtained for [here](https://www.zytrax.com/tech/audio/audio.html)