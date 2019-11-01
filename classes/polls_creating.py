import cv2 as cv

amount_of_polls = 200
for i in range(1, amount_of_polls + 1):
    image_path = '..\\images\\poll.png'
    image = cv.imread(image_path, cv.IMREAD_UNCHANGED)
    position = (180, 200)
    if i > 9:
        position = (145, 200)
    if i > 99:
        position = (115, 200)

    cv.putText(
        image,  # numpy array on which text is written
        str(i),  # text
        position,  # position at which writing has to start
        cv.FONT_HERSHEY_SCRIPT_COMPLEX,  # font family
        3,  # font size
        (0, 0, 0),  # font color
        2)  # font stroke
    new_image_path = f'..\\images\\Polls-to-print\\{i}.png'
    cv.imwrite(new_image_path, image)
    print(i)
