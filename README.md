# Pneumonia Recognition
#### Простое настольное приложение для определения области поражения легких при пневмонии на флюорографических снимках.

Приложение выполнено в рамках курса **Интеграция данных в информационных системах** в качестве курсового проекта по направлению **Image Recognition**.

При создании модели для определения пневмонии использовалась модель **[Mask R-CNN](https://github.com/matterport/Mask_RCNN)**. 

Реализация нашей модели и ее описание находится в здесь **[model/PneumoniaDetection.ipynb](https://github.com/AlexeyPopov1997/PneumoniaRecognition/blob/main/model/PneumoniaDetection.ipynb)**.

![readme](https://github.com/AlexeyPopov1997/PneumoniaRecognition/blob/main/figures/readme.gif?raw=true)

### Создание и установка виртуальной среды
1. Так как GitHub не позволяет пушить файлы размером более 100 МБ, для работы с приложением я предлагаю клонировать репозиторий себе на машину:
```sh
git clone https://github.com/AlexeyPopov1997/PneumoniaRecognition.git
```
2. Скачать модель по ссылке
**[pneumonia20201217T0225](https://drive.google.com/drive/folders/1d8gfDlsQd6GB01qbXbT_fk2c9JP4mR6e?usp=sharing)**
   и скопировать модель в папку **[model/working/pneumonia20201217T0225](https://github.com/AlexeyPopov1997/PneumoniaRecognition/tree/main/model/working/pneumonia20201217T0225)**

***
*При желании, вы без труда можете создать свою модель, воспользовавшись **[model/PneumoniaDetection.ipynb](https://github.com/AlexeyPopov1997/PneumoniaRecognition/blob/main/model/PneumoniaDetection.ipynb)***
***

3. Далее создайте виртуальное окружение, используя файл **[environment.yml](https://github.com/AlexeyPopov1997/PneumoniaRecognition/blob/main/environment.yml)** (**Не забудьте изменить `prefix` в файле!**):
```sh
conda env create -f environment.yml
```
Первая строка файла `environment.yml` устанавливает имя окружения.

4. Активируйте новое окружение:

```sh
conda activate PneumoniaRecognition
```

5. Убедитесь, что окружение было установлено правильно:

```sh
conda env list
```

6. Запустите приложение:
```sh
python main.py
```
***

**Используемые материалы**
1. [Mask-RCNN and COCO transfer learning LB:0.155](https://www.kaggle.com/hmendonca/mask-rcnn-and-coco-transfer-learning-lb-0-155)
2. [R-CNN – Neural Network for Object Detection and Semantic Segmentation](https://neurohive.io/en/popular-networks/r-cnn/)
3. [The complete PyQt5 tutorial — Create GUI applications with Python](https://www.learnpyqt.com/)