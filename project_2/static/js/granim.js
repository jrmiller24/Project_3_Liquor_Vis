var granimInstance = new Granim({
    element: '#canvas-image-blending',
    direction: 'top-bottom',
    isPausedWhenNotInView: true,
    image : {
        // source: '../assets/img/bg-forest.jpg',
        //lets see if this works. If it doesn't, we'll download the file into your `static` folder 
        source: 'https://sarcadass.github.io/granim.js/assets/img/bg-forest.jpg',
        blendingMode: 'color',
    },
    states : {
        "default-state": {
            gradients: [
                ['#29323c', '#485563'],
                ['#FF6B6B', '#556270'],
                ['#80d3fe', '#7ea0c4'],
                ['#f0ab51', '#eceba3']
            ],
            transitionSpeed: 7000
        }
    }
});