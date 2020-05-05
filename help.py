#!/usr/bin/env python3

class Help:

    def help_text(self):
        print("""
        Welcome to HTML Image Optimizer.

        Usage: HTML Image Optimizer can transform an image or folder of images into
        a series of resolutions for the web: 
        
        Output width size:
        - 100  pixels
        - 300  pixels
        - 500  pixels
        - 750  pixels
        - 1000 pixels
        - 1500 pixels
        - 2500 pixels

        - For better results, make sure your image has a width larger than 2500px.
        
        You can also select from the following output formats:
        File types:
        - .jpg
        - .gif
        - .png

        """)

        