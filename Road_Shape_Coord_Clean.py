# This is to extract the coordinates from geometry.coordinates column after cleaning
def coord_clean(x):
    x = str(x)
    x = x.split('[')[2:]
    x = str(x).replace("['", "")
    x = x.replace("]", "")
    x = x.replace(" ',", "")
    x = x.replace(" '", "")
    x = x.replace("'", "")
    coords = x.split(',')

    return coords