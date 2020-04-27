from os_image_handler import image_handler as ih

##################################################################################
#
# this is a simple module for the creation of a feature graphic for Android
#
##################################################################################

# finals
OUTPUT_WIDTH = 1024
OUTPUT_HEIGHT = 500


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
                           logo_distance_from_top=40):
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

    # create a background canvas with a background gradient color
    background = ih.create_new_image(OUTPUT_WIDTH, OUTPUT_HEIGHT, fixed_background_hex_color, gradient_background_hex_color_start, gradient_background_hex_color_end)

    # calculate centers
    center_point_x = background.width / 2
    center_point_y = background.height / 2

    # add text
    if app_name is not None:
        font_size = app_name_max_font_size
        if len(app_name) > 38:
            font_size = 20
        ih.draw_text_on_img(background, app_name, center_point_x - (len(app_name) * font_size / 2) / 1.8, app_name_distance_from_top, app_name_font_color_hex, app_name_custom_font_path, font_size)

    # add the logo
    logo_img = ih.load_img(logo_path)
    logo_img = ih.resize_img_by_width(logo_img, logo_max_width_pixels)
    ih.paste_image(background, logo_img, center_point_x - logo_img.width / 2, logo_distance_from_top)

    # save
    ih.save_img(background, output_path)
