---
layout: post
title:  "Topological mapping for traversability-aware long-range navigation in off-road terrain"
date:   2025-02-13 10:51:09 -0400
categories: research projets 
---

<div style="text-align:center;">
<b>ICRA 2025 - Altanta, GA, USA<br/>
<a href="https://arxiv.org/abs/2410.01925">arXiv</a></b>
</div>

![](../../../../../figure_topological_mapping.png)

# Video presentation
Ready soon!

# Abstract
Autonomous robots navigating in off-road terrain like forests open new opportunities for automation. While off-road navigation has been studied, existing work often relies on clearly delineated pathways. We present a method allowing for long-range planning, exploration and low-level control in unknown off-trail forest terrain, using vision and GPS only. We represent outdoor terrain with a topological map, which is a set of panoramic snapshots connected with edges containing traversability information. A novel traversability analysis method is demonstrated, predicting the existence of a safe path towards a target in an image. Navigating between nodes is done using goal-conditioned behavior cloning, leveraging the power of a pretrained vision transformer. An exploration planner is presented, efficiently covering an unknown off-road area with unknown traversability using a frontiers-based approach. The approach is successfully deployed to autonomously explore two 400 meters squared forest sites unseen during training, in difficult conditions for navigation. 

# Complete test footage, test site A
Autonomous exploration, aside from 13 interventions in 20 minutes
<!-- blank line -->
<figure class="video_container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/GZpQKdrs_Rs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>
<!-- blank line -->

# Complete test footage, test site B
Autonomous exploration, aside from 12 interventions in 20 minutes
<!-- blank line -->
<figure class="video_container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/i-8RXuMICNI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>
<!-- blank line -->

