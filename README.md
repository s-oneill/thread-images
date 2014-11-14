thread-images
=============

automated image grabber for 4chan threads

Goals:
    The ultimate goal of this project is to create a program that will be able
to take a given thread on 4chan and download all the images in that thread and
store them locally. 

Design:
    Our deisgn of this program is still in its infancy, the general idea will be
to use some method of retrieving the thread, whether it be downloading the
entire thread or parsing through the page using data mining techniques.
Analyzing the elements of the thread, we will identify files that have the
appropriate file extensions that we want to download (.gif, .png, .jpg, .webm,
etc). After identification we will retrieve the files themself, possibly through
the use of something like wget and place them in a local repository.
