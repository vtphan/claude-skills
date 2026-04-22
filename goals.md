I have an existing DNA methylation analysis pipeline that I would like to productize into a user-friendly application. The app will allow users to upload raw Illumina methylation array data (IDAT files, paired Red/Green channels, with optional sample metadata).

Upon upload, the system will execute a standardized analysis pipeline that includes preprocessing (e.g., normalization and QC), followed by downstream analyses such as dimensionality reduction (PCA/UMAP), unsupervised clustering, and copy number variation (CNV) inference.

The app will generate an automated, interactive HTML report summarizing results, including:

Quality control metrics (e.g., detection p-values, signal intensity, sample outliers) Visualization of sample relationships (PCA/UMAP plots). Clustering results with annotations Genome-wide CNV plots and segmentation. The goal is to provide a streamlined, reproducible, and accessible interface for researchers and clinicians to analyze methylation data without requiring command-line expertise.

The app will be used internally by researchers. There are two roles: administrator and authenticated user (researcher)

These files are large ~25MB. So, it's preferable to have a mechanism to have users upload their files via FTP instead of via the app (at least directly).  But there should be a way to link uploaded files to users.

This app is similar to this: https://mepylome.readthedocs.io/en/latest/ 