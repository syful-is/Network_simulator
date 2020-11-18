# Research Artifact: What Network Simulator Questions Do Users Ask? A Large-Scale Study of Stack Overflow Posts
[https://github.com/syful-is/Network_simulator](https://github.com/syful-is/Network_simulator)

## Abstract
The use of network simulator as a modern tool in analyzing and predicting the behaviour of computer networks has grown to reduce the complexity of its accuracy measurement. This attracts researchers and practitioners to share problems and discuss them to improve the features. To communicate the related issues, users move to an online discussion platform, such as Stack Overflow. Although recent studies have shown the popularity and benefits of adopting network simulation tools, however, the challenges of using network simulator that users face remain unknown. In this paper, we examine 2,322 network-simulator-related Stack Overflow posts to extract insights on the topics and challenges that users discussed. We apply the Latent Dirichlet Allocation topic modelling to understand the topics discussed in Stack Overflow. We then investigate the popularity and difficulty of each topic. The results show that users use Stack Overflow as an implementation guideline for the network simulation model. We determine 8 discussion topics that are merged into 5 major categories. Simulation model configuration is the most useful topic for users. We also observe that target network protocol modification and network simulator installation are the most popular topics. Network simulator installation and Target Network Protocol modification issues have been challenging for most users. The findings also highlight future research to propose techniques to help the research community in its early stages to overcome the most popular and difficult topics that practitioners face when using network simulation tools.
    
## Replication package Structure:
```
📁 Network_simulator project/
├─ 📁 Dataset/
├─ 📁 Scripts/ 
├─ 📁 Results/
─
```
## Contents:
  1. [Dataset](https://github.com/syful-is/Network_simulator/tree/master/Data)- is a folder that contains the dataset for `NS project`.
  2. [Scripts](https://github.com/syful-is/Network_simulator/tree/master/Script)- is a folder that contains the all the codes. 
  3. [Results](https://github.com/syful-is/Network_simulator/tree/master/Results)- is a folder that contains the results obtained from dataset.

## How to run:
  1. Clone the repository from [here](https://github.com/syful-is/Network_simulator.git)
  2. Extract the files.
  3. Open `Jupyter Notebook` or `Python Spyder`.
  4. Copy any code and Set your working directory using 
                
                ```
                import os
                
                #Please specify your dataset directory. 
                os.chdir("..../Dataset/")
                ```
  
  4. Example-1: Run the LDA topic modeling **[01_NS_LDA.ipynb](https://github.com/syful-is/Network_simulator/blob/master/Script/01_NS_LDA.ipynb)** 

## Authors:
  1. [Syful Islam](https://syful-is.github.io/)
  2. [Yusuf Sulistyo Nugroho](https://yusufsn.github.io/)
  3. [Md. Javed Hossain](http://www.nstu.edu.bd/faculty-member/md-javed-hossain-bdr991)
  
## MIT License for code
Our SZZ implementation is licensed under the [MIT License](LICENSE).

## CC0 1.0 Universal for dataset
CC0 [summary](https://creativecommons.org/publicdomain/zero/1.0/) and [legal text](https://creativecommons.org/publicdomain/zero/1.0/legalcode)

Our dataset are published on the public domain, so that anyone may freely build upon, enhance and reuse the dataset for any purposes without restriction under copyright or database law.
