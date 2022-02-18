import argparse
import os
import json

def get_smoothness(id_file, pred_file, label_file, k, out_dir):

    # load res if it exists
    outf = os.path.join(out_dir, 'res.json')
    if os.path.exists(outf):
        return json.load(open(outf))

    # load all required files
    ids = open(id_file, 'r').readlines()
    preds = open(pred_file, 'r').readlines()
    labels = open(label_file, 'r').readlines()

    res = {}
    for eid, pred, label in zip(ids, preds, labels):
        eid = int(eid.strip())
        pred = int(pred.strip())
        label = int(label.strip())

        # add smoothness and prediction
        if eid not in res:
            res[eid] = [[0] * k, pred == label]
        res[eid][0][pred] += 1

    for eid in res:
        res[eid][0] = max(res[eid][0])/sum(res[eid][0])

    with open(outf, 'w') as of:
        json.dump(res, of)

    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--id-file', '-i', type=str, required=True,
            help='Path to file with example IDs')

    parser.add_argument('--pred-file', '-p', type=str, required=True,
            help='Path to file with predicted labels.')

    parser.add_argument('--label-file', '-l', type=str, required=True,
            help='Path to file with true labels.')

    parser.add_argument('--output', '-o', type=str, default='.',
            help='Path to output directory. If not specified, use current directory.')

    parser.add_argument('--num-classes', '-k', type=int, default=None,
            help='Number of total classes.')

    args = parser.parse_args()

    res = get_smoothness(args.id_file, args.pred_file, args.label_file, args.num_classes, args.output)

    accuracy = 0
    smoothness = 0
    for eid in res:
        smoothness += res[eid][0]
        accuracy += res[eid][1]

    accuracy /= len(res)
    smoothness /= len(res)
    print("Accuracy: {}\tSmoothness: {}".format(accuracy, smoothness))


