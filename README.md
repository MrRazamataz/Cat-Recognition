# Cat-Recognition
A python program that can recognise cats from a camera input, and can take pictures of them, sending them via a discord webhook.

## How to use:

* 1. Have all of the needed python pip packages installed (see `requirements.txt`).
* 2. Go into `config.json` and paste your discord webhook link in `discordwebhook`.
* 3. Start the script `main.py` and make sure a camera is connected to your computer correctly, otherwise it will give an error.
* 4. Show the *front* of a cat, it only scans for the front of the cat.  

It's the ESC key to exit the script.

## Knows issues:

Upon a picture taking, or the ESC key (anywhere that `cv2.destroyAllWindows()` appears in the code), the error (or warn, as it claims) ``anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback`` shows. This seems to be a bug with the cv2 libary, but it doesn't break anything so its fine to ignore.

## Credits:

All the actual hardwork was done by the people over at https://github.com/opencv/opencv , including the file that includes what a "cat" looks like (psst, `haarcascade_frontalcatface.xml`).