###############################################################################
# creating project folder
# a script that organizes audio samples into scale folders
# Nathan Turczan


# function for mapping note names to numbers [a, bf, c] = [9, 10, 0]
# this function taken from pretty midi and modified, removing the octave capture group


def IntersecOfSets(folder1, folder2, folder3):  
    arr1 = os.listdir(folder1) 
    arr2 = os.listdir(folder2)  
    arr3 = os.listdir(folder3)  
     
    # Converting the arrays into sets  
    s1 = set(arr1)  
    s2 = set(arr2)  
    s3 = set(arr3)  
       
    # Calculates intersection of   
    # sets on s1 and s2  
    set1 = s1.intersection(s2)         #[80, 20, 100]  
       
    # Calculates intersection of sets  
    # on set1 and s3  
    result_set = set1.intersection(s3)  
       
    # Converts resulting set to list  
    final_list = list(result_set)  
    pprint.pprint(sorted(final_list))  

def find_samples_in_common(folder1, folder2): 
    samples_in_common = [] 
    for key1 in os.listdir(folder1): 
        for key2 in os.listdir(folder2): 
            if (key1 == key2): 
                samples_in_common.append(key1) 
    pprint.pprint(sorted(samples_in_common)) 


if __name__ == "__main__":

	import os
	import sys
	import shutil
	from pydub import AudioSegment, effects 

	# detect the current working directory and print it: "something/something/something/sample_laboratory"
	path = os.getcwd()
	print ("The current working directory is %s" % path)

	shared_samples = sys.argv[2]+'--'+sys.argv[3]
	scale_folder_1 = sys.argv[2]
	scale_folder_2 = sys.argv[3]

	#make project directory, samples in common folders, 
	os.makedirs(sys.argv[1]+'/'+shared_samples, exist_ok=True)
	os.makedirs(sys.argv[1]+'/'+scale_folder_1, exist_ok=True)
	os.makedirs(sys.argv[1]+'/'+scale_folder_2, exist_ok=True)

	for key1 in os.listdir(path+'/scales_dir/'+scale_folder_1): 
		for key2 in os.listdir(path+'/scales_dir/'+scale_folder_2): 
			if (key1 == key2):
				shutil.copyfile(path+'/scales_dir/'+scale_folder_1+'/'+key1, path+'/'+sys.argv[1]+'/'+shared_samples+'/'+key1)
			if (key1 != key2):
				shutil.copyfile(path+'/scales_dir/'+scale_folder_1+'/'+key1, path+'/'+sys.argv[1]+'/'+scale_folder_1+'/'+key1)
				shutil.copyfile(path+'/scales_dir/'+scale_folder_2+'/'+key2, path+'/'+sys.argv[1]+'/'+scale_folder_2+'/'+key1)
		#if filename.endswith(".wav"): 
		# beat = AudioSegment.from_file(filename, "wav") 
			# backwards = beat.reverse() 
			# backwards.export(path+'/'+sys.argv[1]+'/'+scale_folder_1+os.path.splitext(filename)[0]+"_reversed.wav", format="wav")  

	

