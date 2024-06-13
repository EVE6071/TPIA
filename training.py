import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import os


def train_model(data_path, epochs=10, learning_rate=0.001):
    # Charger les données d'entraînement
    train_data, val_data = load_data(data_path)

    # Définir le modèle
    model = Sequential([
        Dense(64, activation='relu', input_shape=(train_data.element_spec[0].shape[1],)),
        Dense(1, activation='sigmoid')
    ])

    # Compiler le modèle
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Entraîner le modèle
    model.fit(train_data, validation_data=val_data, epochs=epochs)

    # Sauvegarder le modèle entraîné
    model.save('model.h5')
    return model


def load_data(data_path):
    # Charger les données depuis data_path
    train_data = tf.keras.preprocessing.image_dataset_from_directory(
        data_path,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(256, 256),
        batch_size=32
    )

    val_data = tf.keras.preprocessing.image_dataset_from_directory(
        data_path,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(256, 256),
        batch_size=32
    )

    return train_data, val_data
