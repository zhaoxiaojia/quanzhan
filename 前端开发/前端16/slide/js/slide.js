$(function(){
	// 获取slide 中的li标签
	var $li = $('.slide_list li');
	var iLen = $li.length;
	// 获取 < button
	var $prev = $('.prev');
	// 获取 > button
	var $next = $('.next');
	// 获取圆点button
	var $points = $('.points');
	var iNowli = 0;
	var iNextli = 0;

	// 除第一个元素都右移760
	$li.not(':first').css({left:760});
	// 添加圆点
	$li.each(function(i) {
		var $sli = $('<li>');
		if(i==0){
			$sli.addClass('active');
		}
		$sli.appendTo($points);
	});

	// 获取圆点li标签集合
	var $pointsli = $('.points li');
	$pointsli.click(function() {
		iNextli = $(this).index();
		if (iNextli==iNowli) {
			return;
		}
		// 给选中的圆点添加背景色 其余的删除背景色
		$(this).addClass('active').siblings().removeClass('active');
		move();
	});

	// 点击 < button时滚动幻灯片并改变圆点样式
	$prev.click(function() {
		iNextli --;
		move();
		$pointsli.eq(iNextli).addClass('active').siblings().removeClass('active');
	});

	// 点击 > button时滚动幻灯片并改变圆点样式
	$next.click(function() {
		iNextli ++;
		move();
		$pointsli.eq(iNextli).addClass('active').siblings().removeClass('active');
	});

	// 移动幻灯片
	function move(){
		// 第一张幻灯片往前的时候
		if(iNextli<0){
			iNextli = iLen-1;
			iNowli = 0;
			$li.eq(iNextli).css({left:-760});
			$li.eq(iNextli).stop().animate({left:0});
			$li.eq(iNowli).stop().animate({left:760});
			iNowli = iNextli;
			return;
		}
		// 最后一张幻灯片往后的时候
		if(iNextli>iLen-1){
			iNextli = 0;
			iNowli = iLen-1;
			$li.eq(iNextli).css({left:760});
			$li.eq(iNextli).stop().animate({left:0});
			$li.eq(iNowli).stop().animate({left:-760});
			iNowli = iNextli;
			return;
		}
		// 幻灯片从右边过来
		if(iNextli>iNowli){
			// 先把幻灯片放到右边
			$li.eq(iNextli).css({left:760});
			$li.eq(iNowli).stop().animate({left:-760});
		}
		// 幻灯片从左边过来
		else{
			// 先把幻灯片放到左边
			$li.eq(iNextli).css({left:-760});
			$li.eq(iNowli).stop().animate({left:760});
		}
		// 幻灯片归位
		$li.eq(iNextli).stop().animate({left:0});
		iNowli = iNextli;
	}
});