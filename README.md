python 3.7
----------------------------------------------------------------------------------------------


### Description
This Repository is a Django Based API to extract signature from signature Image using opencv-python. The main aim is to remove the background and make it as a transparent image.

![ezgif com-video-to-gif](https://github.com/Dimensions-Limited/signature_extractor_api/assets/68796875/265a6283-c19e-41bc-aff5-1279eac096d0)


### Installation

```BibTeX
git clone git@github.com:shkhamza143/signature_extractor_api.git
cd signature_extractor_api
pip install -r requirements.txt
```


### To Do's
- Object Detection Algorithm to Detect Signatures From document
- Extract Signature Image 
- Paste Signature to Any other document


### Inference
		
```BibTeX
- python manage.py runserver
- Open Postman and paste the given IP Address.
- Send the file attribute witth file type.
- Browse The image, and hit send.
- The Givene Generated link would be a transpaernt Image
```


## Citing SignatureExtractorAPI

If you use SignatureExtractorAPI in your research, please use the following BibTeX entry.

```BibTeX
@misc{wu2019detectron2,
  author =       {Hamza Naeem},
  title =        {Signature Extractor API},
  howpublished = {\url{https://github.com/facebookresearch/detectron2}},
  year =         {2023}
}
```
