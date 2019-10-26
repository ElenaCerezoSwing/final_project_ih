# paths:
DATASET = 'images_dummies.csv'
ROOT_IMG = '../data/input_images/'
# img size:
ROW_IMAGES = 384
COL_IMAGES = 512
IMG_COLORS = 3
input_shape = (ROW_IMAGES, COL_IMAGES, IMG_COLORS)
# num of pictures:
PIC_NUM = 2527
# train-test parameters:
TRAIN_RATIO = 0.2
RANDOM_STATE = 42
# fit parameters:
BATCH_SIZE = 20
EPOCHS =10

COLUMNS = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
num_classes = len(COLUMNS)