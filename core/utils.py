from PIL import Image


def convert_image_to_greyscale(image_file):
    try:
        img = Image.open(image_file).convert('L')
        greyscale_name = "{0}_greyscale.{1}".format(
            image_file.name.split(".")[-2],
            image_file.name.split(".")[-1]
        ).split("/")[-1]
        path = "{0}/".format(image_file.path.rsplit("/", 1)[0])
        return img.save(path + greyscale_name)
    except Exception, e:
        raise e


def resize_image(image_file, height, width):
    try:
        img = Image.open(image_file).resize((height, width), Image.ANTIALIAS)
        resize_name = "{0}_resize.{1}".format(
            image_file.name.split(".")[-2],
            image_file.name.split(".")[-1]
        ).split("/")[-1]
        path = "{0}/".format(image_file.path.rsplit("/", 1)[0])
        return img.save(path + resize_name)
    except Exception, e:
        raise e
