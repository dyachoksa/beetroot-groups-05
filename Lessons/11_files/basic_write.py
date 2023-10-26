f = open("data_write.txt", "w")

f.write("""Line 1
Line 2
Line 3""")

# or
# f.writelines([
#     "Line 1",
#     "Line 2",
#     "Line 3",
# ])

f.close()
