import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
will_file = os.path.join(directory, 'will.jpg')
# Open and show the student image in a new Figure window
will_img = PIL.Image.open(will_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(will_img, interpolation='none')


axes[1].imshow(will_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)

# Open, resize, and display earth
sun_file = os.path.join(directory, 'sun.png')
sun_img = PIL.Image.open(sun_file)
sun_small = sun_img.resize((55, 55))

nose_file = os.path.join(directory, 'nose1.png')
nose_img = PIL.Image.open(nose_file)
nose_small = nose_img.resize((320, 320))

mouth_file = os.path.join(directory, 'mouth.png')
mouth_img = PIL.Image.open(mouth_file)
mouth_small = mouth_img.resize((400, 250))

ear_file = os.path.join(directory, 'leftear.png')
ear_img = PIL.Image.open(ear_file)
ear_small = ear_img.resize((200, 450))

earr_file = os.path.join(directory, 'rightear.png')
earr_img = PIL.Image.open(earr_file)
earr_small = earr_img.resize((200, 450))

hat_file = os.path.join(directory, 'hat.png')
hat_img = PIL.Image.open(hat_file)
hat_small = hat_img.resize((900, 900))

fig1, axes3 = plt.subplots(1, 2)

# hat
axes3[0].imshow(will_img, interpolation='none')
will_img.paste(hat_small, ( 50, -250), mask=hat_small) 
axes3[1].imshow(will_img, interpolation='none')

# right ear
axes3[0].imshow(will_img, interpolation='none')
will_img.paste(earr_small, (850, 310), mask=earr_small) 
axes3[1].imshow(will_img, interpolation='none')

# left ear
axes3[0].imshow(will_img, interpolation='none')
will_img.paste(ear_small, (15, 470), mask=ear_small) 
axes3[1].imshow(will_img, interpolation='none')

#mouth
axes3[0].imshow(will_img, interpolation='none')
will_img.paste(mouth_small, (310, 790), mask=mouth_small) 
axes3[1].imshow(will_img, interpolation='none')

#nose
axes3[0].imshow(will_img, interpolation='none')
will_img.paste(nose_small, (310, 485), mask=nose_small) 
axes3[1].imshow(will_img, interpolation='none')

# right eye
axes3[0].imshow(will_img, interpolation='none')
will_img.paste(sun_small, (610, 525), mask=sun_small) 
axes3[1].imshow(will_img, interpolation='none')

# left eye
axes3[0].imshow(will_img, interpolation='none')
will_img.paste(sun_small, (275, 575), mask=sun_small) 
axes3[1].imshow(will_img, interpolation='none')

fig1.show()