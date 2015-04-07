thread-images
=============

Automated image grabber for 4chan threads. Places all images of a thread into a
given directory.

### Install

You have two choices:

1. Bash + C++
2. Python

Whichever, you choice. Place the contents of its folder
(ex thread-images/src/python) into a given PATH directory (ex /usr/local/bin)


### CLI

As these are just scripts, use them via CLI follows:

    thread-images boards.4chan.org/<BOARD>/thread/<NUM>

    thread-images [DIRECTORY] boards.4chan.org/<BOARD>/thread/<NUM>
### Dependencies

	wget
