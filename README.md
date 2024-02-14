###Proyecto de Reconocimiento Facial
Este proyecto contiene una serie de scripts diseñados para capturar imágenes de rostros, entrenar modelos de reconocimiento facial y probar el reconocimiento utilizando diferentes algoritmos.

###Descripción de los Scripts
1. capturandorostros.py
Este script te permite capturar imágenes de rostros desde un video o directamente desde la cámara. Las imágenes se utilizan para crear una base de datos que se empleará para entrenar los modelos de reconocimiento facial.

2. trainRF.py
El script trainRF.py se encarga de entrenar tres modelos diferentes de reconocimiento facial: EigenFaceRecognizer, Fisher y LGBH (Light Gradient Boosting Machine). Utiliza la base de datos creada con capturandorostros.py para el entrenamiento.

3. reconocimiento.py
El script reconocimiento.py permite probar el reconocimiento facial utilizando los modelos entrenados. Puedes seleccionar el modelo que deseas utilizar para el reconocimiento facial.
