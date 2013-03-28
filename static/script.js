//hide addbook more details form initially
$(function(){$(".moreDetailsForm").hide();});

//addbook form toggler
$(function(){$(".addBookClickable").click(function(){$(".addBookForm").slideToggle();})});

//addbook more details toggler
$(function(){$(".moreDetailsClickable").click(function(){$(".moreDetailsForm").slideToggle();});});

function imageSelected(link){
	document.getElementById('googleImage').value = link;
}
