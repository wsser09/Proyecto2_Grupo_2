# https://youtu.be/NJpS-sFGLng
"""
Live prediction of emotion, age, and gender using pre-trained models. 
Uses haar Cascades classifier to detect face..
then, uses pre-trained models for emotion, gender, and age to predict them from 
live video feed. 
Prediction is done using tflite models. 
Note that tflite with optimization takes too long on Windows, so not even try.
Try it on edge devices, including RPi. 
"""

import os
import cv2
import time
import sys
import numpy as np
from datetime import datetime
import tflite_runtime.interpreter as tf

################ Programa ##############
mst=float(sys.argv[1])

##########---------- Estadísticas -----------############
def txtPorcentaje(emocion,cantidad, porcentaje):
    # dd_mm_YY___h_m_s
    now = datetime.now()
    array = []
    array = [str(emocion),str(cantidad), 'Porcentaje = ',str(porcentaje)]
    with open(Estadisticas, 'a') as f:
        f.write(' '.join(array))
        f.write('\n')

def txtTotal(emocion, dt_string):
    # dd_mm_YY___h_m_s
    now = datetime.now()
    Emociones_time= now.strftime("%H_%M_%S ")
    array = []
    array = [Emociones_time,emocion]
    with open(Emociones, 'a') as f:
        f.write(' '.join(array))
        f.write('\n')

def printporcentajes(emociones):
    print('-----------------------------------------------')
    print('Estadistica de las emociones detectadas: \n \n')
    directorio = {i:emociones.count(i) for i in emociones}
    suma_emociones = sum(list(directorio.values()))
    for i in list(directorio.keys()):
        print (i, directorio.get(i), 'Porcentaje = ', 100*(directorio.get(i) /suma_emociones))
        txtPorcentaje(i, directorio.get(i), 100*(directorio.get(i) /suma_emociones))
    print('----------------------------------------------- \n')

########################################

face_classifier=cv2.CascadeClassifier('haarcascades_models/haarcascade_frontalface_default.xml')


#### PREDICT USING tflite ###

# Load the TFLite model and allocate tensors.
emotion_interpreter = tf.Interpreter(model_path="emotion_detection_model_200epochs_no_opt.tflite")
emotion_interpreter.allocate_tensors()


# Get input and output tensors.
emotion_input_details = emotion_interpreter.get_input_details()
emotion_output_details = emotion_interpreter.get_output_details()

# Test the model on input data.
emotion_input_shape = emotion_input_details[0]['shape']

class_labels=['Angry','Disgust', 'Fear', 'Happy','Neutral','Sad','Surprise']


cap=cv2.VideoCapture(0)
#####################################
emociones = []
if os.path.isdir('./resultado/'):
    pass    
else:
    os.mkdir('./resultado/')


now= datetime.now()
Estadisticas = './resultado/Stat_'+ now.strftime("%H_%M_%S__%d_%m_%Y")+'.txt'
Emociones = './resultado/Total_'+ now.strftime("%H_%M_%S__%d_%m_%Y")+'.txt'
####################################
while True:
    ret,frame=cap.read()
    labels=[]
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_gray=cv2.resize(roi_gray,(48,48))/255

        #Get image ready for prediction
        roi= np.array(roi_gray, dtype=np.float32).reshape(-1,48,48,1)
        #roi=roi_gray.astype('float')/255.0  #Scale
        #roi=img_to_array(roi)
        #roi=np.expand_dims(roi,axis=0)  #Expand dims to get it ready for prediction (1, 48, 48, 1)
        
        emotion_interpreter.set_tensor(emotion_input_details[0]['index'], roi)
        emotion_interpreter.invoke()
        emotion_preds = emotion_interpreter.get_tensor(emotion_output_details[0]['index'])

        #preds=emotion_model.predict(roi)[0]  #Yields one hot encoded result for 7 classes
        emotion_label=class_labels[emotion_preds.argmax()]  #Find the label
        emotion_label_position=(x,y)
        
        
        cv2.putText(frame,emotion_label,emotion_label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        
        #####################################
        print(emotion_label)
        emociones.append(emotion_label)
        txtTotal(emotion_label,Emociones)
       
    cv2.imshow('Emotion Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):  #Press x to exit
        break
        
printporcentajes(emociones)
       
cap.release()
cv2.destroyAllWindows()


##############################
