# Research Artifact: What Network Simulator Questions Do Users Ask? A Large-Scale Study of Stack Overflow Posts
[https://github.com/syful-is/Network_simulator](https://github.com/syful-is/Network_simulator)

# Abstract
The use of network simulator as a modern tool in analyzing and predicting the behaviour of computer networks has grown to reduce the complexity of its accuracy measurement.
 This attracts the researchers and practitioners to share problems and discuss to improve the features.
 To communicate the issues relates to network simulators, users move to an online discussion platform, such as Stack Overflow.
 Although recent studies have shown the popularity and benefits of adopting network simulation tools, however, the challenges of using network simulator that users face remain mostly unknown. 
 Therefore, in this paper, we examine 2,322 network-simulator-related Stack Overflow posts to provide insights on the topics that users are interested and the challenges they face. 
 We apply the Latent Dirichlet Allocation topic modeling to understand the topics that are being discussed in Stack Overflow. 
 Then, we investigate the popularity and difficulty of each topic.
 The results of this study show that users use Stack Overflow as an implementation guideline for network simulation model. 
 We determine 8 discussion topics (e.g., network simulator installation) that are merged into 5 major categories.
 Most of the posts discuss simulation model configuration. 
 We also observe that target network protocol modification and network simulator installation are the most popular topics among the users compared to other topics. 
 Users are specially facing challenges on network simulator installation and Target Network Protocol modification issues. 
 The findings also highlight for future research to propose techniques to help the research community at its early stages to overcome the most popular and difficult topics that practitioners face when using network simulation tools.
 
# Replication package Structure:
```
📁 Network_simulator project/
├─ 📁 Dataset/
├─ 📁 Scripts/ 
├─ 📁 Results/
─
```
### Contents:
  1. [Dataset](https://github.com/syful-is/Network_simulator/tree/master/Data)- is a folder that contains the dataset for `NS project`.
  2. [Scripts](https://github.com/syful-is/Network_simulator/tree/master/Script)- is a folder that contains the all the codes. 
  3. [Results](https://github.com/syful-is/Network_simulator/tree/master/Results)- is a folder that contains the results obtained from dataset.

# How to run:
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

# Authors:
  1. [Syful Islam](https://syful-is.github.io/)
  2. [Yusuf Sulistyo Nugroho](https://yusufsn.github.io/)
  3. 
