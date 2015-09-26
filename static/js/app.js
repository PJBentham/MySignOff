var canvas=document.getElementById("signatureCanvas");
    
var signaturePad = null;

signaturePad = new SignaturePad(canvas);
signaturePad.minWidth = 1;
signaturePad.maxWidth = 2;
signaturePad.penColor = "rgb(4, 4, 4)";

clearButton.addEventListener("click", function (event) {
    signaturePad.clear();
    input.value = '';
    return false;
});

var input = document.getElementById("signature");

//PHP would be $_POST['signature']

canvas.addEventListener("mouseup", function(event) {
    if ( signaturePad.isEmpty() ) {
        input.value = '';
    } else {
        input.value = signaturePad.toDataURL();
    }
});