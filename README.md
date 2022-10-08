Code and data for :
## _Using Deep Learning to Determine Amyloid Deposition through PET and Clinical Data for Alzheimer's Prognosis_
***

Authors: Sucheer Maddury<sup>1</sup>, Krish Desai<sup>1</sup><br>  
 <sup>1</sup> Leland High School, San Jose, California, USA<br>  
Please address correspondence to Sucheer Maddury; e-mail: <sumaddurycollege2024@gmail.com>

DOI: [10.1101/2022.10.04.22280712](https://doi.org/10.1101/2022.10.04.22280712)

__Abstract__    Amyloid deposition is a vital biomarker in the process of Alzheimer's diagnosis. Florbetapir PET scans can provide valuable imaging data to determine cortical amyloid quantities. However the process is labor and doctor intensive, requiring extremely specialized education and resources that may not be accessible to everyone, making the amyloid calculation process inefficient. Deep learning is a rising tool in Alzheimer's research which could be used to determine amyloid deposition. Using data from the Alzheimer's Disease Neuroimaging Initiative, we identified 2980 patients with PET imaging, clinical, and genetic data. We tested various ResNet and EfficientNet convolutional neural networks and later combined them with Gradient Boosting Decision Tree algorithms to predict standardized uptake value ratio (SUVR) of amyloid in each patient session. We tried several configurations to find the best model tuning for regression-to-SUVR. We found that the EfficientNetV2-Small architecture combined with a grid search-tuned Gradient Boosting Decision Tree with 3 axial input slices and clinical and genetic data achieved the lowest loss. Using the mean-absolute-error metric, the loss converged to an MAE of 0.0466, equating to 96.11% accuracy across the 596 patient test set. We showed that this method is more consistent and accessible in comparison to human readers from previous studies, with lower margins of error and substantially faster calculation times. Deep learning algorithms could be used in hospitals and clinics with resource limitations for amyloid deposition, and shows promise for more imaging tasks as well.

Research is protected under a CC-BY-NC-ND 4.0 International license.

Notes:
All data is available at the [Alzheimer's Disease Neuroimaging Initiative](https://adni.loni.usc.edu/).
Code was built by Sucheer Maddury.

Cite as: Maddury SM, Desai KS. Using Deep Learning to Determine Amyloid Deposition through PET and Clinical Data for Alzheimer's Prognosis. medRxiv; 2022. DOI: 10.1101/2022.10.04.22280712.
