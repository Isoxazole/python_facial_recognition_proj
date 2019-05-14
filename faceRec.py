# Import needed packages
import face_recognition as fr


def face_rec(picture_path=""):
	# Load variables
	known_face_load = False
	count = 0


	# Load file with image directories.
	with open("img_paths.txt") as f:
		file_locs = f.readlines()
	file_locs = [x.strip() for x in file_locs]

	# Create file where recognized faces will go
	known_face_file = open("Recognized_Faces_Location.txt", "w+")

	# make this not a local variable when used in the later nested for loops (make sure it's in a bigger scope)
	known_face_enc = ""

	# Get full path to user known image
	while not (known_face_load):
		if picture_path == "":
			known_face_loc = raw_input("Please enter the full path of the known face to be found:\n")
		else:
			known_face_loc = picture_path
		# Load known face to test off of. Working from lfw dataset.
		try:
			known_face = fr.load_image_file(known_face_loc)
			known_face_enc = fr.face_encodings(known_face)[0] 
			known_face_load = True # Set variable confirm sucessful setting.
		except:
			print('There was an error loading the known face. \n Check the path and that the image has a face.\nTry again..')

	# Here is the code to make this project work.
	# It needs to undergo a for loop for every known image we have.
	# https://github.com/ageitgey/face_recognition/blob/master/examples/recognize_faces_in_pictures.py
	for file_loc in file_locs:
		unk_img = fr.load_image_file(file_loc)
		unk_img_enc = fr.face_encodings(unk_img)
		for i in range(len(unk_img_enc)):
			result = fr.compare_faces([known_face_enc], unk_img_enc[i]) 
			# If there is a True result, no need to search image further.
			if ([True] in result):
				known_face_file.write(file_loc + "\n")
				count += 1
				print("MATCH: %s" % file_loc)
				break
	# Finished searching, close file.
	known_face_file.close()
	return known_face_file, count

if __name__=="__main__":
	face_rec()
