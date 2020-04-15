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
	return pitch_map[pitch] + offset 

def update_sample_manifest():
	# this function updates samples_data.json file in your main directory
	for chord in samples_dict:
		for note in samples_dict[chord]["note_names"]: 
			samples_dict[chord]["pitch_classes"].append(note_name_to_number(note)) 
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
	transposed_sound = lopitch_sound.set_frame_rate(44100) 
	transposed_sound.export(os.path.splitext(filename)[0]+"_"+semitones+'.wav', format='wav') 

def file_sample_in_correct_folder():
	# compare every sample to every scale with is_sample_subset_of_scale()
	for sample, scale in itertools.combinations(????):
	        if is_sample_subset_of_scale(sample, scale) == True:
	        	# if true, 
	    return scales_dict




if __name__ == "__main__":

	# import libraries for audio manipulation, directory creation, and json read/write
	from pydub import AudioSegment, effects  
	import os
	import json

	# detect the current working directory and print it: "something/something/something/sample_laboratory"
	path = os.getcwd()
	print ("The current working directory is %s" % path)

	#load scale json
	with open('/Users/NathanAT/sample_laboratory/scale_data.json') as f: 
		scales_dict = json.load(f) 

	#create a folder for each scale
	for scale in scale_dict:
		try: 
			os.mkdir(scale) 
		except OSError: 
			print ("Creation of the directory %s failed" % scale) 
		else: 
			print("Successfully created the directory %s " % scale) 


	#load sample json "manifest"

	with open('/Users/NathanAT/sample_laboratory/samples.json') as f: 
		samples_dict = json.load(f) 

