from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


def get_augmentation_strategy():
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizonta_flip=True,
        fill_mode='nearest'
    )

    img=load_img('data/input_images/cardboard/cardboard1.jpg')
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i= 0
    for batch in datagen.flow(x, batch_size=1, save_to_dir='data/input_images', save_prefix='cap', save_format='jpeg'):
        i += 1
        if i > 20:
            break