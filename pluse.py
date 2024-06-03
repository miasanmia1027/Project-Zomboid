from PIL import ImageGrab

# Capture the entire screen
screenshot = ImageGrab.grab()

# Save the screenshot to a file
screenshot.save("screenshot.png")

# Close the screenshot
screenshot.close()


# Capture a specific region (left, top, right, bottom)
screenshot = ImageGrab.grab(bbox=(100, 100, 500, 500))
#특정 부분을 캡처 할때



