from rembg import remove
import os


def rembg(input_path, output_path):
	with open(input_path,'rb') as i:
		with open(output_path,'wb') as o:
			input = i.read()
			output = remove(input)
			o.write(output)



if __name__ == "__main__":
	rembg("image.webp","output.png")