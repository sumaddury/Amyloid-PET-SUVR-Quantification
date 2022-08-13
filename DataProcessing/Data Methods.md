1. The data was collected from the *Alzheimer's Disease Neuroimaging Initiative* [ADNI](https://adni.loni.usc.edu/) with the included patient IDs (these IDs were determined from additional scripts, not included).
2. The images were filtered by slice and partitioned by patient using **ImageSorting.py.**
3. The individual patients each had color composites made from the slices using **ColorCompositeMaker.py.**

Seperately, clinical data was found using **ClinicalProcessing.py**, this was found using the download CSV function on ADNI for the selected patient IDs
The Standardized Uptake Value Ratios were found using the UC Berkeley AV45 Analysis, specifically the **SUMMARYSUVR_WHOLECEREBNORM** value.
