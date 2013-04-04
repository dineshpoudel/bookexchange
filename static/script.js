//validation
$(function(){$("[name='price']").blur(function(){
	if(isNaN($("[name='price']").val())){		
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



