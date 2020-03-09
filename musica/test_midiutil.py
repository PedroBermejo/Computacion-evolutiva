from midiutil import MIDIFile
import os.path


# Create a two-track file
MyMIDI = MIDIFile(10, adjust_origin=False)
MyMIDI.addTempo(0, 0, 30)

track = 0
time = 0
channel = 0
pitch = 60
duration = 1
volume = 100

for i in range(10):
    MyMIDI.addProgramChange(0, i, 0, i +20)
    MyMIDI.addNote(track + i, channel + i, pitch, time + i, duration, volume)

dirPath = "musica/output/"
fileName = "musica/output/output.mid"
i = 1
while os.path.isfile(fileName):
    fileName = dirPath + "output_" + str(i) + ".mid"
    i = i + 1

with open(fileName, 'wb') as binfile:
    MyMIDI.writeFile(binfile)