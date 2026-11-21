---
layout: work
title: Building a GAN with PyTorch & SageMaker
permalink: /projects/gan-sagemaker/
description: A published engineering walkthrough connecting a custom generative model to managed cloud training.
kind: Published engineering example
period: 2021
role: Author, AWS Machine Learning Blog
focus: PyTorch, managed training, and model artifacts
visual: gan
---

## The problem

Understanding a generative model also means understanding how to train and run it. This example uses handwritten digits to make the engineering workflow concrete.

## The approach

The walkthrough combines a PyTorch DCGAN, MNIST training data, and a SageMaker training job. A notebook configures the run; a separate training script implements the model. Data and model artifacts are stored in Amazon S3.

## Engineering decisions

- Separate training code from notebook orchestration.
- Pass hyperparameters and data locations into the training job.
- Reload the saved generator to inspect synthetic handwriting.

## Published artifacts

The deliverables are an AWS article and an accompanying example notebook.

- [Read the AWS article](https://aws.amazon.com/blogs/machine-learning/build-gan-with-pytorch-and-amazon-sagemaker/)
- [Explore the example notebook](https://github.com/aws/amazon-sagemaker-examples/blob/main/advanced_functionality/pytorch_bring_your_own_gan/build_gan_with_pytorch.ipynb)

*Published in 2021. The original environment versions are documented in the article; this example has not been retested against current releases.*
