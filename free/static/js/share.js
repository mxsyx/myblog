function isPc(){
	let ua = navigator.userAgent;
	if(/Android|iPhone|iPod/i.test(ua)){
    return false;
  } else {
  return true;
  }
}

function searchByKeyword() {
  let keyword;
  if(isPc()){
    keyword = $('input')[0].value;
  } else {
    keyword = $('input')[2].value;
  }

  if(keyword == ''){
    alert("搜索内容不能为空！！！");
    return ;
  }
  window.location.href = `/search/keyword/${keyword}/page/0`
}
function searchKeydown(){
  if (event && event.keyCode == 13) {
    searchByKeyword()
  }
}


function showHistoryBox() {
  $('.history-box ul')[0].style.display = 'block'
}
function closeHistoryBox() {
  $('.history-box ul')[0].style.display = 'none'
}


function clearWatchHistory() {
  $.cookie('whp', '', { expires: -1, path: '/' });
  $.cookie('whn', '', { expires: -1, path: '/' });
  $('.history-box ul')[0].innerHTML = '<li>无历史记录</li>'
}


function share(sharedTo) {
  let url = window.location.href;
  let title = "自在仙影视网"
  let desc = "我正在自在仙影视网上观看影片，欢迎你的加入！"
  let summary = "浮云轻入鹤撩雾，青山深处自在仙。"
  let source = "www.zizaixian.top"
  let pics = "https://www.zizaixian.top/static/images/icon/favicon.png"

  if (url.split('/')[3] == 'info') {
    title = $('h2')[0].innerText
    desc = "我正在自在仙影视网上观看《" + title + "》，一部超级好看的影片，你也来看看吧！ ";
    summary = $('.container-intro .panel-body')[0].innerText.slice(0, 80)
    pics = $('img')[0].src;
  }
  if (url.split('/')[3] == 'play') {
    title = $('.breadcrumb a')[3].innerText
    desc = "我正在自在仙影视网上观看《" + title + "》，一部超级好看的影片，你也来看看吧！ ";
  }

  let qqzoneLink = "http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url="
                    + url + "&title=" + title + "&desc=" + desc + "&summary=" 
                    + summary + "&site=" + source + "&pics=" + pics;

  let qqLink = "http://connect.qq.com/widget/shareqq/index.html?url="
                + url + "&title=" + title + "&source=" + source 
                + "&desc=" + desc + "&pics=" + pics + "&summary=" + summary

  let weiboLink = "http://service.weibo.com/share/share.php?url=" + 
                   url + "&title=" + desc + "&pic=" + pics;

  switch (sharedTo) {
    case 'qq': window.open(qqLink); break;
    case 'qqzone': window.open(qqzoneLink); break;
    case 'weibo': window.open(weiboLink); break;
  }
}
