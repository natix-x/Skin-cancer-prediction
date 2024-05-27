import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf
from sklearn.metrics import classification_report


def plot_loss_accuracy_curves(history):
    """
  Returns separate loss and accuracy curves for training and validation metrics.
  """
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    accuracy = history.history['accuracy']
    val_accuracy = history.history['val_accuracy']

    epochs = range(len(history.history['loss']))

    # Plot loss
    plt.plot(epochs, loss, label='training_loss')
    plt.plot(epochs, val_loss, label='val_loss')
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.legend()

    # Plot accuracy
    plt.figure()
    plt.plot(epochs, accuracy, label='training_accuracy')
    plt.plot(epochs, val_accuracy, label='val_accuracy')
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.legend();


def evaluation_metrics(model, test_data, y_test, class_names):
    """
    plots confusion matrix and print classification report
    :param model: model to be evaluated
    :param test_data: X_test
    :param y_test: y_test
    :param class_names: names of the classes in model
    :return: heatmap of confusion matrix and classification report
    """
    y_predict = model.predict(test_data)
    y_pred = np.argmax(y_predict, axis=-1)
    y_true = np.argmax(y_test, axis=-1)
    confusion_matrix = tf.math.confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_matrix, annot=True, fmt='d', cbar=False)

    # Set x-axis labels to class names
    plt.xticks(ticks=np.arange(len(class_names)) + 0.5, labels=class_names, rotation=45, ha='center')
    # Set y-axis labels to class names
    plt.yticks(ticks=np.arange(len(class_names)) + 0.5, labels=class_names, rotation=0, va='center')

    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title('Confusion Matrix')
    plt.show()
    print(classification_report(y_true, y_pred, target_names=class_names))