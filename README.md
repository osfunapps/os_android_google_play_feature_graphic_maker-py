Introduction
------------

This script will create a simple feature graphic for you to use in the Google Play store.

## Installation
Install via pip:

    pip install os-android-feature-graphic-maker

## Usage       

    import os_android_feature_graphic_maker.feature_graphic_maker as fgm
    
    fgm.create_feature_graphic(logo_path='/Users/home/Desktop/icons/chubby_logo.png',
                               output_path='/Users/home/Desktop/icons/feature_graphic.png',
                               gradient_background_hex_color_start='#ed4264',
                               gradient_background_hex_color_end='#ffedbc',
                               app_name='Catch The Chubby Hedgehog!',
                               app_name_custom_font_path='/Users/home/Library/Fonts/Consolas.ttf')
    

## output
![Output](/images/feature_graphic.png)

## Function Signature
    def create_feature_graphic(logo_path,
                           output_path,
                           fixed_background_hex_color=None,
                           gradient_background_hex_color_start=None,
                           gradient_background_hex_color_end=None,
                           app_name=None,
                           app_name_font_color_hex='#ffffff',
                           app_name_custom_font_path=None,
                           app_name_max_font_size=32,
                           app_name_distance_from_top=390,
                           logo_max_width_pixels=300,
                           logo_distance_from_top=40)
    """Will create the feature graphic.

    Parameters:
    :param logo_path: the path to your logo file
    :param output_path: the path to which the feature graphic image will be saved
    :param fixed_background_hex_color: if you would like to use a fixed hex for the background, set it here
    :param gradient_background_hex_color_start: if you would like to use a dynamic background, set the start color here
    :param gradient_background_hex_color_end: if you would like to use a dynamic background, set the end color here
    :param app_name: the name of your app
    :param app_name_font_color_hex: the color of your app name
    :param app_name_custom_font_path: you can use a custom font for your app name. Just set it here
    :param app_name_max_font_size: if the size is too big/small for you, you can set here a new static size
    :param app_name_distance_from_top: set here the distance of the app name, from the image top
    :param logo_max_width_pixels: the maximum width of the image (the height will be scaled proportionally
    :param logo_distance_from_top: the distance of the logo from the top
    """
    


## Licence
MIT