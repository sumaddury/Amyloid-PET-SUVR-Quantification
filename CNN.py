"""
Code for Convolutional Neural Network
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten, GlobalMaxPooling2D
from tensorflow.keras.optimizers import Adam

from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.applications.resnet_rs import ResNetRS50
from tensorflow.keras.applications.efficientnet_v2 import EfficientNetV2B3
from tensorflow.keras.applications.efficientnet_v2 import EfficientNetV2S

import warnings
warnings.filterwarnings("ignore")

# The SUVR value used was SUMMARYSUVR_WHOLECEREBNORM

delim = '-----'

labels = pd.read_csv('...\\Full Set\\AllAmyloidTarget.csv')

def load_train(path, shuffle):
    
    # Train
    
    labels = pd.read_csv('...\\Full Set\\AllAmyloidTarget.csv')
    train_datagen = ImageDataGenerator(validation_split=0.2, rescale=None)
    train_gen_flow = train_datagen.flow_from_dataframe(
        dataframe=labels,
        directory='...\\Full Set\\AllAmyloidProcessedRGBV2\\',
        x_col='ID',
        y_col='Value',
        target_size=(224, 224),
        batch_size=32,
        class_mode='raw',
        subset = 'training',
        seed=1234,
        shuffle=shuffle)

    return train_gen_flow


def load_test(path, shuffle):
    
    # Validation/Test

    labels = pd.read_csv('...\\Full Set\\AllAmyloidTarget.csv')
    validation_datagen = ImageDataGenerator(validation_split=0.2, rescale=None)
    test_gen_flow = validation_datagen.flow_from_dataframe(
    dataframe = labels,
    directory='...\\Full Set\\AllAmyloidProcessedRGBV2\\',
    x_col="ID",
    y_col="Value", 
    class_mode="raw", 
    target_size=(224,224), 
    batch_size=32,
    subset = "validation",
    seed=1234,
    shuffle=shuffle
    )

    return test_gen_flow

def create_model(input_shape):
    
    # EfficientNetV2 Small was used due to VRAM limitations. Very slight improvements may be possible with EfficientNetV2 Large or more powerful networks
    backbone = EfficientNetV2S(input_shape=input_shape, weights='imagenet', include_top=False)
    model = Sequential()
    model.add(backbone)
    
    # We add a Dropout layer to prevent overfitting
    model.add(Dropout(0.5))

    # Average pooling makes the most sense for regression
    model.add(GlobalAveragePooling2D())
    
    # Full connected linear downsample layer
    model.add(Dense(1, activation='linear'))

    # Adam was used to optimize
    optimizer = Adam(learning_rate=0.0003)

    # Mean squared loss was not used as it punishes overestimation more than underestimating, which doesn't make sense for this projec
    model.compile(optimizer=optimizer, loss='mae', metrics=['mae'])
    print(model.summary())

    return model

def train_model(model, train_data, test_data, batch_size=32, epochs=60,
                steps_per_epoch=None, validation_steps=None):

    # Training
    history = model.fit(train_data, validation_data=test_data, batch_size=batch_size, 
              epochs=epochs, steps_per_epoch=steps_per_epoch, 
              validation_steps=validation_steps, verbose=2)

    # Get training and test loss histories
    training_loss = history.history['loss']
    test_loss = history.history['val_loss']


    epoch_count = range(1, len(training_loss) + 1)

    # Visualize Epoch vs Loss
    plt.plot(epoch_count, training_loss, 'r--')
    plt.plot(epoch_count, test_loss, 'b-')
    plt.legend(['Training Loss', 'Test Loss'])
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.show();

    return model

path = '...\\Full Set\\'

# Load training and testing
train_data = load_train(path, False)
test_data = load_test(path, False)

# Build a model
model = create_model(input_shape = (224, 224, 3))

# Train the model
model = train_model(model, train_data, test_data)

# Save the model

path = "...\\SavedModel\\"
model.save(path + '\\EffNetV2SModel.h5')
model.save_weights(path + '\\EffNetV2SWeights.h5')

print(delim)
