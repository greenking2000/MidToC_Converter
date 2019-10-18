import mido
import FinalFile
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(dir_path)


def get_midi_file():
    """Get the name of the input file. Returns mido.midifiles.midifiles.MidiFile"""
    midi_file = str(parent_path + "\\" + input("Link to midi file\nFile should be in source root\n"))
    # Set default midi file
    if midi_file == str(parent_path + "\\"):
        midi_file = str(parent_path + "\\ELO - do ya.mid")
    # Determine if .mid needs appending or not
    try:
        if midi_file.upper()[-4:] == ".MID":
            song = mido.MidiFile(midi_file.upper())
            print("Loaded:\n" + midi_file + "\n")
            return song
        else:
            song = mido.MidiFile(str(midi_file.upper() + ".MID"))
            print("Loaded:\n" + midi_file + ".mid\n")
            return song
    except:
        print("Failed to find midi file\n"
              "Please input the exact name (Case does not matter)")
        get_midi_file()


def get_multi_tracks():
    """Ask whether multi tracks or single track"""
    multi_tracks = input("Do you want multiple tracks? Yes or No\n")
    if multi_tracks.upper() == "YES":
        multi_tracks = True
    elif multi_tracks.upper() == "NO":
        multi_tracks = False
    else:
        print("Please input either \"yes\" or \"no\". You will be asked for track number next")
        get_multi_tracks()
    return multi_tracks


#GO BACK AND EDIT
def get_oper_sys():
    print(os.name)
    """Check whether for arduino or windows"""
    oper_sys = input("Arduino or no?\n")
    return oper_sys


def get_pin():
    """Ask which is the output pin for arduino"""
    pin = input("Which is the output pin?\n")
    return  pin


