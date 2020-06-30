 
_base_ = [
    # '../_base_/models/faster_rcnn_r50_fpn.py',
	# '../_base_/models/faster_rcnn_r50_caffe_c4.py',
    '../_base_/models/retinanet_r50_fpn.py',
    '../_base_/datasets/voc0712.py',
    '../_base_/default_runtime.py'
]

# faster RCNN
# model = dict(roi_head=dict(bbox_head=dict(num_classes=10)))

#Retinanet
# model = dict(bbox_head=dict(num_classes=10))

# optimizer

#Faster RCNN
# optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
# optimizer_config = dict(grad_clip=None)
# lr_config = dict(policy='step', step=[6])
# total_epochs = 6  # actual epoch = 4 * 3 = 12


#Retinanet
optimizer = dict(  # Config used to build optimizer, support all the optimizers in PyTorch whose arguments are also the same as those in PyTorch
    type='SGD',  # Type of optimizers, refer to https://github.com/open-mmlab/mmdetection/blob/master/mmdet/core/optimizer/default_constructor.py#L13 for more details
    lr=0.01,  # Learning rate of optimizers, see detail usages of the parameters in the documentaion of PyTorch
    momentum=0.9,  # Momentum
    weight_decay=0.0001)  # Weight decay of SGD
optimizer_config = dict(  # Config used to build the optimizer hook, refer to https://github.com/open-mmlab/mmcv/blob/master/mmcv/runner/hooks/optimizer.py#L8 for implementation details.
    grad_clip=None)  # Most of the methods do not use gradient clip
lr_config = dict(  # Learning rate scheduler config used to register LrUpdater hook
    policy='step',  # The policy of scheduler, also support CosineAnealing, Cyclic, etc. Refer to details of supported LrUpdater from https://github.com/open-mmlab/mmcv/blob/master/mmcv/runner/hooks/lr_updater.py#L9.
    warmup='linear',  # The warmup policy, also support `exp` and `constant`.
    # warmup_iters=500,  # The number of iterations for warmup
    # warmup_ratio=0.001,  # The ratio of the starting learning rate used for warmup
    step=[6])  # Steps to decay the learning rate
total_epochs = 12  # Total epochs to train the model