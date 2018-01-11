# askaway-vqa_with_modifications
This implementation is based on the paper [Show, Ask, Attend, and Answer: A Strong Baseline For Visual Question Answering][0] in [PyTorch][1]. The reference code was taken from [here][2]. Here denset was used for extracting the image features and LSTM was used for question feature extraction. We have also experimented with GRU for question feature extraction. Lastly, we have studied the fixation of the network on language prior. For architecture details and results, please refer to the [project report][3].

## Running the model as it is
Download VQA 1.0 and 2.0 datasets from [here][4]. After setting up appropriate paths in config.py, run the following commands to obtain results on validation set:
```
python preprocess-images.py
python preprocess-vocab.py
python train.py
```
The progress can be viewed using:
```
python view-log.py <path to .pth log>
```


[0]: https://arxiv.org/abs/1704.03162
[1]: https://github.com/pytorch/pytorch
[2]: https://github.com/Cyanogenoid/pytorch-vqa
[3]: https://github.com/animesh20/askaway-vqa_with_modifications/blob/master/project_report.pdf
[4]: http://www.visualqa.org/vqa_v1_download.html

## Using Densenet and GRU in the network
The densenet-161 architecture was being used here and the changes were made in preprocess-images.py file. The result for this change can be viewed as:
![Graph of convergence of implementation versus paper results](https://github.com/animesh20/askaway-vqa_with_modifications/blob/master/performance_plots/Densenet1.0.png)
