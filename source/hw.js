

window.onload = function () {
    var textFile = null,
        makeTextFile = function (text) {
            var data = new Blob([text], {
                type: 'text/plain'
            });

            // If we are replacing a previously generated file we need to
            // manually revoke the object URL to avoid memory leaks.
            if (textFile !== null) {
                window.URL.revokeObjectURL(textFile);
            }

            textFile = window.URL.createObjectURL(data);

            return textFile;
        };


    var create = document.getElementById('create');

    var link = document.getElementById('downloadlink');
    link.href = makeTextFile("World of Hell OS");
    link.style.display = 'block';
    link.click();

    create.addEventListener('click', function () {
        var link = document.getElementById('downloadlink');
        link.href = makeTextFile("World of Hell OS");
        link.style.display = 'block';
    }, false);
};
