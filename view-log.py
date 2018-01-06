import sys
import torch
import numpy
import matplotlib; matplotlib.use('agg')
import matplotlib.pyplot as plt


def main():
    path = sys.argv[1]
    results = torch.load(path)

    val_acc = torch.FloatTensor(results['tracker']['val_acc'])
    val_acc = val_acc.mean(dim=1).numpy()
    numpy.savetxt("VQA2.0-simple.csv", val_acc, delimiter=",")

    plt.figure()
    plt.plot(val_acc)
    plt.savefig('val_acc.png')


if __name__ == '__main__':
    main()
