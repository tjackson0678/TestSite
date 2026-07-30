---
title: "Your Presentation Title"
author:
  - "Terrence Jackson"
  - "Advisor: Dr. Ron Sass"
institute: "UNC Charlotte"
date: "Summer 2026"
aspectratio: 169
---

<!--

  Thesis Defense Slides

  all in one command to make a quick PDF...

  pandoc -t beamer --slide-level 2 thesis_slides.md -o thesis_slides.pdf

-->

# Intro

## Background

- BS in Computer Science from UMBC (Maryland Balt Co.)

- Currently Staff Systems Engineer @ Carrier Corporation

- 20+ years experience in Defense, Technology

- LM, Honeywell, Centene, Carrier, GA

- Software Development, and Systems Engineering experiences

- Pursuing MS Computer Engineering from UNCC starting 2024

## Consider: Imaginary Scenario

*   **2023** a large HVAC company launches a "next generation" controller
    (Gryphon) 
    -   modern interface with high resolution screen
    -   sophisticated algorithms for large commercial buildings
    -   SOM (System-on-a-Module) integrated with a
        full-custom controller
    \pause

- **2024** ChatGPT introduced and AI explodes
  \pause

- **2026** naturally a fictional executive wants to be a part of AI boom
  and starts to ask ...
  \pause
  - can we do AI on the Gryphon controller?
  - noting, we are only 3 years into a 15-20 year lifetime!
  - the engineering question:
    \pause
    **_Are ML algorithms feasible on Gryphon?_**

## Outline

- Intro/Framing of the question and assumptions

- Background and Related works

- Extensions to Infrastructure & firmware

- Build Experiments and Analysis

- Ultimate Result and Conclusion

# Background

## Experiments and Infrastructure

- Gryphon board is using Yocto Linux build
  - SOM Manufactured by ADLink 
  - SMARC form factor 
  - Cellular M.2 modem slot 

- IMX8M Plus Microcontroller design
  - Quad core System on Module (SOM)
  - Integrated NPU, VPU, GPU Units 
  - Custom 4GB LPDDR RAM

- PCB with a System on Module (SOM) board design
  - Quad Core SoC 
  - ARM Cortex-A53 + Cortex-M7
  - Integrated WiFi and Bluetooth

## Infrastructure (cont'd)

- Unused processing potential 
  - 2.3 TOPS Neural Processing Unit 
  - Vivante. GC7900UL GPU

- Linux Ubuntu with Yocto Build Recipe
  - 16GB Flash Memory available
  - SD Card slot, Video decoding 

- Added Python and some Specific libraries for AI, ML
  - Tensor Flow, APT, PIP Installers 
  - SciPY, Numpy, Matplotlib for charts, graphs
  - Pandas for datatables 

- Build Guide explains exact recipes uses, but others added
  - Sklearn, Seaborn for training models, datasets 

# Analysis and Experiments

## Analysis and Setup

- Experimented with a number of intro to ML projects to test
  - Linear Regression with Gradient Descent
  - Computing Cost Functions using variable Theta and Cost functions

- Predictive Models using Training and Test data
  - Used to create more accurate predictions
  - Supervised learning modes to create predictions  

- Classification Models with predictions and Accuracy scoring
  - Case where there is a discrete subset of outcomes 
  - Different models allow fore better accuracy 

- 4 Projects in total

## Analysis and Experiments (cont'd)

- Datasets from Kaggle.com and Sklearn libraries
  - Energy Data - multiple features and sampled efficiencies
  - Steel Data - years worth of efficiencys for plant
  - Breast Cancer data - classification of outcomes 
  - Housing data - prices and home feature data  

- Used for training as well as predictions

Runtimes varied across the machines used 
  - 2s to 6-10 minutes on a laptop
  - 22s to 59min on target device
  - small/nominal dataset sizes for assignments 

## Analyssis and Experiments (cont'd)

Runtimes accros the machines tested: 
  - Small, med, large datasets used in projects
  - Smaller sets ran quicker
  - larger sets (700 - 35K samples) ran slower 

Target machine seemed up to the challenge: 
  - Larger took more time but eventually completed
  - Multiple Learning Models used for projects
    - Classification, linear, logistic regression models 
  - Theta and interation values affected outcome times
    - most still completed with target machine working much slower 
    - 6-10min vs 20-59min on target 

## Analysis and Experiments (cont'd)

Additional Experiments - MicroGPT 
  - Out of the box experiment using MicroGPT    
  - Python version of scaled down ChatGPT
  - No libraries or dependencies, just one text input file

MicroGPT - 1 text file as input 
  - Outputs predicttions based on input
  - Use any input for training
  - Names, address, businesses 

Running results of MicroGPT 
  - 1000 Steps / samples 
  - Initially 3-4 minutes on Laptop
  - 1000 (default) - 24 minutes on target

## Analysis and Experiments (cont'd)

Additional tests w/MicroGPT 
  - 15000 steps (learning inputs)
    - 6 hrs on target 
  - 4 Layers of Neural Network Transformers
    - 50 Minutes on Target
  - 10000 steps and 4 depths of layers 
    - 17 hours on target 

- Other options include:
  -  Width of network 
  -  Attenuation heads

- Tests w/options rapidly push target limits

# Conclusion

## Conclusion

- Positive case outcomes with limitations
  - Nominal testing of AI and ML 
  - Successful Linear Regression runs
  - Classifications successful 

- Complex cases of AI present limitations 
  - Tuning of AI/ML Learning variables 
  - Theta, iterations, sample size

- Hardware sufficient for what is needed at this time
  - NPU / GPU may also add capability 
  - Tensor flow for GPU runs 
