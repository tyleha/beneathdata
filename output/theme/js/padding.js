function padding() {
	var heightSlider = $('#sidebar').height();
	var heightAbout = $('#aboutme').height();
	var heightContent = $('.col-sm-9').height();
	alert('heightSidebar ' + heightSlider);
	if (heightContent < heightAbout){
		$('.col-sm-9').css({ paddingBottom : heightContent + heightAbout 'px' });
		alert('heightContent ' + heightContent);
	}
}
