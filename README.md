Code and data for :
## _DeepAD: A deep learning application for predicting amyloid standardized uptake value ratio through PET for Alzheimer's prognosis_
***

Authors: Sucheer Maddury<sup>1</sup>, Krish Desai<sup>1</sup><br>  
 <sup>1</sup> Leland High School, San Jose, California, USA<br>  
Please address correspondence to Sucheer Maddury; e-mail: <sumaddurycollege2024@gmail.com>

DOI: [10.3389/frai.2023.1091506](https://doi.org/10.3389/frai.2023.1091506)

__Abstract__    Amyloid deposition is a vital biomarker in the process of Alzheimer's diagnosis. 18F-florbetapir PET scans can provide valuable imaging data to determine cortical amyloid quantities. However, the process is labor and doctor intensive, requiring extremely specialized education and resources that may not be accessible to everyone, making the amyloid calculation process inefficient. Deep learning is a rising tool in Alzheimer's research which could be used to determine amyloid deposition. Using data from the Alzheimer's Disease Neuroimaging Initiative, we identified 2,980 patients with PET imaging, clinical, and genetic data. We tested various ResNet, EfficientNet, and RegNet convolutional neural networks and later combined the best performing model with Gradient Boosting Decision Tree algorithms to predict standardized uptake value ratio (SUVR) of amyloid in each patient session. We tried several configurations to find the best model tuning for regression-to-SUVR. We found that the RegNet X064 architecture combined with a grid search-tuned Gradient Boosting Decision Tree with 3 axial input slices and clinical and genetic data achieved the lowest loss. Using the mean-absolute-error metric, the loss converged to an MAE of 0.0441, equating to 96.4% accuracy across the 596-patient test set. We showed that this method is more consistent and accessible in comparison to human readers from previous studies, with lower margins of error and substantially faster calculation times. We implemented our deep learning model on to a web application named DeepAD which allows our diagnostic tool to be accessible. DeepAD could be used in hospitals and clinics with resource limitations for amyloid deposition and shows promise for more imaging tasks as well.

__Notes:__
All data is available at the [Alzheimer's Disease Neuroimaging Initiative](https://adni.loni.usc.edu/).
Code was built by Sucheer Maddury.

__Cite as:__ S. Maddury and K. Desai, ‘DeepAD: A deep learning application for predicting amyloid standardized uptake value ratio through PET for Alzheimer’s prognosis’, Frontiers in Artificial Intelligence, vol. 6, 2023.
