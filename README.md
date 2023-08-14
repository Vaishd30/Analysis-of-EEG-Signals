![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/fa6fee46-e78a-42c4-b519-46c5070fbaab)# Analysis-of-EEG-Signals
Analysis of EEG Signals to Understand Impact of Meditation on Concentration

# Abstract
In order to analyze EEG data and estimate a person's degree of concentration, we apply machine learning algorithms. From the EEG signals, we first extract Fast Fourier Transform (FFT) values and plot them against frequency. Then, we compute the intercept, coefficients and R-squared error after fitting a linear regression model to the data. These measures enable us to assess the effectiveness of our model and gauge how well it predicts the concentration level.
Machine learning algorithms can analyze EEG signals and correctly forecast a person's level of concentration. This has significant ramifications for understanding how the human brain functions and for the diagnosis and treatment of neurological illnesses.

# Different Brain Waves
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/3a2b1e9f-b504-4e28-aa75-21c99e6bed00)

# RMS MAXIMUS 32 EEG
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/6d0c2ad2-942c-416d-864f-e7e7bffe2ca3)
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/d85e6218-f84b-4c71-be38-fcc30eaa5674)
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/0e821d96-68d9-405d-aa80-03bb2296593d)
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/67d14169-3a2f-45ff-b224-54bd6529aed5)

# Regression Algorithm
Regression algorithms are commonly used for analysing EEG signals because they can help to model the relationship between EEG data and some other variable of interest, such as the level of concentration. EEG signals are typically complex and noisy, so it can be challenging to directly interpret the raw data. Regression algorithms provide a way to extract meaningful information from the data by identifying patterns and relationships between the EEG signal and the target variable.
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/ba608363-d420-4acc-9e8c-cee0c0abfd50)

# Methodology
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/fe4093f8-fad4-4ef6-ad98-c9c1240279a3)

# Block Diagram
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/86e6944d-9361-4f3e-9b9d-f87b8f8c1b76)

# Flowchart
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/d3b0f934-f541-4493-89a1-941d697c0c9e)

# Algorithm
Markup : *Regression algorithms are commonly used for analysing EEG signals because they can help to model the relationship between EEG data and some other variable of interest, such as the level of concentration.
*EEG signals are typically complex and noisy, so it can be challenging to directly interpret the raw data.
*Regression algorithms provide a way to extract meaningful information from the data by identifying patterns and relationships between the EEG signal and the target variable. 
*The machine learning process known as regression is used to forecast a continuous numerical value or output based on one or more input variables.
*Finding the correlation between the input and output variables and using that correlation to predict future data are the two main objectives of regression analysis.
*Building a mathematical model that depicts the relationship between the input variables and the output variable is how regression algorithms operate.
*A training dataset, which consists of a collection of input-output pairs, is used to build the model. The algorithm then use this model to forecast outcomes for fresh data that it hasn't before encountered.
*Pandas, Numpy, Scikit-Learn, and Matplotlib.pyplot should all be imported. Import data from an Excel file 
*FFT values and frequency should be extracted from the loaded data.
*Using Matplotlib, create a scatter plot of the FFT values versus frequency. 
*Scikit-learn is used to fit a linear regression model to the FFT values and frequency data. 
*Making use of the regression model, make predictions. 
*The difference between the actual and anticipated FFT values is used to calculate the residuals. 
*Use Scikit-Learn to print the regression coefficients and model performance indicators like mean squared error and R-squared. 
*Based on the predictions of the regression model, calculate the concentration level 
*Utilizing Matplotlib, plot the regression line and scatter plot of the FFT values against frequency.
*Using matplotlib, create a scatter plot of the FFT results versus the residuals and add a horizontal line at 0 to see the residuals.

# Before meditation result
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/5e0b3564-7908-4a83-8e6e-12fa2de81d33)
The above figure consists of Frequency vs PSD , Regression line , Residual plot and regression parameters which indicates a more alert mind state, resulting in more frequent alpha waves in the brain.

# After meditation result
![image](https://github.com/Vaishd30/Analysis-of-EEG-Signals/assets/139155413/a7de9c0f-04b6-4895-8db9-30032f578296)
The above figure consists of Frequency vs PSD , Regression line, Residual plot and regression parameters which indicates a focused mind state and cognitive task is performed, resulting in more frequent beta waves in the brain.

# References
[1] Aftanas, L. I., & Golocheikine, S. A. (2001). Non-linear dynamic complexity of the human EEG during meditation. Neuroscience letters, 310(1), 57-60.
[2] Baijal, S., & Srinivasan, N. (2010). Theta activity and meditative states: spectral changes during concentrative meditation. Cognitive processing, 11(1), 31-38.
[3] Cahn, B. R., & Polich, J. (2006). Meditation states and traits: EEG, ERP, and neuroimaging studies. Psychological bulletin, 132(2), 180.
[4] Carter, O. L., Presti, D. E., Callistemon, C., Ungerer, Y., Liu, G. B., & Pettigrew, J. D. (2005). Meditation alters perceptual rivalry in Tibetan Buddhist monks. Current Biology, 15(11), R412-R413.
[5] Dillbeck, M. C., & Bronson, E. C. (1981). Short-term longitudinal effects of the transcendental meditation technique on EEG power and coherence. International Journal of Neuroscience, 14(3-4), 147-151.
[6] Gao, X., Xu, M., Xu, P., Wang, Y., Zhu, C., & Wang, Y. (2011). EEG-fMRI study on the interplay between brain spontaneous activity and meditation. NeuroImage, 57(3), 846-850.
[7] Hinterberger, T., Schmidt, S., Kamei, T., & Walach, H. (2014). EEG feedback and subjective meditation. International Journal of Psychophysiology, 93(1), 59-64.
[8] Josipovic, Z. (2014). Neural correlates of nondual awareness in meditation. Annals of the New York Academy of Sciences, 1307(1), 9-18.
[9] Khushu, S., Kumar, V., Tripathi, R. P., & Jain, N. (2006). Quantitative EEG and neurofeedback therapy in children with attention deficit hyperactivity disorder: a retrospective feasibility study. Journal of Neurotherapy, 10(4), 37-44.
[10] Leung, M. K., Chan, C. C., Yin, J., Lee, C. F., So, K. F., & Lee, T. M. (2013). Increased gray matter volume in the right angular and posterior parahippocampal gyri in loving-kindness meditators. Social cognitive and affective neuroscience, 8(1), 34-39.
[11] Liang, W. K., Lo, M. T., Yang, A. C., Peng, C. K., Cheng, S. K., & Tseng, P. (2015). Revealing the brain's adaptability and the transcranial direct current stimulation facilitating effect in inhibitory control by multiscale entropy. NeuroImage, 108, 356-366.










