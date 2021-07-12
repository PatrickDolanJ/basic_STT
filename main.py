
import mic_vad_streaming as mvs
import argparse

activate = False

def update_words(words,activate):
    print(words)
    print(activate)
    if 'initialize' in words:
        print('what would you like to initialize?')
        activate=True
        print(activate)

    if 'claw' in words and activate==True:
        print(activate)
        print('--The Claw has been initialized--)')
        activate=False
        print(activate)

    return(activate)











parser = argparse.ArgumentParser(description="Stream from microphone to DeepSpeech using VAD")

parser.add_argument('-v', '--vad_aggressiveness', type=int, default=3,
                    help="Set aggressiveness of VAD: an integer between 0 and 3, 0 being the least aggressive about filtering out non-speech, 3 the most aggressive. Default: 3")
parser.add_argument('--nospinner', action='store_true',
                    help="Disable spinner")
parser.add_argument('-w', '--savewav',
                    help="Save .wav files of utterences to given directory")
parser.add_argument('-f', '--file',
                    help="Read from .wav file instead of microphone")

parser.add_argument('-m', '--model', required=True,
                    help="Path to the model (protocol buffer binary file, or entire directory containing all standard-named files for model)")
parser.add_argument('-s', '--scorer',
                    help="Path to the external scorer file.")
parser.add_argument('-d', '--device', type=int, default=None,
                    help="Device input index (Int) as listed by pyaudio.PyAudio.get_device_info_by_index(). If not provided, falls back to PyAudio.get_default_device().")
parser.add_argument('-r', '--rate', type=int, default=16000,
                    help=f"Input device sample rate. Default: {16000}. Your device may require 44100.")


vac_args = parser.parse_args(['-d','4','-m', 'deepspeech-0.9.3-models.pbmm'])
mvs.main(vac_args,words=update_words)








