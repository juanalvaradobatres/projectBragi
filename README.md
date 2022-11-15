# projectBragi
A project to automatically add captions to videos.

# Description
This project has a few moving parts that I need to tackle in order for it all to come together. 
- Use the Dropbox Python API to grab video files and download them
- Find a library to create a transcription from the audio of the video file
- Send the initial draft transcript to a Telegram bot with a link to edit/correct anything, changes sent back or approval sent back
- Approved transcription is turned into caption file with timestamps
- Use CLI based tool to apply captions to video file
- Export a low resolution sample of the video file for proofing
- Upon approval of proof, encode full quality video with captions
- Place captioned video in Dropbox folder again

Obviously, there are a few things I have to figure out, but I'll start with these tasks in order to move forward.
