#SUMMARY = "My test videos"
#DESCRIPTION = "Test Videos"
#HOMEPAGE = ""
LICENSE = "CLOSED"
LIC_FILES_CHKSUM = ""

SRC_URI = "file://DETECTOR.py \
	   file://emotion_detection_model_200epochs_no_opt.tflite \
	   file://haarcascade_frontalface_default.xml "

S = "${WORKDIR}"

TARGET_CC_ARCH += "${LDFLAGS}"

#FILES_${PN} += "${libdir}/*"
#FILES_${PN}-dev = "${libdir}/* ${includedir}"


do_install () {
   install -d ${D}${bindir}/PROYECTO
   install -m 0755 DETECTOR.py ${D}${bindir}/PROYECTO
   install -m 0755 emotion_detection_model_200epochs_no_opt.tflite ${D}${bindir}/PROYECTO
   install -m 0755 haarcascade_frontalface_default.xml ${D}${bindir}/PROYECTO
}
