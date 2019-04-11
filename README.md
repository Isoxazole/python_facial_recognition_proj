# PythonFinalProj
A collection of files for Python final project

Project is meant to be able to walk through the contents of an entire hard drive and make collections of viable images. After a collection of these images is cached, the images will be run through face_recognition to search for a desired face, a predetermined image to match.
This could be difficult for users with very large librarys of photos on a weak computer as the frameworks need a good amount of power to be run. Should work for both GPU and CPU.

This is meant to help photographers with large libraries of images to search for specified faces, using Openface/face_recognition as a backend.

Frameworks required:
	openface - recomend using Docker image (bamos/openface)
	face_recognition
