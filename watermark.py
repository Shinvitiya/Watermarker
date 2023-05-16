from PIL import Image, ImageDraw, ImageFont


class WatermarkAdder:

    def __init__(self, image_path, watermark_text, fontsize, image_final_path):
        self.im_path = image_path
        self.im_final_path = image_final_path
        self.im = Image.open(image_path)
        self.width, self.height = self.im.size

        self.draw = ImageDraw.Draw(self.im)
        self.text = watermark_text

        self.font = ImageFont.truetype("arial.ttf", fontsize)
        self.textwidth, self.textheight = self.draw.textsize(self.text, self.font)
        self.generate()

    def generate(self):
        margin = 15
        xcor = self.width - self.textwidth - margin
        ycor = self.height - self.textheight - margin
        self.draw.text((xcor, ycor), self.text, font=self.font,)
        self.im.save(self.im_final_path)






