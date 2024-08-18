# Chapter 5: Perspective Warping

In this chapter, we will explore how to perform perspective warping on images using OpenCV.

## Table of Contents

1. 🔄 **Warp Perspective**

### 🔄 Warp Perspective

**Warp Perspective** is a transformation technique that changes the perspective of an image, making it appear as if it was viewed from a different angle. This is useful in applications like document scanning, where you want to correct the perspective of a tilted document to make it look flat.

#### Key Points:
- **Transformation Matrix**: To warp the perspective, you first need to define a transformation matrix. This matrix maps points from the source image to the destination image.
- **Point Mapping**: Identify four points in the original image and map them to the desired points in the output image. The order of these points should correspond between the input and output images.
- **Application**: Commonly used in tasks like correcting perspective distortions, creating top-down views of objects, or aligning images for stitching.
