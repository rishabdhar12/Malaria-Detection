# Malaria-Detection

* Created a tool to save humans by detecting and deploying Image Cells that contain Malaria or not!
* Engineered images for better fit.
* Used Pre-trained model (VGG19) for predictions.
* Built a client facing API using flask

# Codes and Resources Used


* Python Version: 3.8.5
* Tensorflow Version : 2.2.0
* Packages: numpy, matplotlib, flask, tensorflow
* For Web Framework Requirements: pip install -r requirements.txt
* This Dataset is taken from the official NIH Website: https://ceb.nlm.nih.gov/repositories/malaria-datasets/
* Flask Productionization: https://www.youtube.com/watch?v=H-bcnHE6Mes&t=5286s



# Project Overview

Malaria is a life-threatening disease caused by parasites that are transmitted to people through the bites of infected female Anopheles mosquitoes. It is preventable and curable.

* In 2017, there were an estimated 219 million cases of malaria in 90 countries.
* Malaria deaths reached 435 000 in 2017.
* The WHO African Region carries a disproportionately high share of the global malaria burden. In 2017, the region was home to 92% of malaria cases and 93% of malaria deaths.

Malaria is caused by Plasmodium parasites. The parasites are spread to people through the bites of infected female Anopheles mosquitoes, called "malaria vectors." There are 5 parasite species that cause malaria in humans, and 2 of these species – P. falciparum and P. vivax – pose the greatest threat.

# EDA

![alt text](https://github.com/rishabdhar12/Malaria-Detection/blob/main/one.png)


# Model Building

The model was build using Pre Trained model VGG19
https://keras.io/api/applications/vgg/


# Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request as image and returns a prediction.


























