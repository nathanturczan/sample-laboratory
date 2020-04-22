###############################################################################
# sample_clerk
# a script that organizes audio samples into scale folders
# Nathan Turczan


# function for mapping note names to numbers [a, bf, c] = [9, 10, 0]
# this function taken from pretty midi and modified, removing the octave capture group
def note_name_to_number(note_name): 

	# Map note name to the semitone 
	pitch_map = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11} 
	# Relative change in semitone denoted by each accidental 
	acc_map = {'#': 1, 's': 1, '': 0, '♭': -1, 'f': -1,  '!': 0} 

	# Reg exp will raise an error when the note name is not valid 
	try: 
	    # Extract pitch, octave, and accidental from the supplied note name 
	    match = re.match(r'^(?P<n>[A-Ga-g])(?P<off>[#s♭f!]?)$', note_name)
	    pitch = match.group('n').upper() 
	    offset = acc_map[match.group('off')] 
	except: 
	    raise ValueError('Improper note format: {}'.format(note_name)) 

	# Convert from the extrated ints to a full note number 
	return (pitch_map[pitch] + offset) % 12

def update_sample_manifest():
	# this function updates samples_data.json in your main directory
	for sample in samples_dict:
		for note in samples_dict[sample]["note_names"]: 
			samples_dict[sample]["pitch_classes"].append(note_name_to_number(note)) 
			json.dumps()
			pprint.pprint(samples_dict) 

def normalize_all_samples():
	for filename in os.listdir(path):
		if filename.endswith(".wav"):
			raw = AudioSegment.from_file(filename, "wav")
			normalized = effects.normalize(raw)
			normalized.export(os.path.splitext(filename)[0]+"_normalized.wav", format="wav") 

def is_sample_subset_of_scale(scale, sample): 
    i = 0
    j = 0
    if len(scale) < len(sample) : 
        return 0
          
    scale.sort() 
    sample.sort() 
  
    while i < len(sample) and j < len(scale) : 
        if scale[j] < sample[i]: 
            j += 1
        elif scale[j] == sample[i]: 
            j += 1
            i += 1
        elif scale[j] > sample[i]: 
            return 0
    return False if i < len(sample) else True

def transpose_sample(sample, semitones):
	sound = AudioSegment.from_file(sample, format="wav") 
	new_sample_rate = int(sound.frame_rate * 2**((semitones)/12) ) 
	transposed_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate}) 
	transposed_sound = transposed_sound.set_frame_rate(44100) 
	transposed_sound.export(os.path.splitext(sample)[0]+"_transposed_by"+str(semitones)+'.wav', format='wav') 
	return os.path.splitext(sample)[0]+"_transposed_by"+str(semitones)+'.wav'


def transpose_pitch_classes(pitch_classes, semitones):
	transposed_pitch_classes = []
	for note in pitch_classes:
		note = (note+semitones) % 12
		transposed_pitch_classes.append(note)
	return transposed_pitch_classes


if __name__ == "__main__":

	# import libraries for audio manipulation, directory creation, and json read/write
	from pydub import AudioSegment, effects  
	import os
	import json
	import shutil
	import re

	# detect the current working directory and print it: "something/something/something/sample_laboratory"
	path = os.getcwd()
	print ("The current working directory is %s" % path)

	# load scale json
	with open(path+'/scales_data.json') as f: 
		scales_dict = json.load(f) 

	# create a folder for each scale
	for scale in scales_dict:
		os.makedirs("scales_dir/"+scale, exist_ok=True)

	# load sample json "manifest"
	with open(path+'/samples_data.json') as f: 
		samples_dict = json.load(f) 

	for sample in samples_dict:
		samples_dict[sample].update({"pitch_classes": []})
		for note in samples_dict[sample]["note_names"]:
			samples_dict[sample]["pitch_classes"].append(note_name_to_number(note))    

	# main forloop

	for sample_name in samples_dict:
		for scale_name in scales_dict:
			sample_path = path+"/samples/"+sample_name+".wav"
			# if the sample is a subset of the scale
			if is_sample_subset_of_scale(scales_dict[scale_name]['pitch_classes'], samples_dict[sample_name]['pitch_classes']):
				print("creating a shortcut to ", sample_path, "in ", "scales_dir/"+scale_name)
				# create a shortcut / alias / symbolic link to that sample in the scale folder
				os.symlink(sample_path, "scales_dir/"+scale_name+"/"+sample_name+".wav")
			for transposition in (-4, -3, -2, -1, +1, +2):
				transposed_sample = transpose_sample(sample_path, transposition)
				transposed_pitch_classes = transpose_pitch_classes(samples_dict[sample_name]['pitch_classes'], transposition)
				if is_sample_subset_of_scale(scales_dict[scale_name]['pitch_classes'], transposed_pitch_classes):
					print("creating a shortcut to ", transposed_sample, "in ", "scales_dir/"+scale_name)
					# create a shortcut / alias / symbolic link to that sample in the scale folder
					os.symlink(transposed_sample, "scales_dir/"+scale_name+"/"+sample_name+"_transposed_by"+str(transposition)+".wav")


