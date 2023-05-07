from goprocam import GoProCamera, constants
import time

# Get GoPro camera information
gopro = GoProCamera.GoPro(constants.gpcontrol)
#gopro.overview()

for i in range(10):
    time.sleep(5)
    # Take Image
    gopro.take_photo()
