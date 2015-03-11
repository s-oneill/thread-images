thread-images
=============

Automated image grabber for 4chan threads. Places all images of a thread into a
given directory.

Dependencies:

    wget

install:
    Place both of the files thread-images and images-file into a PATH directory (/usr/local/bin etc)
and call via CLI as follows:

    thread-images boards.4chan.org/<BOARD>/thread/<NUM>

    thread-images [DIRECTORY] boards.4chan.org/<BOARD>/thread/<NUM>

Files:

    thread-images -- Bash Script
    images-file  -- C++ Program
