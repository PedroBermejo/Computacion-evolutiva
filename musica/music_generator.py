#!/usr/bin/env python
from midiutil import MIDIFile
from genetic import helper
import os.path

dirPath = "musica/output/"
fileName = "musica/output/output.mid"
index = 1

track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 30   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

 # MyMIDI = MIDIFile(1)  One track, defaults to format 1 (tempo track is created
                      # automatically)


degreesPiano = helper.createPopulation(22, 110, 50, 10)
degreesAcordion = helper.createPopulation(22, 110, 50, 10)
timesPiano = helper.createPopulation(0, 10, 50, 10)
timesAcordion = helper.createPopulation(0, 10, 50, 10)
volumes = helper.createPopulation(80, 100, 50, 10)
durations = helper.createPopulation(1, 5, 50, 10)
tempos = helper.createPopulation(20, 40, 1, 10)

for i in range(len(degreesPiano)):
    MyMIDI = MIDIFile(2, adjust_origin=False) 
    MyMIDI.addTempo(track, time, tempos[i][0])
    MyMIDI.addProgramChange(0, 0, 0, 0)

    for j, pitch in enumerate(degreesPiano[i]):
        MyMIDI.addNote(track, channel, pitch, time + (j-1 + timesPiano[i][j-1])/10 , durations[i][j-1], volumes[i][j-1])
    
    # change track to 1 and instrument to acordion
    MyMIDI.addProgramChange(0, 1, 0, 26)

    for j, pitch in enumerate(degreesAcordion[i]):
        MyMIDI.addNote(track + 1, channel +1, pitch, time + (j-1 + timesAcordion[i][j-1])/10 , durations[i][j-1], volumes[i][j-1])

    while os.path.isfile(fileName):
        fileName = dirPath + "output_" + str(index) + ".mid"
        index = index + 1

    with open(fileName, 'wb') as binfile:
        MyMIDI.writeFile(binfile)

    