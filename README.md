## Proyecto de Reconocimiento Facial
Este proyecto contiene una serie de scripts diseñados para capturar imágenes de rostros, entrenar modelos de reconocimiento facial y probar el reconocimiento utilizando diferentes algoritmos.

## Descripción de los Scripts
1. capturandorostros.py
Este script te permite capturar imágenes de rostros desde un video o directamente desde la cámara. Las imágenes se utilizan para crear una base de datos que se empleará para entrenar los modelos de reconocimiento facial.

2. trainRF.py
El script trainRF.py se encarga de entrenar tres modelos diferentes de reconocimiento facial: EigenFaceRecognizer, Fisher y LGBH (Light Gradient Boosting Machine). Utiliza la base de datos creada con capturandorostros.py para el entrenamiento.

3. reconocimiento.py
El script reconocimiento.py permite probar el reconocimiento facial utilizando los modelos entrenados. Puedes seleccionar el modelo que deseas utilizar para el reconocimiento facial.

## Resultados de los Métodos de Reconocimiento Facial

A continuación, se presentan los resultados obtenidos al probar los modelos de reconocimiento facial entrenados. Los resultados se muestran en tablas para cada método utilizado.

### EigenFaces

En primer lugar se exponen los resultados obtenidos para el método eigenfaces trabajando con diferentes bases de datos de 10,100 y 400 imágenes.

| Base de datos | Tiempo de entrenamiento | Tiempo de ejecución | Exito    |
|---------------|-------------------------|---------------------|----------|
| 10 fotos      | 0.7346s                 | 0.1574s             | 100\%    |
| 100 fotos     | 3.832s                  | 2.320s              | 100\%    |
| 400 fotos     | 50.025s                 | 7.2466s             | 86.858\% |

Según estos resultados pareciera que el algoritmo funciona a la perfección, pero se realizó la misma prueba pero con otro vídeo con el entrenamiento de 10 fotos.

![test](https://github.com/GoyecheaAgustin/Face_recognition/assets/104398552/1232067a-93ce-4118-ac60-f68c1e97414b)

En este caso se identificó un error en la clasificación que generó un resultado incorrecto, está diciendo que Agustin es Sheldon Cooper lo cual, evidentemente, es incorrecto.

Es importante mencionar que los sistemas de reconocimiento facial pueden verse afectados por diversos factores, como la calidad de la imágenes de entrenamiento, la iluminación, la posición de la persona en la imagen, entre otros. A pesar de que se utilizan metodologías rigurosas para minimizar estos errores, es posible que se presenten casos en los que se produzcan falsos positivos (como en este caso) o falsos negativos

![test1](https://github.com/GoyecheaAgustin/Face_recognition/assets/104398552/edc3b910-e99c-4040-a56a-f4f49a0a32b8)

### Fisherfaces
Ahora  se exponen los resultados obtenidos para el método fisherfaces trabajando, también, con diferentes bases de datos de 10,100 y 400 imágenes.

| Base de datos | Tiempo de entrenamiento | Tiempo de ejecución | Exito    |
|---------------|-------------------------|---------------------|----------|
| 10 fotos      | 0.368s                  | 0.03291s            | 0\%      |
| 100 fotos     | 1.452s                  | 0.0421s             | 35.576\% |
| 400 fotos     | 77.44s                  | 0.0566s             | 76.923\% |


### Método LBPH

Se procede a mostrar los resultados obtenidos para el método LBPH (***Local Binary Pattern Histograms***). Nuevamente con un cuadro con los resultados con las diferentes bases de datos.

| Base de datos | Tiempo de entrenamiento | Tiempo de ejecución | Exito     |
|---------------|-------------------------|---------------------|-----------|
| 10 fotos      | 0.16s                   | 0.0658s             | 0\%       |
| 100 fotos     | 3.832s                  | 2.320s              | 32.692\%  |
| 400 fotos     | 6.41s                   | 4.5s                | 78.8461\% |


En general, se observa que el método fisherfaces es el que mayores ratios de éxito proporciona, por lo
que, a simple vista, se trata del más fiable. A pesar de esto, es el método que peor respuesta
proporciona al trabajar con un número de imágenes en training bajo (10 fotos) junto al Eigenfaces. En este sentido, el
método LBPH se trata del más estable, proporcionando una buena tasa de éxitos incluso con un
número bajo de imágenes en training. Esto, dicho con otras palabras, se puede expresar como que el
método fisherfaces es el que mayor exposición presenta al underfitting. 


Por lo que respecta al tamaño del archivo de training, resulta evidente que eigenfaces es el
que mayores recursos de memoria necesita, llegando a sobrepasar los 250 MB para 400 imágenes
en training. Los métodos LBPH y fisherfaces son los más eficaces, pero de entre ellos dos, fisherfaces se trata del método más óptimo en cuanto a uso de recursos
de memoria.

El mejor tiempo de ejecución de training es el del método LBPH, mientras que el que mayor
número de recursos consume en cuanto a tiempo es eigenfaces. LBPH presenta una tendencia lineal,
mientras que los otros dos métodos tienen una tendencia ligeramente exponencial. 

Hablando del tiempo de ejecución del test, fisherfaces es el mejor método. Además, cabe
destacar que para este método, el tiempo se mantiene constante a pesar de que el número de
imágenes en training aumente, de manera que solamente depende de la cantidad de imágenes que
hay bajo test. En el lado opuesto se encuentra el método eigenfaces, teniendo el peor tiempo de
ejecución del test.
