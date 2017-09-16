import requests
from ffmpy import FFmpeg
#pip install ffmpy
#pip3 install ffmpy

def random_sad_images():
	r = requests.get('http://api.giphy.com/v1/gifs/random?tag=sad&api_key=0db4fdd98a4a49ccb3842eb47cb0d04a')
	json = r.json()
	id = json['data']['id']
	imageurl = 'https://i.giphy.com/media/' + id + '/giphy.gif'
	return imageurl

random_sad_images()

FFmpeg(
	inputs={'https://i.giphy.com/media/10tIjpzIu8fe0/giphy.gif': None},
	outputs={'output.gif': ["-vf \"drawtext=fontfile=/usr/share/fonts/default/Type1/n019003l.pfb:text='hey': fontcolor=white: fontsize=24: box=1: boxcolor=black@0.5:boxborderw=5: x=(w-text_w)/2: y=(h-text_h)-2\" -an"}
)

if __name__ == '__main__':
    ff.run()
