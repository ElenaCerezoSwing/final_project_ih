from keras.models import Sequential
from keras.layers import ConV2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

model = Sequential()

# first we make a model that outputs 3D feature maps (height, width and features)
model.add(ConV2D(32, (3,3), input_shape=(3, 150, 150)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(ConV2D(32, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(ConV2D(32, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

# the we convert 3D feature maps to 1D feature vectors
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# now, we prepare our data

batch_size = 16
# augmentation configuration for training data
train_datagen = ImageDataGenerator (resclae=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

# augmentation configuration for testing fata (only rescaling)
test_datagen = ImageDataGenerator(rescale=1./255)

# this part of the code is a generator that read pictures found in subfolders of 'data/input_images',
# and indefinetely generate batches of augmented image data

train_generator = train_datagen.flow_from_directory('data/input_images', target_size=(150, 150), batch_size=batch_size, class_mode='binary')

# and the same for validation
valdation_generator = train_datagen.flow_from_directory('data/validation', target_size=(150, 150), batch_size=batch_size, class_mode='binary')


model.fit_generator(
    train_generator,
    steps_per_epoch=2000 // batch_size,
    epochs=50,
    validation_data=valdation_generator,
    validation_steps=800 // batch_size)
model.save_weights('first_try.h5')


