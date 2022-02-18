# Predicting OOD Generalization with Local Manifold Smoothness

This is an implementation of our paper Predicting OOD Generalization with Local Manifold Smoothness. In order to calculate smoothness values, we require 3 files:
- ID File: list of example IDs, where each ID corresponds to an augmented version of a particular example. For example, if example 0 was augmented 10 times, we expect 11 IDs of 0 in the ID file (one for the original example and 10 for the augmented examples)
- Pred File: list of predictions for each example. Should be ints corresponding to the label.
- Label File: list of true labels for each example. Should be ints correspoding to the label.
As an example for each of these file formats, refer to the `example` directory. 

To calculate smoothness for the classification task in the example folder with 5 examples, we can run
```
python3 smoothness.py \
  --id-file example/ids.txt \
  --pred-file example/preds.txt \
  --label-file example/labels.txt \
  --num-classes 5
```
This will generate a file `res.json` in the current directory containing a dictionary mapping example IDs to smoothness and accuracy values as well as output the overall accuracy and smoothness for the entire dataset.

`Accuracy: 0.6714212939378502    Smoothness: 0.8437919696197912`
