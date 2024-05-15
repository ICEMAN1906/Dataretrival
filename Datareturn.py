# Define the drive where the data is stored
Drive = "\\\\.\\C:"

# Open the file in binary read mode
File = open(Drive, "rb")

# Set the size of the chunks to read
size = 4096

# Read the first chunk of data
byte = File.read(size)

# Initialize variables
offs = 0  # Offset for keeping track of the current position in the file
rcvd = 0  # Counter for the number of files recovered

# Define the signatures for JPG and PNG files
jpg_signature = b'\xff\xd8\xff\xe0\x00\x10\x4a\x46'
png_signature = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

# Main loop for reading and processing the file
while byte:
    # Search for the signatures in the current chunk
    jpg_found = byte.find(jpg_signature)
    png_found = byte.find(png_signature)

    # If a JPG signature is found
    if jpg_found >= 0:
        # Print the location of the JPG signature in the file
        print('---------Found JPG at Location:' + str(hex(jpg_found + (size * offs))) + '---------')

        # Open a new file to write the recovered JPG
        with open('1\\' + str(rcvd) + ".jpg", "wb") as FileA:
            # Write the current chunk from the found signature to the end of the chunk
            FileA.write(byte[jpg_found:])
            rcvd += 1  # Increment the counter for recovered files


    if png_found >= 0:
        # Print the location of the PNG signature in the file
        print('---------Found PNG at Location:' + str(hex(png_found + (size * offs))) + '---------')

        # Open a new file to write the recovered PNG
        with open('1\\' + str(rcvd) + ".png", "wb") as FileA:
            # Write the current chunk from the found signature to the end of the chunk
            FileA.write(byte[png_found:])
            rcvd += 1  # Increment the counter for recovered files

    # Read the next chunk of data
    byte = File.read(size)
    offs += 1  # Increment the offset to keep track of the current position in the file


File.close()
