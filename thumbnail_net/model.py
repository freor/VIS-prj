from PIL import Image
from torchvision import transforms
import torch
import torchvision.models as models
import torch.nn as nn
from torch.autograd import Variable

import json
import os
import time


for nation in ['CA', 'GB', 'IN']:
    jsonfile = open(f'../youtube-json/views_{nation}videos.json', 'r')
    fpath = "../thumbnail_img/"

    new_jsonfile = open(f'./views_{nation}_thumbnail_vector.json', 'w')

    d = json.load(jsonfile)#["nodes"]

    ext = ".jpg" # image file extension

    resnet18 = models.resnet18(pretrained=True)
    modules=list(resnet18.children())[:-1]
    model=nn.Sequential(*modules)
    for p in model.parameters():
                p.requires_grad = False

    #model.eval()
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])


    datas = {}

    for i in d:
        fn = fpath + i["video_id"] + ext

        try:
            input_image = Image.open(fn)
        except:
            continue
        print(input_image.size)

        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            model.to('cuda')

        with torch.no_grad():
            output = model(input_batch)
        output = output.squeeze()

        d = output.cpu().detach().numpy()
        #d = ' '.join([str(i) for i in d])
        datas[i["id"]] = [str(i) for i in d]#d#str(output.cpu().detach().numpy())

        print(output.shape) # (1, 512, 1, 1)

        '''
        # Tensor of shape 1000, with confidence scores over Imagenet's 1000 classes
        print(output[0])
        # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
        print(torch.nn.functional.softmax(output[0], dim=0))
        '''
        #time.sleep(10)

    json.dump(datas, new_jsonfile)#, indent='\t')
