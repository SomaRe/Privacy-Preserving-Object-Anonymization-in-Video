from PIL import Image

def process_batch(batch):
    for image_dir, image in batch:
        # get the image name
        image_name = image.split("/")[-1]
        # get the image width and height
        image_width, image_height = Image.open(image_dir+"/"+image).size
        # get the image label
        image_label = (image_dir+"/"+image).replace("images", "labels").replace(".jpg", ".txt")
        # get the image label name
        image_label_name = image_label.split("/")[-1]
        # break the image name into parts
        image_name_parts = image_name.split("-")
        xy = []
        for i in range(len(image_name_parts[2].split("_"))):
            xy.append(image_name_parts[2].split("_")[i].split("&"))
            xy = [list(map(int, x)) for x in xy]
        # get bounding box coordinates
        xmin = xy[0][0]
        ymin = xy[0][1]
        xmax = xy[1][0]
        ymax = xy[1][1]

        # print x_center, y_center, width, height in ratios
        x_center = (xmin + xmax) / (2 * image_width)
        y_center = (ymin + ymax) / (2 * image_height)
        width = (xmax - xmin) / image_width
        height = (ymax - ymin) / image_height
        # write the bounding box coordinates to the txt file
        with open(image_label, "w") as f:
            f.write(f"0 {x_center} {y_center} {width} {height}")

        # close the file
        f.close()

        print(f"Creating labels {image_dir.split('/')[-1]}")

