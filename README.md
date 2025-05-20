# AViT-UNet: An Efficient Medical Image Segmentation Method Based on Multiple Attention Mechanisms

*HaoBin XU ,  Zhendong LI ,  YiQiang WU ,  Hao LIU ,  Shuai LI*

### Abstract

> Existing medical image segmentation methods suffer from high computational complexity, large parameter counts, and suboptimal accuracy that hinder deployment on low-resource clinical edge devices,. To address these issues, we propose AViT-UNet, a lightweight Vision Transformer U-Net model incorporating multiple attention mechanisms to reduce model size and latency while maintaining competitive segmentation performance. The method first designs a lightweight convolutional module LDB and applies it to the convolutional module of the encoding-decoding layer, which significantly reduces the computational complexity of the model. Secondly, the method invokes a self-attention mechanism module EMHA, which is applied in the deep network and bottleneck layer to significantly enhance the segmentation accuracy. Finally, to enhance the fidelity of skip connections and feature fusion, the network integrates channel and spatial attention mechanisms to bolster residual pathways and deepen convolutional representations, yielding more precise segmentation outputs. This strategy effectively offsets the high computational demands of Transformer-based models and compensates for the limited global receptive field of conventional convolutional neural networks. As a result, the proposed lightweight architecture achieves superior semantic segmentation accuracy while remaining suitable for deployment on resource-constrained medical devices and mobile platforms. Experimental results show that the method proposed in this paper is validated on three publicly available medical image semantic segmentation benchmark datasets, Synapse, GlaS, and MoNuSeg, with multi-dimensional evaluation metrics, and the validation results fully prove that the method proposed in this paper has a certain degree of sophistication and feasibility. The specific implementation code of the method proposed in this paper has been uploaded to https://github.com/shepherdxu/AViT-UNet.

![image](https://github.com/user-attachments/assets/3ac2d3fc-6194-40b5-9fe7-5bd032cbc6c0)


### Data pre

Synapse dataset is used in our paper. [Download](https://paperswithcode.com/sota/medical-image-segmentation-on-synapse-multi)

![消融实验二维图](https://github.com/user-attachments/assets/68e6302b-c484-4631-ad18-aba8af7b5f80)



### Thanks for the code provided by:

**EfficientFormerV2** https://github.com/snap-research/EfficientFormer/blob/main/README.md

**Swin-Unet** https://github.com/HuCaoFighting/Swin-Unet

**SelfReg-UNet** https://github.com/ChongQingNoSubway/SelfReg-UNet

**UCTransNet** https://github.com/McGregorWwww/UCTransNet/blob/main/nets/UCTransNet.py

**EViT-UNet**  https://github.com/Retinal-Research/EVIT-UNET

### Thanks for the datasets open-sourced by:

https://paperswithcode.com/sota/medical-image-segmentation-on-synapse

https://arxiv.org/abs/2306.07863
