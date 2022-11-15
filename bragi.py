#   Project Bragi
#
# This project will take the Scriptable Unix based video transcription. On my Plex server, 
# create a (virtual machine? docker container? listener?). Robert posts a dropbox link. 
# When that happens, I get a notification on Telegram (bot creation), and a script kicks off.
# The script will take the Dropbox URL, download the video, automatically create a transcription from the audio, 
# and send it to a web interface for proofreading/editing. 
# Once I make my edits, send it back to the program, and have it generate timestamps and apply captions. 
# Once captions are applied, a low quality, low resolution proof is created. 
# Then, a Telegram bot sends me the proof. If everything looks good, 
# then I can upload the video to an FTP server, 
# or to an SFTP server where Robert can access them.

# First, take the Dropbox URL and download a video to a point
