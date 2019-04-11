# Import needed packages
import face_recognition as fr

# Load file with image directories.
with open("img_paths.txt") as f:
	file_locs = f.readlines()
file_locs = [x.strip() for x in file_locs]

# Load known face to test off of. Working from lfw dataset.
known_face = fr.load_image_file("/root/Data/known/Tim_Allen_0001.jpg")
known_face_enc = fr.face_encodings(known_face)[0] # This can error out if no face is in image

# Create variable for file location, this should not be needed in final implementation
work_dir = "/root/Data/unknown/"

# Here is the code to make this project work.
# It needs to undergo a for loop for every known image we have.
# https://github.com/ageitgey/face_recognition/blob/master/examples/recognize_faces_in_pictures.py
for file_loc in file_locs:
	print(file_loc)
	curr_test_img = work_dir + file_loc
	unk_face = fr.load_image_file(curr_test_img)
	unk_face_enc = fr.face_encodings(unk_face)[0]
	result = fr.compare_faces([known_face_enc], unk_face_enc)
	print(result)
