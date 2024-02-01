# Root Cause Prediction Using Deep Learning

![nn_architecture.png](Root%20Cause%20Prediction%20Using%20Deep%20Learning%2000c499d7984646f0b4367be118995ff1/nn_architecture.png)

# Problem Statement

In IT Service Management (ITSM), incident tickets often provide user-reported symptoms. Identifying the root cause of these symptoms is crucial for reducing resolution times and improving user satisfaction. This project employs deep learning to predict the root cause based on the given symptoms.

**Key Objective:** Quickly identify the root cause of incidents reported in ITSM based on observed symptoms.

## Dataset

Dataset Link: [Root Cause Analysis Dataset on Kaggle](https://www.kaggle.com/datasets/anjolaoluwaajayi/root-cause-analysis-dataset/data)

### Overview

The training data consists of symptoms collected by technical teams during incident analysis. Each symptom is represented as a binary attribute (1 or 0), indicating its presence or absence. The dataset includes 1000 training examples, providing a foundation for predicting root causes.

### Symptoms Include:

- CPU load
- Memory load
- Network delays
- Specific error codes in log files

### Target Variable:

- Root Cause (Classes of root causes)

*Note: In real-world scenarios, symptom diversity may be vast. Symptoms can be further categorized by location (e.g., load balancer, microservice) and isolated from text using text mining.*

## Model Architecture:

![Screenshot 2023-12-29 at 11.41.50 AM.png](Root%20Cause%20Prediction%20Using%20Deep%20Learning%2000c499d7984646f0b4367be118995ff1/Screenshot_2023-12-29_at_11.41.50_AM.png)

### Model Overview

The neural network architecture consists of hidden layers using the `relu` activation function and an output layer using `softmax`. The model is trained with categorical cross-entropy loss and the Adam optimizer.

### Activation Functions

- Hidden Layers: `relu`
- Output Layer: `softmax`

### Loss Function

- Categorical Cross-Entropy

### Optimizer

- Adam

## Model Performance

- Training Accuracy: 87%
- Validation Accuracy: 81%

![accuracy.png](Root%20Cause%20Prediction%20Using%20Deep%20Learning%2000c499d7984646f0b4367be118995ff1/accuracy.png)

![loss.png](Root%20Cause%20Prediction%20Using%20Deep%20Learning%2000c499d7984646f0b4367be118995ff1/loss.png)

## Deployment

The trained model can be deployed for practical use. Below is a screenshot of the web application:

![app_ss.png](Root%20Cause%20Prediction%20Using%20Deep%20Learning%2000c499d7984646f0b4367be118995ff1/app_ss.png)