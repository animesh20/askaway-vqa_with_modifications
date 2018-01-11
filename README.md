# askaway-vqa_with_modifications
This implementation is based on the paper [Show, Ask, Attend, and Answer: A Strong Baseline For Visual Question Answering][0] in [PyTorch][1]. The reference code was taken from [here][2]. Here denset was used for extracting the image features and LSTM was used for question feature extraction. We have also experimented with GRU for question feature extraction. Lastly, we have studied the fixation of the network on language prior. For architecture details and results, please refer to the [project report][3].
The VQA 1.0 and VQA 2.0 dataset can be selected by editing the paths in config.py.

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
## Using Densenet and GRU in the network
The densenet-161 architecture was being used here and the changes were made in preprocess-images.py file. The result for this change can be viewed as:
![Graph of convergence of implementation versus paper results](https://github.com/animesh20/askaway-vqa_with_modifications/blob/master/performance_plots/Densenet1.0.png)

The GRU network was implemented in model.py and can be changed back to LSTM by editing the same.

## Studying the fixation on language prior by turning off image pipeline
The fixation on language prior was first studied by passing a tensor of all 1s. This was done by editing data.py and image can be turned on by editing the same.

## Studying the fixation on language prior by removing the image and attention pipeline
The fixation on language prior was then studied by simplifying the network and reducing it to NLP question answering task. This was done by editing model.py. The execution time was reduced 3 times here.

## Visualizations
![v1](https://github.com/animesh20/askaway-vqa_with_modifications/blob/master/performance_plots/v1.png)

Obtained attention from AskAway for question ’Does this flask have enough wine to fill the glass?’ a) Input image b) First attention glimpse c)Second attention (finer) glimpse

![v2](https://github.com/animesh20/askaway-vqa_with_modifications/blob/master/performance_plots/v2.png)
![v3](https://github.com/animesh20/askaway-vqa_with_modifications/blob/master/performance_plots/v3.png)

[0]: https://arxiv.org/abs/1704.03162
[1]: https://github.com/pytorch/pytorch
[2]: https://github.com/Cyanogenoid/pytorch-vqa
[3]: https://github.com/animesh20/askaway-vqa_with_modifications/blob/master/project_report.pdf
[4]: http://www.visualqa.org/vqa_v1_download.html
