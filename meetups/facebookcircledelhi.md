# Convulation

Operation which is used to convert an image matrix using dot product of image matrix as well as filter matrix. This can be illustrated by following example:


**Image Matrix**

| 1 | 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 1 |

**Filter Matrix**

| 1 | -1 | -1 |
| -1 | 1 | -1 |
| -1 | -1 | 1 |

Therefore the first value of the convulation would be 3 as 

(1 * 1) + (0 * -1) + (0 * -1) + (0 * -1) + (1 * 1) + (0 * -1) + (0 * -1) + (0 * -1) + (1 * 1) = 3