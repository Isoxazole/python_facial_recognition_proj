# Import needed packages
import face_recognition as fr


def face_rec():
	# Load variables
	known_face_load = False
	count = 0

	# Load file with image directories.
	with open("img_paths.txt") as f:
		file_locs = f.readlines()
	file_locs = [x.strip() for x in file_locs]

	# Create file where recognized faces will go
	known_face_file = open("Recognized_Faces_Location.txt", "w+")

	# Get full path to user known image
	
	while not (known_face_load):
		known_face_loc = raw_input("Please enter the full path of the known face to be found:\n")
		# Load known face to test off of. Working from lfw dataset.
		try:
			known_face = fr.load_image_file(known_face_loc)
			known_face_enc = fr.face_encodings(known_face)[0] 
			known_face_load = True
		except:
			print('There was an error loading the known face. \n Check the path and that the image has a face.\nTry again..')

	# Here is the code to make this project work.
	# It needs to undergo a for loop for every known image we have.
	# https://github.com/ageitgey/face_recognition/blob/master/examples/recognize_faces_in_pictures.py
	for file_loc in file_locs:
		try:
			unk_face = fr.load_image_file(file_loc)
			unk_face_enc = fr.face_encodings(unk_face)[0]
			result = fr.compare_faces([known_face_enc], unk_face_enc)
		except:
			# No face was found in file.
			# Or error loading file..
			print('NO FACES WERE FOUND HERE')
		if (result == [True]):
			known_face_file.write(file_loc)
			count += 1
			print("MATCH: %s" % file_loc)
	known_face_file.close()
	return known_face_file, count

if __name__=="__main__":
    face_rec()