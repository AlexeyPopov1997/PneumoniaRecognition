# Pneumonia Recognition
#### Простое настольное приложение для определения области поражения легких при пневмонии на флюорографических снимках.

Приложение выполнено в рамках курса **Интеграция данных в информационных системах** в качестве курсового проекта по направлению **Image Recognition**.

При создании модели для определения пневмонии использовалась модель **[Mask R-CNN](https://github.com/matterport/Mask_RCNN)**. 

Реализация нашей модели и ее описание находится в здесь **[model/PneumoniaDetection.ipynb](https://github.com/AlexeyPopov1997/PneumoniaRecognition/blob/main/model/PneumoniaDetection.ipynb)**.

![readme](https://github.com/AlexeyPopov1997/PneumoniaRecognition/blob/main/figures/readme.gif?raw=true)

### Создание и установка виртуальной среды
1. Я предлагаю создать виртуальное огружегие, используя файл **[environment.yml](https://github.com/AlexeyPopov1997/PneumoniaRecognition/blob/main/environment.yml)** (**Не забудьте изменить `prefix` в файле!**):
```sh
conda env create -f environment.yml
```
Первая строка файла `environment.yml` устанавливает имя окружения.

2. Активируйте новое окружение:

```sh
conda activate PneumoniaRecognition
```

3. Убедитесь, что окружение было установлено правильно:

```sh
conda env list
```
***

4. Запустите приложение:
```sh
python main.py
```
***

**Используемые материалы**
1. [Mask-RCNN and COCO transfer learning LB:0.155](https://www.kaggle.com/hmendonca/mask-rcnn-and-coco-transfer-learning-lb-0-155)
2. [R-CNN – Neural Network for Object Detection and Semantic Segmentation](https://neurohive.io/en/popular-networks/r-cnn/)
3. [The complete PyQt5 tutorial — Create GUI applications with Python](https://www.learnpyqt.com/)