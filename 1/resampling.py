from PIL import Image

# Load the original image
original_image = Image.open(r"C:\Users\jayda\OneDrive\Desktop\IP Practical\1\sample.jpg")

# Define the sizes for subsampling
sizes = [(512, 512), (256, 256), (128, 128), (64, 64), (32, 32)]

# Subsample the original image
subsampled_images = [original_image.resize(size) for size in sizes]

# Save the subsampled images
for i, size in enumerate(sizes):
    subsampled_images[i].save(f"subsampled_image_{size[0]}x{size[1]}.jpg")

# Resample the subsampled images to reconstruct the original image
resampled_images = [image.resize((1024, 1024), Image.LANCZOS) for image in subsampled_images]

# Save the resampled images
for i, size in enumerate(sizes):
    resampled_images[i].save(f"resampled_image_{size[0]}x{size[1]}.jpg")
