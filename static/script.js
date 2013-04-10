//form validate submit validation
function validate2(){
	if($("[name='googleImage']").val().trim() == ''){
		document.getElementById("errorMsg").innerHTML = "<span id='smallCaption'>You forgot to select suitable image for this book. <br>Click on no image if you don't see any relevant image</span>";
		return false;
	}else{
		return true;
	}
}

//form submit validation
function validate(){
	if($("[name='bookTitle']").val().length <3){
		document.getElementById('bookTitleError').innerHTML = "Book name looks incorrect";
		$(".moreDetails").slideUp();
		$("[name='bookTitle']").focus();
		return false;
	}else if(isNaN($("[name='price']").val()) || $("[name='price']").val().trim()==''){		
		document.getElementById('priceError').innerHTML = "Enter the valid price.";
		$("[name='price']").focus();
		return false;		
	}else if($("[name='contact']").val().trim() == '' || $("[name='contact']").val().trim() != $("[name='verifyContact']").val().trim()){
		document.getElementById('contactError').innerHTML = "Contact information couldn't be validated";
		$("[name='contact']").focus();
		return false;
	}else{
		return true;
	}
	
}

//validation
$(function(){$("[name='price']").blur(function(){
	if(isNaN($("[name='price']").val()) || $("[name='price']").val().trim()== ''){		
		document.getElementById('priceError').innerHTML = "Enter the valid price.";		
	}else{
		document.getElementById('priceError').innerHTML = ":)";
	}
;});});



//hide addbook requireddetails form initially
$(function(){$(".moreDetails").hide();});

//auto toggle requiredDetails form
$(function(){$("#bookTitle").blur(
	function(){
		if($("[name='bookTitle']").val().length <3){
			document.getElementById('bookTitleError').innerHTML = ":(";
			$(".moreDetails").slideUp();
		}else{
			$(".moreDetails").slideDown();
			document.getElementById('bookTitleError').innerHTML = ":)";
		}
	}
)});
//manual toggle requiredDetails form
$(function(){$(".manualExpandCollapse").click(function(){$(".moreDetails").slideToggle();});});


//addbook form toggler
$(function(){$(".addBookClickable").click(function(){$(".addBookForm").slideToggle();})});


//functions
function imageSelected(link){
	document.getElementById('googleImage').value = link;
	document.getElementById('googleImgDisp').innerHTML = "<img class='googleImgDispImg' src=" + link + "></img>";

}


//analytics


