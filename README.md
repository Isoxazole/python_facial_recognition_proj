Bulk Photo Face Recognition
===

Overview
---

This project is meant to be able to gather a listing of images on a users computer, and given a known face, find images with similar faces.

The scripts run through the contents of the hard drive, from either root or specified location and extract the full path of each image. 
After this full path of images is found and written to a file, another script reads though files in.
Each file is individually loaded to be compared against the known face image. 
If the current image is a close enough match to the known image, its full path is saved to a file.
The end result is a text file with the full path of any/all images with similar faces as the known image.

This program was created with the idea that photographers with large, and potentially unorganized photosets, can still search for certain individuals.

This program uses OpenFace and face_recognition as the frameworks behind them. 
Both of these libraries work by analyzing the individual pixel values of a given image.
As such, this can be **EXTREMELY** taxing computationally. 

For large photo collections or collections with large files contained in it, it is recomended to use a GPU to improve performance.

---

Frameworks required:
---
	openface - recomend using Docker image (bamos/openface)  
	face_recognition

SETUP:
---
	Load OpenFace
		Pull Docker image "bamos/openface"
		`docker pull bamos/openface`
		OR
		Follow instructions here
			https://cmusatyalab.github.io/openface/setup/
	Run image
		`docker run -it bamos/openface bash`
	Load dependencies
		`pip install face_recognition`
	Load Program
		`git clone https://github.com/rjfitzg/PythonFinalProj.git`

Running the program:
---
	1. Take an image of your face. Make sure it is only your face in the image. To maximize accuracy, you should make sure there is good lighting and the image is front facing. 

	2. Move the image of your face to where the local project is. 
		ie. '~/Path/To/PythonFinalProj/known/'

	3. Rename the image of yourself to your name.
		ie. 'Riley_Fitz.jpg'

	4. Run the python project. 
	`python PythonFinalProj`

Examples:
```
python face_find.py # Searches from root

python face_find.py /path/to/directory # Searches given path if it exists
