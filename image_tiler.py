from PIL import Image
import os
import shutil

def split_image(image_path, x, y, output_folder):
    try:
        # Open the image
        img = Image.open(image_path)
        img_width, img_height = img.size

        # Calculate tile size
        tile_width = img_width // x
        tile_height = img_height // y

        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        else:
            # Clear previous tiles in the output folder
            shutil.rmtree(output_folder)
            os.makedirs(output_folder)

        # Split the image into tiles
        for i in range(x):
            for j in range(y):
                # Define the region to crop
                left = i * tile_width
                upper = j * tile_height
                right = left + tile_width
                lower = upper + tile_height

                # Crop the image
                tile = img.crop((left, upper, right, lower))

                # Save the tile
                tile.save(f"{output_folder}/tile_{i}_{j}.png", "PNG")

        print(f"Image split into {x * y} tiles in {output_folder} folder.")

    except Exception as e:
        print(f"Error: {e}")

image_path = "world.png"  # Replace with your image path

y = 8  # zoom level
x = y * 2 

output_folder = "tiles_" + str(y)

split_image(image_path, x, y, output_folder)