Todays Objectives

* half-day Machine Learning
* half-day Spark

* Deploying a model to Heroku

* Transfer Learning

A technique for modifying the classes of a Pretrained model with custom classes. Things to know about this
    1) Pretrained model normally has many layers
    
    2) Transfer learning modifies weights in a subset of layers

    3) Simplest will be modifying just the last layer of the Pretrained model

    4) The nodes in the new layer represent your desired classes

    5) Good starting accuracy with this method

* Auto Encoders

The start to image generation is the Auto Encoder NN. This special NN can be used to distill an image to it's essence ("Code") and then re-generate and image from that. A picture can be seen below
https://miro.medium.com/max/5286/1*oUbsOnYKX5DEpMOK3pH_lg.png

Auto Enoder is composed of an Encoder and Decoder
    1 ) Encoder used to distill inputs

    2) Decoder use to generate a new image from the "Code" layer

    3) Colab activity we follow
    https://colab.research.google.com/github/zaidalyafeai/Notebooks/blob/master/AutoEncoders.ipynb

* Times Series modeling with Recurrent NN

* BERT (Bidirectional Encoder Representations from Transformers)