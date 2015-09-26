//Jquery for datepicker:

//Signature Canvas Script
var canvas=document.getElementById("signatureCanvas");
canvas.width = 300;
canvas.height = 100;
var signaturePad = null;

signaturePad = new SignaturePad(canvas);
signaturePad.minWidth = 1;
signaturePad.maxWidth = 2;
signaturePad.penColor = "rgb(2, 10, 666)";

//Empty signature box if 'clear' clicked
clearButton.addEventListener("click", function (event) {
  	signaturePad.clear();
  	input.value = '';
  	return false;
});

var input = document.getElementById("signature");

canvas.addEventListener("touchend", function(event) {
  	if ( signaturePad.isEmpty() ) {
      	input.value = '';
  	} else {
  	    input.value = signaturePad.toDataURL();
  	}
});

canvas.addEventListener("mouseup", function(event) {
  	if ( signaturePad.isEmpty() ) {
      	input.value = '';
  	} else {
  	    input.value = signaturePad.toDataURL();
  	}
});	

//Check Signature is complete
function CheckForm(){
	var x=document.forms["mainForm"]["signature"].value;
	if (x==null || x==""){
			return false;
		}
		else {
			return true;
		}
	};
