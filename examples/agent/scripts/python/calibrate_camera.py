#!/usr/bin/env python3
from itertools import cycle

import cv2
import depthai as dai

"""
Modified from https://github.com/luxonis/depthai-python/blob/main/examples/ColorCamera/rgb_camera_control.py

This example shows usage of Camera Control message as well as ColorCamera configInput to change crop x and y.
"""

script_help = """--- LUXONIS RGB CAMERA CALIBRATION ---

Crop window:
    'WASD' - controls to move the crop window
    'YX'   - to decrease or increase the crop window's width
    'CV'   - to decrease or increase the crop window's height

Sensor controls:
    Control:      key[dec/inc]  min..max
    exposure time:     I   O      1..33000 [us]
    sensitivity iso:   K   L    100..1600
    focus:             ,   .      0..255 [far..near]
    white balance:     N   M   1000..12000 (light color temperature K)

To go back to auto controls:
    'E' - autoexposure
    'F' - autofocus (continuous)
    'B' - auto white-balance

Other controls:
    'T' - autofocus lock (true / false)
    '1' - AWB lock (true / false)
    '2' - AE lock (true / false)
    '3' - Select control: AWB mode
    '4' - Select control: AE compensation
    '5' - Select control: anti-banding/flicker mode
    '6' - Select control: effect mode
    '7' - Select control: brightness
    '8' - Select control: contrast
    '9' - Select control: saturation
    '0' - Select control: sharpness
    '[' - Select control: luma denoise
    ']' - Select control: chroma denoise

For the 'Select control: ...' options, use these keys to modify the value:
    '-' or '_' to decrease
    '+' or '=' to increase

'/' to toggle showing camera settings: exposure, ISO, lens position, color temperature

'p' to print the camera configuration to use with the AVIS agent

EXIT >> Press 'q' to exit the application
----
"""

# Step size ('W','A','S','D' controls)
STEP_SIZE = 12  # px - Needs to be divisible by WIDTH_DIVISOR and HEIGHT_DIVISOR
# Manual exposure/focus/white-balance set step
EXP_STEP = 500  # us
ISO_STEP = 50
LENS_STEP = 3
WB_STEP = 200
WIDTH_DIVISOR = 2
HEIGHT_DIVISOR = 3

CV2_WINDOW_NAME = "Camera Calibration"


def clamp(num, v0, v1):
    return max(v0, min(num, v1))


def draw_crosshair(frame, center_x: int, center_y: int):
    """Draw a red crosshair at the center location"""
    length = 20

    cv2.line(
        frame,
        (center_x - length, center_y),
        (center_x + length, center_y),
        (0, 0, 255),
        2,
    )  # Horizontal line
    cv2.line(
        frame,
        (center_x, center_y - length),
        (center_x, center_y + length),
        (0, 0, 255),
        2,
    )  # Vertical line


def closest_divisible_number(n: int, divisor: int) -> int:
    """Find the closest number divisible by the divisor.

    Args:
        n (int): Number to find the closest divisible number for
        divisor (int): Divisor to use

    Returns:
        (int): Closest number divisible by the divisor
    """
    # Finding the nearest multiple below the given number
    lower = n - (n % divisor)

    # Finding the nearest multiple above the given number
    upper = (n + divisor) - (n % divisor)

    # Check which of the two is closer to the original number
    if n - lower < upper - n:
        return lower
    else:
        return upper


# Create pipeline
pipeline = dai.Pipeline()

# Define sources and outputs
camRgb = pipeline.create(dai.node.ColorCamera)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setIspScale(2, 3)  # Go from 1080p to 720p (1280x720)

controlIn = pipeline.create(dai.node.XLinkIn)
configIn = pipeline.create(dai.node.XLinkIn)
videoOut = pipeline.create(dai.node.XLinkOut)

controlIn.setStreamName("control")
configIn.setStreamName("config")
videoOut.setStreamName("video")

