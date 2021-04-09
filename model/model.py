from PIL import Image
import time


def init():
    """
    This method will be run once on startup. You should check if the supporting files your
    model needs have been created, and if not then you should create/fetch them.
    """
    # Placeholder init code. Replace the sleep with check for model files required etc...
    time.sleep(1)


def predict(image_file_name):
    """
    Interface method between model and server. This signature must not be
    changed and your model must be able to create a prediction from the image
    file that is passed in via the filename.

    Note: All images are stored in the directory '/app/images/' in the Docker container. You may assume that the file
    name that is passed to this method is valid and that the image file exists.

    Example code for opening the image using PIL:
    image = Image.open('/app/images/'+image_file_name)
    """

    image = Image.open('/app/images/'+image_file_name)

    return {
        'classes': ['isGreen', 'isRed'],  # List every class in the classifier
        'result': {  # For results, use the class names above with the result value
            'isGreen': 0,
            'isRed': 1
        }
    }
