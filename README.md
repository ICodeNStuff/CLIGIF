# CLIGIF
## Render GIFs and images in the command line with python.
### Does not support all terminals, and there may be some slight bugs.
### quality_mp changes the quality, auto_adjust centers the feed according to the terminal width, and respect framerate should be on for an accurate video, char changes the character that is used as a pixel
### use repeat_times = -1 to loop the gif forever

# Installing: pip install cligif
# Usage:
### For images:
    
_ = ImageObj(filename=-string-, char=-character-, quality_mp=-int-, brightness=-int-, auto_adjust=-boolean-)

_.render() # returns -1 on failure

### For GIFs:

_ = GifObj(filename=-string>, char=-character-, quality_mp=-int-, brightness=-int-, auto_adjust=-boolean-, additional_text=-string-, repeat_times=-int-, respect_framerate=-boolean-)

_.render() # returns -1 on failure