# Linking
camRgb.video.link(videoOut.input)
controlIn.out.link(camRgb.inputControl)
configIn.out.link(camRgb.inputConfig)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:
    # Get data queues
    controlQueue = device.getInputQueue("control")
    configQueue = device.getInputQueue("config")
    videoQueue = device.getOutputQueue("video")

    # Defaults and limits for manual focus/exposure controls
    auto_focus = True
    lensPos = 150
    expTime = 20000
    sensIso = 800
    wbManual = 4000
    ae_comp = 0
    ae_lock = False
    awb_lock = False
    saturation = 0
    contrast = 0
    brightness = 0
    sharpness = 0
    luma_denoise = 0
    chroma_denoise = 0
    control = "none"
    show = False

    awb_mode = cycle(
        [
            item
            for name, item in vars(dai.CameraControl.AutoWhiteBalanceMode).items()
            if name.isupper()
        ]
    )
    anti_banding_mode = cycle(
        [
            item
            for name, item in vars(dai.CameraControl.AntiBandingMode).items()
            if name.isupper()
        ]
    )
    effect_mode = cycle(
        [
            item
            for name, item in vars(dai.CameraControl.EffectMode).items()
            if name.isupper()
        ]
    )

    # Print the instructions on how to use the calibration script
    print(script_help)

    # Print information about the size of the video
    print(f"ISP Video Dimensions: {camRgb.getIspWidth()}x{camRgb.getIspHeight()}")

    # Default dimensions for the cropped area
    crop_width = closest_divisible_number(
        int(0.2 * camRgb.getIspWidth()), WIDTH_DIVISOR
    )
    crop_height = closest_divisible_number(crop_width, HEIGHT_DIVISOR)
    crop_x = int(camRgb.getVideoWidth() / 2 - crop_width / 2)
    crop_y = int(camRgb.getVideoHeight() / 2 - crop_height / 2)
    update_crop = True

    while True:
        videoFrames = videoQueue.tryGetAll()
        for videoFrame in videoFrames:
            if show:
                txt = f"[{videoFrame.getSequenceNum()}] "
                txt += f"Exposure: {videoFrame.getExposureTime().total_seconds() * 1000:.3f} ms, "
                txt += f"ISO: {videoFrame.getSensitivity()}, "
                txt += f"Lens position: {videoFrame.getLensPosition()}, "
                txt += f"Color temp: {videoFrame.getColorTemperature()} K"
                print(txt)

            frame = videoFrame.getCvFrame()
            draw_crosshair(
                frame=frame,
                center_x=int(crop_x + crop_width / 2),
                center_y=int(crop_y + crop_height / 2),
            )

            cv2.rectangle(
                frame,
                (crop_x, crop_y),
                (crop_x + crop_width, crop_y + crop_height),
                (0, 0, 255),
                2,
            )

            cv2.imshow(CV2_WINDOW_NAME, frame)

            if update_crop:
                print(
                    f"Crop area: xmin = {crop_x/camRgb.getIspWidth()}, ymin = {crop_y/camRgb.getIspHeight()}, xmax = {(crop_x+crop_width)/camRgb.getIspWidth()}, ymax = {(crop_y+crop_height)/camRgb.getIspHeight()}"
                )
                update_crop = False

        # Update screen (1ms pooling rate)
        key = cv2.waitKey(1)
        if key == ord("q"):
            print("Exiting the application...")
            break
        elif key == ord("/"):
            show = not show
            if not show:
                print("Printing camera settings: OFF")
        elif key in [ord("p")]:
            print(
                f"""
'camera': {{
    'image_path': PosixPath('image.png'),
    'name': 'oak_d_poe',
    'resolution': '1080p',
    'fixed_focus': {None if auto_focus else lensPos},
    'crop': {{
        'xmin': {crop_x/camRgb.getIspWidth()},
        'xmax': {(crop_x+crop_width)/camRgb.getIspWidth()},
        'ymin': {crop_y/camRgb.getIspHeight()},
        'ymax': {(crop_y+crop_height)/camRgb.getIspHeight()},
    }}
}}
        """
            )
        elif key == ord("t"):
            print("Autofocus trigger (and disable continuous)")
            ctrl = dai.CameraControl()
            ctrl.setAutoFocusMode(dai.CameraControl.AutoFocusMode.AUTO)
            ctrl.setAutoFocusTrigger()
            controlQueue.send(ctrl)
        elif key == ord("f"):
            print("Autofocus enable, continuous")
            ctrl = dai.CameraControl()
            ctrl.setAutoFocusMode(dai.CameraControl.AutoFocusMode.CONTINUOUS_VIDEO)
            controlQueue.send(ctrl)
            auto_focus = True
        elif key == ord("e"):
            print("Autoexposure enable")
            ctrl = dai.CameraControl()
            ctrl.setAutoExposureEnable()
            controlQueue.send(ctrl)
        elif key == ord("b"):
            print("Auto white-balance enable")
            ctrl = dai.CameraControl()
            ctrl.setAutoWhiteBalanceMode(dai.CameraControl.AutoWhiteBalanceMode.AUTO)
            controlQueue.send(ctrl)
        elif key in [ord(","), ord(".")]:
            if key == ord(","):
                lensPos -= LENS_STEP
            if key == ord("."):
                lensPos += LENS_STEP
            lensPos = clamp(lensPos, 0, 255)
            print("Setting manual focus, lens position: ", lensPos)
            ctrl = dai.CameraControl()
            ctrl.setManualFocus(lensPos)
            controlQueue.send(ctrl)
            auto_focus = False
        elif key in [ord("i"), ord("o"), ord("k"), ord("l")]:
            if key == ord("i"):
                expTime -= EXP_STEP
            if key == ord("o"):
                expTime += EXP_STEP
            if key == ord("k"):
                sensIso -= ISO_STEP
            if key == ord("l"):
                sensIso += ISO_STEP
            expTime = clamp(expTime, 1, 33000)
            sensIso = clamp(sensIso, 100, 1600)
            print("Setting manual exposure, time: ", expTime, "iso: ", sensIso)
            ctrl = dai.CameraControl()
            ctrl.setManualExposure(expTime, sensIso)
            controlQueue.send(ctrl)
        elif key in [ord("n"), ord("m")]:
            if key == ord("n"):
                wbManual -= WB_STEP
            if key == ord("m"):
                wbManual += WB_STEP
            wbManual = clamp(wbManual, 1000, 12000)
            print("Setting manual white balance, temperature: ", wbManual, "K")
            ctrl = dai.CameraControl()
            ctrl.setManualWhiteBalance(wbManual)
            controlQueue.send(ctrl)
        elif key in [
            ord("w"),
            ord("a"),
            ord("s"),
            ord("d"),
            ord("y"),
            ord("x"),
            ord("c"),
            ord("v"),
        ]:
            # Move left
            if key == ord("a"):
                crop_x -= STEP_SIZE
                if crop_x < 0:
                    crop_x = 0
            # Move right
            elif key == ord("d"):
                crop_x += STEP_SIZE
                if crop_x + crop_width > camRgb.getIspWidth():
                    crop_x = camRgb.getIspWidth() - crop_width
            # Move up
            elif key == ord("w"):
                crop_y -= STEP_SIZE
                if crop_y < 0:
                    crop_y = 0
            # Move down
            elif key == ord("s"):
                crop_y += STEP_SIZE
                if crop_y + crop_height > camRgb.getIspHeight():
                    crop_y = camRgb.getIspHeight() - crop_height
            # Decrease width
            elif key == ord("y"):
                crop_width -= STEP_SIZE
                if crop_width < STEP_SIZE:
                    crop_width = STEP_SIZE
            # Increase width
            elif key == ord("x"):
                crop_width += STEP_SIZE
                if crop_x + crop_width > camRgb.getIspWidth():
                    crop_width -= STEP_SIZE  # Undo
            # Decrease height
            elif key == ord("c"):
                crop_height -= STEP_SIZE
                if crop_height < STEP_SIZE:
                    crop_height = STEP_SIZE
            # Increase height
            elif key == ord("v"):
                crop_height += STEP_SIZE
                if crop_y + crop_height > camRgb.getIspHeight():
                    crop_height -= STEP_SIZE  # Undo
            update_crop = True
        elif key == ord("1"):
            awb_lock = not awb_lock
            print("Auto white balance lock:", awb_lock)
            ctrl = dai.CameraControl()
            ctrl.setAutoWhiteBalanceLock(awb_lock)
            controlQueue.send(ctrl)
        elif key == ord("2"):
            ae_lock = not ae_lock
            print("Auto exposure lock:", ae_lock)
            ctrl = dai.CameraControl()
            ctrl.setAutoExposureLock(ae_lock)
            controlQueue.send(ctrl)
        elif key >= 0 and chr(key) in "34567890[]":
            if key == ord("3"):
                control = "awb_mode"
            elif key == ord("4"):
                control = "ae_comp"
            elif key == ord("5"):
                control = "anti_banding_mode"
            elif key == ord("6"):
                control = "effect_mode"
            elif key == ord("7"):
                control = "brightness"
            elif key == ord("8"):
                control = "contrast"
            elif key == ord("9"):
                control = "saturation"
            elif key == ord("0"):
                control = "sharpness"
            elif key == ord("["):
                control = "luma_denoise"
            elif key == ord("]"):
                control = "chroma_denoise"
            print("Selected control:", control)
        elif key in [ord("-"), ord("_"), ord("+"), ord("=")]:
            change = 0
            if key in [ord("-"), ord("_")]:
                change = -1
            if key in [ord("+"), ord("=")]:
                change = 1
            ctrl = dai.CameraControl()
            if control == "none":
                print("Please select a control first using keys 3..9 0 [ ]")
            elif control == "ae_comp":
                ae_comp = clamp(ae_comp + change, -9, 9)
                print("Auto exposure compensation:", ae_comp)
                ctrl.setAutoExposureCompensation(ae_comp)
            elif control == "anti_banding_mode":
                abm = next(anti_banding_mode)
                print("Anti-banding mode:", abm)
                ctrl.setAntiBandingMode(abm)
            elif control == "awb_mode":
                awb = next(awb_mode)
                print("Auto white balance mode:", awb)
                ctrl.setAutoWhiteBalanceMode(awb)
            elif control == "effect_mode":
                eff = next(effect_mode)
                print("Effect mode:", eff)
                ctrl.setEffectMode(eff)
            elif control == "brightness":
                brightness = clamp(brightness + change, -10, 10)
                print("Brightness:", brightness)
                ctrl.setBrightness(brightness)
            elif control == "contrast":
                contrast = clamp(contrast + change, -10, 10)
                print("Contrast:", contrast)
                ctrl.setContrast(contrast)
            elif control == "saturation":
                saturation = clamp(saturation + change, -10, 10)
                print("Saturation:", saturation)
                ctrl.setSaturation(saturation)
            elif control == "sharpness":
                sharpness = clamp(sharpness + change, 0, 4)
                print("Sharpness:", sharpness)
                ctrl.setSharpness(sharpness)
            elif control == "luma_denoise":
                luma_denoise = clamp(luma_denoise + change, 0, 4)
                print("Luma denoise:", luma_denoise)
                ctrl.setLumaDenoise(luma_denoise)
            elif control == "chroma_denoise":
                chroma_denoise = clamp(chroma_denoise + change, 0, 4)
                print("Chroma denoise:", chroma_denoise)
                ctrl.setChromaDenoise(chroma_denoise)
            controlQueue.send(ctrl)
