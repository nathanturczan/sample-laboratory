###############################################################################
# reverse all 
# Nathan Turczan


# function for mapping note names to numbers [a, bf, c] = [9, 10, 0]
# this function taken from pretty midi and modified, removing the octave capture group




if __name__ == "__main__":

	import os
	from pydub import AudioSegment, effects 

	# detect the current working directory and print it: "something/something/something/sample_laboratory"
	path = os.getcwd()
	print ("The current working directory is %s" % path)


