import os_android_feature_graphic_maker.feature_graphic_maker as fgm

fgm.create_feature_graphic(logo_path='/Users/home/Desktop/icons/chubby_logo.png',
                           output_path='/Users/home/Desktop/icons/feature_graphic.png',
                           gradient_background_hex_color_start='#ed4264',
                           gradient_background_hex_color_end='#ffedbc',
                           app_name='Catch The Chubby Hedgehog!',
                           app_name_custom_font_path='/Users/home/Library/Fonts/Consolas.ttf')
