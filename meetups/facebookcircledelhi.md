# facebookcircledelhi
---

## Steps in CNN

1. Convulation
2. Max Pooling
3. Convulation
4. Max Pooling
5. Flatenning

---

## Convulation

Operation in which dot product of image matrix with filter matrix is calculated. The main purpose of this operation is to detect the edges. This can be illustrated by following example:


**Image Matrix**

| 1 | 0 | 0 | 0 | 0 | 1 |
|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 1 |

**Filter Matrix**

The task of filter is to detect an edge.

| 1 | -1 | -1 |
|---|----|---|
| -1 | 1 | -1 |
| -1 | -1 | 1 |

Therefore the first value of the convulation would be 3 as 

(1 * 1) + (0 * -1) + (0 * -1) + (0 * -1) + (1 * 1) + (0 * -1) + (0 * -1) + (0 * -1) + (1 * 1) = 3

---

## Max Pooling

The Process of resizing by reducing the features the image into a smaller size is Known as Max Pooling. It is also done by dot product of image matrix and a filter matrix. It basically reduces the featues of an image.

---

## Flattening

The process of converting 3 Dimensional array into 2 Dimensions 

## Drawbacks of CNN

1. Need to train the whole model again for every new person.
2. Training time is large

