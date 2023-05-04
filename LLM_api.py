from Image_captioning import generate_caption
import poe
client = poe.Client("pqwbrzjCafmAXogA2g7luA%3D%3D") 
has_image= True


def reply(message,has_image,sample_img):
   if has_image:
      caption = generate_caption(sample_img)
      message =  "assume that I showed you a photo that: " + caption + ". now, given the information about the photo, I'll tell you this: " + message
   for chunk in client.send_message("nutria", message):
      print(chunk["text_new"], end="")
    

def reply_with_photo(message,has_image,sample_img):
    if has_image:
      caption = generate_caption(sample_img)
      message =  "assume that I showed you a photo that: " + caption + ". now, given the information about the photo, I'll tell you this: " + message
    output_list = []
    result = []
    for chunk in client.send_message("nutria", message):
      output_list.append(chunk["text_new"])
    my_string = "".join(output_list)
    my_list = my_string.split("\n")

    # Calling google search api
    if my_list[1]=="Yes":
        # use my_list[3] as it contains the description of the photo required and you have to make a function that returns an image and put it in the return of the reply function.
        pass
    return my_list[5]

reply("what is this kind of sport",0,"")
print("\n\n\n\n","------------------------------------------------------------------","\n\n\n\n")
reply("what is this kind of sport",1,"download.jpeg")
