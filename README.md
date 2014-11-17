thread-images
=============

automated image grabber for 4chan threads

How to use:
    Place both of the files thread-images and images-file into a PATH directory
and call the program as follows:

    thread-images boards.4chan.org/<BOARD>/thread/<NUM>

    thread-images [DIRECTORY] boards.4chan.org/<BOARD>/thread/<NUM>

The output directory will be the current working directory.

Files:

    thread-images -- Bash Script
    images-file  -- C++ Program

Dependencies

    wget
    gcc compiler

Design:
    This program uses a combination of bash scripting and a C++ program. When
called with a thread url as a CLI argument, the bash script will wget the raw
HTML from the thread and pass that file into the C++ program. The C++ program
searches the HTML for a marker of image URLs, it then singles them out and
removes any duplicates. The resulting image URLs are outputted into a temporary
file containing the URLs. The bash script then takes that file with the image
URLs and wgets them all into the directory.


