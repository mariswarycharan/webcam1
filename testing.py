# import required libraries
from vidgear.gears import CamGear
import cv2
import streamlit as st

# set desired quality as 720p
options = {"STREAM_RESOLUTION": "720p"}

# Add any desire Video URL as input source
# for e.g https://vimeo.com/151666798
# and enable Stream Mode (`stream_mode = True`)
stream = CamGear(
    source=0,
    stream_mode=False,
    logging=True,

).start()
ii = st.image([])
# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # Show output window
    ii.image(frame)

# safely close video stream
stream.stop()
