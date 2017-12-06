#### Group Members

| #        | Name                 |
|:--------:|:--------------------:|
|   1      |    Sai Avinash Reddy Biradhavolu  |
|   2      |    Karthik Yarlapragada          |

1.What are Convolutional Neural Networks?

Answer: 
In machine learning, a convolutional neural network (CNN, or Conv Net) is a class of deep, feed-forward artificial neural networks that has successfully been applied to analyzing visual imagery. CNNs use a variation of multilayer perceptron’s designed to require minimal preprocessing. 
Reference: https://en.wikipedia.org/wiki/Convolutional_neural_network

2.What are Deconvolutional networks?

Answer:
Deconvolutional networks (De Conv Nets) have been proposed to visualize image patterns that strongly activate any given neuron in a Convolutional Neural Networks and therefore shed some light on the Convolutional Neural Networks structure. However, the De Conv Net construction is partially heuristic and so are the corresponding visualizations.
Reference: https://www.robots.ox.ac.uk/~vedaldi/assets/pubs/mahendran16salient.pdf 

3.What is Max Pooling?
Answer:
Max pooling is a sample-based discretization process. The objective is to down-sample an input representation (image, hidden-layer output matrix, etc.), reducing its dimensionality and allowing for assumptions to be made about features contained in the sub-regions binned.

Reference: https://www.quora.com/What-is-max-pooling-in-convolutional-neural-networks


4.What is Unpooling? 
Answer:
In the convnet, the max pooling operation is non-invertible, however we can obtain an approximate inverse by recording the locations of the maxima within each pooling region in a set of switch variables. In the de conv net, the Unpooling operation uses these switches to place the reconstructions from the layer above into appropriate locations, preserving the structure of the stimulus.

Reference: https://arxiv.org/pdf/1311.2901v3.pdf 


5.What is Rectified linear function?
Answer:
The rectifier function is an activation function f(x) = Max(0, x) which can be used by neurons just like any other activation function, a node using the rectifier activation function is called a ReLu node.

Reference: https://stackoverflow.com/questions/27319931/relu-and-dropout-in-cnn 

6.What is Rectification?
Answer:
The convnet uses relu non-linearities, which rectify the feature maps thus ensuring the feature maps are always positive. To obtain valid feature reconstructions at each layer (which also should be positive), we pass the reconstructed signal through a relu non-linearity.

Reference: https://arxiv.org/pdf/1311.2901v3.pdf 

7.What is Filtering?
Answer:
The convnet uses learned filters to convolve the feature maps from the previous layer. To invert this, the de conv net uses transposed versions of the same filters, but applied to the rectified maps, not the output of the layer beneath. In practice this means flipping each filter vertically and horizontally.

Reference: https://arxiv.org/pdf/1311.2901v3.pdf

8.What is Stochastic Gradient Descent?
Answer:
Stochastic gradient descent (often shortened to SGD), also known as incremental gradient descent, is a stochastic approximation of the gradient descent optimization and iterative method for minimizing an objective function that is written as a sum of differentiable functions. In other words, SGD tries to find minima or maxima by iteration.

Reference: https://en.wikipedia.org/wiki/Stochastic_gradient_descent 

9. What is a epoch?
Answer:
o	Measure of the number of times all of the training vectors are used once to update the weights.
o	For batch training, all of the training samples pass through the learning algorithm simultaneously in one epoch before weights are updated.
o	For sequential training, all of the weights are updated after each training vector is sequentially passed through the training algorithm.

Reference: http://www.ritchieng.com/machine-learning/deep-learning/tensorflow/deep-neural-nets/ 

10.What is Dropout?
Answer:
Dropout is a regularization technique for reducing overfitting in neural networks by preventing complex co-adaptations on training data. It is a very efficient way of performing model averaging with neural networks. The term "dropout" refers to dropping out units (both hidden and visible) in a neural network.

Reference: https://en.wikipedia.org/wiki/Dropout_(neural_networks) 

