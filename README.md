# PythonFinalProj
A collection of files for Python final project

Project is meant to be able to walk through the contents of an entire hard drive and make collections of viable images. After a collection of these images is cached, the images will be run through face_recognition to search for a desired face, a predetermined image to match.
This could be difficult for users with very large librarys of photos on a weak computer as the frameworks need a good amount of power to be run. Should work for both GPU and CPU.

This is meant to help photographers with large libraries of images to search for specified faces, using Openface/face_recognition as a backend.

Frameworks required:
	openface - recomend using Docker image (bamos/openface)
	face_recognition

SETUP:
	Load OpenFace
		Pull Docker image "bamos/openface"
		OR
		Follow instructions here
			https://cmusatyalab.github.io/openface/setup/
	Run image
		docker run -it bamos/openface bash
	Load dependencies
		pip install face_recognition
	Load Program
		git clone https://github.com/rjfitzg/PythonFinalProj.git

Running the program:
	1. Take an image of your face. Make sure it is only your face in the image. To maximize accuracy, you should make sure there is good lighting and is front facing. 

	2. Move the image of your face to where the local project is. 
		ie. '~/Path/To/PythonFinalProj/known/'

	3. Rename the image of yourself to your name.
		ie. 'Riley_Fitz.jpg'

	4. Run the python project. 
		python PythonFinalProj

		NOTE: Running the code snippet above will search the entire hard drive from root or C:/. To only search a certain directory, run..
		python PythonFinalProj ~/Path/To/Directory/