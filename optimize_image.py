from PIL import Image
import os

source_path = r"C:\Users\trade\.gemini\antigravity\brain\94af8ec2-bd42-4f8e-af0e-c675ed6e2e28\uploaded_image_1764576104681.png"
dest_path = r"C:\Users\trade\Projects\CLIENTS\renaror\renaror-images\hero-service-van.jpg"

try:
    with Image.open(source_path) as img:
        # Convert to RGB if necessary (e.g. if PNG has alpha channel)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
            
        # Resize if width > 1920
        if img.width > 1920:
            ratio = 1920 / img.width
            new_height = int(img.height * ratio)
            img = img.resize((1920, new_height), Image.Resampling.LANCZOS)
            print(f"Resized to 1920x{new_height}")
        else:
            print(f"Original size kept: {img.width}x{img.height}")

        # Save as optimized JPEG
        img.save(dest_path, "JPEG", quality=85, optimize=True)
        
        print(f"Successfully saved optimized image to {dest_path}")
        print(f"New file size: {os.path.getsize(dest_path)} bytes")

except Exception as e:
    print(f"Error: {e}")
