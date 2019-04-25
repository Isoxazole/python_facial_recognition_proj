# Import needed packages
import face_recognition as fr


def face_rec():
	# Load file with image directories.
	with open("img_paths.txt") as f:
		file_locs = f.readlines()
	file_locs = [x.strip() for x in file_locs]

	# Load known face to test off of. Working from lfw dataset.
	try:
		known_face = fr.load_image_file("/root/PythonFinalProj/known/Tim_Allen_0001.jpg")
		known_face_enc = fr.face_encodings(known_face)[0] 
	except:
		#import os; os.system('exit')
		print('There was an error loading your known face')

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
			print("MATCH: %s" % file_loc)

if __name__=="__main__":
    face_rec