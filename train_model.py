import os
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers. normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator


def get_model_dir():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    model_dir = os.path.join(script_dir,'data','model')
    return os.path.normpath(model_dir)


def get_image_dir():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    image_dir = os.path.join(script_dir,'data','images')
    return os.path.normpath(image_dir)


def get_image_dir_for_class(image_class):
    class_dir = os.path.join(get_image_dir(),image_class)
    return os.path.normpath(class_dir)


def define_model(image_dim,num_channels,num_classes):
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(image_dim, image_dim, num_channels)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Conv2D(96, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model


def get_data_generators(image_dim,batch_size):
    image_dir=get_image_dir()
    data_generator = ImageDataGenerator(validation_split=0.2)
    train_generator = data_generator.flow_from_directory(image_dir, target_size=(image_dim, image_dim),
                                                         shuffle=True, seed=13,
                                                         class_mode='categorical', batch_size=batch_size,
                                                         subset="training")

    validation_generator = data_generator.flow_from_directory(image_dir, target_size=(image_dim, image_dim),
                                                         shuffle=True, seed=13,
                                                         class_mode='categorical', batch_size=batch_size,
                                                              subset="validation")
    return train_generator , validation_generator


num_channels = 3 #RGB images

image_dim = 100
batch_size = 32

train_generator , validation_generator = get_data_generators(image_dim,batch_size)

num_train_images=train_generator.samples
num_test_images=validation_generator.samples

print('Got generators')



model = define_model(image_dim,num_channels,train_generator.num_classes)

model.summary()

model.fit_generator(
        train_generator,
        epochs=5,
        validation_data=validation_generator)

model_dir = get_model_dir()
os.makedirs(model_dir,exist_ok=True)
model_file = os.path.join(model_dir,'trained_model.h5')
model.save()