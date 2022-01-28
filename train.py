from collections import Counter
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import AveragePooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import numpy as np
import charts as ch
import resourcesImport as ri
from sklearn.utils import class_weight

# inicijalizacija stope učenja, broja epoha i veličine batcha
INIT_LR = 1e-4
EPOCHS = 30
BS = 32

(labels, data) = ri.get_labels_and_data()
categories = Counter(labels).keys()
values = list(Counter(labels).values())

# # grafici
# barchart
ch.plot_barchart(categories, values, 'Distribution of different labels in dataset', 'Labels', 'Number',
                 'barchart_data_plot')

# pie chart
ch.plot_pie_chart(categories, values, 'Distribution of different labels in dataset', 'pie_chart_data_plot',
                  colors=['lightpink', 'mediumorchid', 'plum'])

# priprema podataka i labela za treniranje
lb = LabelBinarizer()
labels = lb.fit_transform(labels)
data = np.array(data, dtype="float32")
labels = np.array(labels)
# test size 20% of data set
(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.20, stratify=labels,  random_state=42)
class_weights = class_weight.compute_class_weight(
                                        class_weight="balanced",
                                        classes=np.unique(lb.inverse_transform(trainY)),
                                        y=lb.inverse_transform(trainY)
                                    )

class_weights = dict(enumerate(class_weights))
print(class_weights)

aug = ImageDataGenerator(rotation_range=20, zoom_range=0.15, width_shift_range=0.2, height_shift_range=0.2,
                         shear_range=0.15, horizontal_flip=True, fill_mode="nearest")

baseModel = MobileNetV2(weights="imagenet", include_top=False, input_tensor=Input(shape=(224, 224, 3)))
headModel = baseModel.output
headModel = AveragePooling2D(pool_size=(7, 7))(headModel)
headModel = Flatten(name="flatten")(headModel)
headModel = Dense(128, activation="relu")(headModel)
headModel = Dropout(0.5)(headModel)
headModel = Dense(3, activation="softmax")(headModel)
model = Model(inputs=baseModel.input, outputs=headModel)

for layer in baseModel.layers:
    layer.trainable = False

print("[INFO] compiling model...")
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

print("[INFO] training head...")
history = model.fit(aug.flow(trainX, trainY, batch_size=BS), steps_per_epoch=len(trainX) // BS, validation_data=(testX, testY),
                    validation_steps=len(testX) // BS, epochs=EPOCHS, class_weight=class_weights)

print("[INFO] evaluating network...")
predIdxs = model.predict(testX, batch_size=BS)

predIdxs = np.argmax(predIdxs, axis=1)

print(classification_report(testY.argmax(axis=1), predIdxs,
                            target_names=lb.classes_))

results = model.evaluate(testX, testY)
print(results)

print("[INFO] saving mask detector model...")
model.save("FaceMaskDetection.model", save_format="h5")

acc = history.history['accuracy']
loss_values = history.history['loss']
val_loss_values = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig(r'.\Resources\charts\final_training_and_validation_loss_c2.png')
plt.show()

plt.clf()
acc_values = history.history['accuracy']
val_acc_values = history.history['val_accuracy']
plt.plot(epochs, acc_values, 'bo', label='Training acc')
plt.plot(epochs, val_acc_values, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig(r'.\Resources\charts\final_training_and_validation_accuracy_c2.png')
plt.show()

