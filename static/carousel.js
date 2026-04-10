document.addEventListener('DOMContentLoaded', function () {
    var nextArrow = document.querySelector('.carousel-arrow-next');
    var prevArrow = document.querySelector('.carousel-arrow-prev');

    if (nextArrow) {
        nextArrow.addEventListener('click', carouselSwipe, false);
    }
    if (prevArrow) {
        prevArrow.addEventListener('click', carouselSwipe, false);
    }
});

function carouselSwipe() {
    var displayedImgs = document.getElementsByClassName('carousel-img-displayed');
    if (displayedImgs.length === 0) return;

    // Get current image ID string like 'carousel-0' and extract the number '0'
    var currentImgStr = displayedImgs[0].id.substring(9);
    var currentImgIdx = parseInt(currentImgStr);

    var totalImgs = document.getElementsByClassName('carousel-img').length;
    var newImgIdx = currentImgIdx;

    if (this.classList.contains('carousel-arrow-next')) {
        newImgIdx++;
        if (newImgIdx >= totalImgs) {
            newImgIdx = 0;
        }
    } else if (this.classList.contains('carousel-arrow-prev')) {
        newImgIdx--;
        if (newImgIdx < 0) {
            newImgIdx = totalImgs - 1;
        }
    }

    // Hide the current image
    document.getElementById('carousel-' + currentImgIdx).classList.remove('carousel-img-displayed');

    // Display the new image
    document.getElementById('carousel-' + newImgIdx).classList.add('carousel-img-displayed');
}