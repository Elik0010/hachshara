import cv2
import numpy as np
import math



def reg_sift(mover, target):
  MAX_FEATURES = 500
  GOOD_MATCH_PERCENT = 0.15
  # print(target)
  orb = cv2.ORB_create(nfeatures=1500)
  keypoints1, descriptors1 = orb.detectAndCompute(target, None)
  keypoints2, descriptors2 = orb.detectAndCompute(mover, None)

  img = cv2.drawKeypoints(target, keypoints1, None)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


  # Match features.
  matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
  matches = matcher.match(descriptors1, descriptors2, None)
   
  # Sort matches by score
  matches.sort(key=lambda x: x.distance, reverse=False)
 
  # Remove not so good matches
  numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
  matches = matches[:numGoodMatches]
 
  # Draw top matches
  imMatches = cv2.drawMatches(target, keypoints1, mover, keypoints2, matches, None)
  # cv2.imwrite("matches.jpg", imMatches)
   
  # Extract location of good matches
  points1 = np.zeros((len(matches), 2), dtype=np.float32)
  points2 = np.zeros((len(matches), 2), dtype=np.float32)
 
  for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt
   
  # Find homography
  h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)
 
  # Use homography
  height, width = mover.shape
  targetReg = cv2.warpPerspective(target, h, (width, height))
   
  return targetReg, h


def rotation_registration(imgf,n):

    array = []
    img = cv2.imread(imgf, cv2.IMREAD_GRAYSCALE)
    img = img + cv2.randn(img.copy(), np.random.randint(-3,3), np.random.randint(-10,10))
    a = math.ceil(math.sqrt(img.shape[0] ** 2 + img.shape[1] ** 2) - min(img.shape[0], img.shape[1]))
    img = cv2.copyMakeBorder(img, a, a, a, a, cv2.BORDER_CONSTANT,value=0)
    array.append(img.copy())
    cv2.imshow("original",img)

    for _ in range(n-1):
        img = cv2.imread(imgf, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("JUSTREAD", img)
        rotation = np.random.randint(0,360)
        img = img + cv2.randn(img.copy(), np.random.randint(2,8), np.random.randint(-10,10))
        img = cv2.copyMakeBorder(img, a, a, a, a, cv2.BORDER_CONSTANT,value=0)
        cols, rows = img.shape
        M = cv2.getRotationMatrix2D((cols/2,rows/2), rotation, 1) 
        img = cv2.warpAffine(img, M, (cols,rows))
        cv2.imshow("rotation:", img)
        array.append(img.copy())

    img = array[0]
    del array[0]
    for i, item in enumerate(array):
        target_reg, _ = reg_sift(img, item)
        del array[i]

    cv2.destroyAllWindows()
    cv2.imshow("Final", img[a:-a,a:-a])
    # cv2.imshow("Final", img)

    cv2.waitKey(0)
    




rotation_registration("menora.jpg", 150)