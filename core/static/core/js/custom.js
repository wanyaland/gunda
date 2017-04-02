wow = new WOW({});
wow.init();

var animationEnd = "WebkitAnimationend MozAnimatioend MsAnimationend oanimatedend animationend";

$(document).ready(function() {
    $('#myCarousel').carousel({
	    interval: 10000
	})
});


$(document).ready(function () {

    $('.btn-vertical-slider').on('click', function () {
        
        if ($(this).attr('data-slide') == 'next') {
            $('#myCarousel').carousel('next');
        }
        if ($(this).attr('data-slide') == 'prev') {
            $('#myCarousel').carousel('prev')
        }

    });
});



	var audioElement = document.createElement('audio');
	var name = 'Ed-sheeran Barcelona';
	var src = '';
	$('.music-cover').click(function(){
		audioElement.src = $(this).attr('data-role');
		audioElement.play();
		$('#status').text('Status: Playing');
		$('.audio-name').text(name);
		$('#play').hide();
		$('#pause').show();
	});

	audioElement.setAttribute('src',src);

	audioElement.addEventListener('ended', function(){
		this.play();
	},false);

	audioElement.addEventListener('canplay',function(){
		$('#length').text('duration:'+audioElement.duration + 'seconds');
		$('#source').text('Source:'+ audioElement.src);
		$('#status').text('Status: Ready to play').css('color','green');
	});

	audioElement.addEventListener('timeupdate', function(){
		var currentTime = audioElement.currentTime;
		var duration = audioElement.duration;

		$('.currentTime').text(formatSecondsAsTime(Math.floor(currentTime)));
		$('.duration').text(formatSecondsAsTime(Math.floor(duration)));
		$('.audio-range').stop(true,true).animate({'width':(Math.floor(currentTime)) /Math.floor(duration) *100 +'%'}, 250,'linear');
	});

	function formatSecondsAsTime(secs)
	{
		var hr = Math.floor(secs/3600);
		var min = Math.floor((secs- (hr * 3600))/60);
		var sec = Math.floor(secs- (hr * 3600) - (min * 60));
		return min+' : '+sec;
	}

	$('#play').click(function(){
		audioElement.src = $(this).attr('data-role');
		audioElement.play();
		$('#status').text('Status: Playing');
		$('.audio-name').text(name);
		$('#play').hide();
		$('#pause').show();
	});


	$('#pause').click(function(){
		audioElement.pause();
		$('#status').text('Status: paused');
		$('#pause').hide();
		$('#play').show();
	});


	$('#restart').click(function(){
		audioElement.currentTime = 0;
	});

	$('#forward').click(function(){
		audioElement.currentTime += 10;
		console.log(currentTime);
	});

	$('#rewind').click(function(){
		audioElement.currentTime -= 10;
	});

//END OF THE AUDIO FILE MANIPULATION