# Import needed packages
import face_recognition as fr

# Need to load file with locations of images on machine.

# Here is the code to make this project work.
# It needs to undergo a for loop for every known image we have.
# https://github.com/ageitgey/face_recognition/blob/master/examples/recognize_faces_in_pictures.py

# Load known and labeled image of person
known_face = fr.load_image_file("image")
known_face_enc = fr.face_encodings(known_face)[0] # If there is no face this will error. Need to validate it. Try catch?

# Create for loop for every line in txt document with a images location
for file_path in image_location_doc:

