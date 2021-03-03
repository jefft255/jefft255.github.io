---
layout: post
title:  "Multimodal dynamics modeling for off-road robots"
date:   2020-11-06 10:51:09 -0400
categories: research projets 
---

# Video
<!-- blank line -->
<figure class="video_container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/y-JS5Q1fLHs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>
<!-- blank line -->

# Quick facts
* Building dynamics models for wheeled robots traversing natural terrain require reasoning about changing traction, topography and possibly non-rigid obstacles.
* We leverage self-supervised learning to learn a state representation which incorporates information from multiple sensors to better predict the future motion of the robot.
* We test our method on synthetic data generated with an Unreal Engine simulator, as well as on the real-world [Montmorency dataset](https://norlab.ulaval.ca/research/montmorencydataset/).
* Our model is robust to missing modalities at test time, with minimal prediction accuracy loss.
* Accepted to ICRA 2021!
* The preprint is available [here](https://arxiv.org/abs/2011.11751)

# Abstract
Dynamics modeling in outdoor and unstructured environments is difficult because different elements in the environment interact with the robot in ways that can be hard to predict.
Leveraging multiple sensors to perceive maximal information about the robot's environment is thus crucial when building a model to perform predictions about the robot's dynamics with the goal of doing motion planning.
We design a model capable of long-horizon motion predictions, leveraging vision, lidar and proprioception, which is robust to arbitrarily missing modalities at test time.
We demonstrate in simulation that our model is able to leverage vision to predict traction changes.
We then test our model using a real-world challenging dataset of a robot navigating through a forest, performing predictions in trajectories unseen during training.
We try different modality combinations at test time and show that, while our model performs best when all modalities are present, it is still able to perform better than the baseline even when receiving only raw vision input and no proprioception, as well as when only receiving proprioception.
Overall, our study demonstrates the importance of leveraging multiple sensors when doing dynamics modeling in outdoor conditions. 


