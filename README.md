# Face-Detection-using-OpenCV
https://www.analyticsvidhya.com/blog/2022/04/object-detection-using-haar-cascade-opencv/#:~:text=Haar%20cascade%20works%20as%20a,modern%20object%20detection%20techniques%20are.

https://medium.com/analytics-vidhya/what-is-haar-features-used-in-face-detection-a7e531c8332b
/
/
/
Viola-Jones face detection utilizes a cascaded approach with a set of weak classifiers to efficiently identify faces in images. Initially, all features are applied to training images, determining optimal thresholds for face classification. Features with the lowest error rates are selected. The final classifier is a weighted sum of these selected features.

To enhance efficiency, a cascade of classifiers is introduced. Instead of applying all features to each window, features are grouped into stages. Windows failing an early stage are immediately discarded, reducing the need for further processing. The authors' detector consists of 6000+ features across 38 stages, with a gradual decrease in features per stage. This cascade significantly speeds up the face detection process.

In practical terms, the method involves applying a subset of features to each window, discarding non-face regions quickly, and focusing processing efforts on potential face regions. Despite having 6000+ features, on average, only 10 features are evaluated per sub-window. This cascade approach allows for efficient and accurate face detection with significantly reduced computational load. For a more in-depth understanding, refer to the original paper or additional resources.
/
/
/
recognision:
https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html
