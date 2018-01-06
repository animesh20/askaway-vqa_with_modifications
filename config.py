# paths
qa_path = '../data/v_2'  # directory containing the question and annotation jsons
train_path = '../data/images_2/train/train2014'  # directory of training images
val_path = '../data/images_2/val/val2014'  # directory of validation images
test_path = '../data/images_2/test/test2015'  # directory of test images
preprocessed_path = 'densenet-14x14.h5'  # path where preprocessed features are saved to and loaded from
vocabulary_path = 'vocab2.json'  # path where the used vocabularies for question and answers are saved to

task = 'OpenEnded'
dataset = 'mscoco'

# preprocess config
preprocess_batch_size = 64
image_size = 448  # scale shorter end of image to this size and centre crop
output_size = image_size // 32  # size of the feature maps after processing through a network
output_features = 2208  # number of feature maps thereof
central_fraction = 0.875  # only take this much of the centre when scaling and centre cropping

# training config
epochs = 30
batch_size = 128
initial_lr = 1e-3  # default Adam lr
lr_halflife = 50000  # in iterations
data_workers = 16
max_answers = 3000
