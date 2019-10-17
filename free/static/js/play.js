/**
 * 新增历史记录
 * 历史记录通过cookie实现
 * whp 记录着播放过的视频路径
 * whn 记录着播放过的视频名称
 */
function addWatchHistory() {
  let historyPath =   // 历史记录路径字符串
    $.cookie('whp') ? $.cookie('whp') : "";
  let historyName =   // 历史记录名称字符串
    $.cookie('whn') ? $.cookie('whn') : "";
  let paths = historyPath.split('$$');  // 历史记录路径数组
  let names = historyName.split('$$');  // 历史记录名称数组

  // 当前页面的地址与视频名字
  let path = '/play/' + window.location.href.split('/play/')[1];
  let name = $('.breadcrumb a')[3].innerText

  /**
   * 判断当前页面是否记录在历史记录中
   * 若当前页面没有记录在历史记录中，则新增历史记录
   */
  for (var i = 0; i < paths.length && path != paths[i]; i++);

  if (i == paths.length) { // 历史记录中无当前页面地址
    // 历史记录最多写入十条
    // 超过十条时删除尾部记录
    if (paths.length == 10) {
      paths.shift();
      names.shift();
    }
    // 新增历史记录
    paths.push(path)
    names.push(name)
    let historyPathNew = paths.join('$$')
    let historyNameNew = names.join('$$')
    // 更新历史记录
    $.cookie('whp', historyPathNew, { expires: 7, path: '/' });
    $.cookie('whn', historyNameNew, { expires: 7, path: '/' });
  }
}


function submitFeedbackInfo() {
  if ($('#feedback-form')[0].feedbackinfo.value == "") {
    alert("反馈信息不能为空");
    return;
  }
  $.ajax(
    {
      type: "POST",
      dataType: "html",
      url: "/feedback/",
      data: $('#feedback-form').serialize(),
      success:
        function (result) {
          $("#infocon").html("<font color='green'><b>您的反馈我们已经收到，感谢您的反馈！请留意您的邮箱！</b></font>")
          $('#myModal').modal();
        },
      error:
        function (data) {
          $("#infocon").html("<font color='green'><b>Sorry，反馈失败，管理员即将修复BUG</b></font>")
          $('#myModal').modal();
        }
    });
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie(csrftoken));
    }
  });
}


function requestPlay() {
  $.ajax(
    {
      type: "POST",
      dataType: "json",
      url: "/player/",
      data: $('#cipher-form').serialize(),
      success:
        function (result) {
          playVideo(atob(result['url']))
        },
      error:
        function (result) {

        }
    });
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie(csrftoken));
    }
  });
}


function playVideo(url) {
  var player = new Aliplayer({
    "id": "player-con",
    "source": url,
    "width": "100%",
    "height": "100%",
    "autoplay": true,
    "isLive": false,
    "rePlay": false,
    "playsinline": true,
    "preload": true,
    "language": "zh-cn",
    "controlBarVisibility": "hover",
    "useH5Prism": true,
    "extraInfo": {
      "crossOrigin": "anonymous"
    },
    "skinLayout": [
      {
        "name": "bigPlayButton",
        "align": "blabs",
        "x": 30,
        "y": 80
      },
      {
        "name": "H5Loading",
        "align": "cc"
      },
      {
        "name": "errorDisplay",
        "align": "tlabs",
        "x": 0,
        "y": 0
      },
      {
        "name": "infoDisplay"
      },
      {
        "name": "tooltip",
        "align": "blabs",
        "x": 0,
        "y": 56
      },
      {
        "name": "thumbnail"
      },
      {
        "name": "controlBar",
        "align": "blabs",
        "x": 0,
        "y": 0,
        "children": [
          {
            "name": "progress",
            "align": "blabs",
            "x": 0,
            "y": 44
          },
          {
            "name": "playButton",
            "align": "tl",
            "x": 15,
            "y": 12
          },
          {
            "name": "timeDisplay",
            "align": "tl",
            "x": 10,
            "y": 7
          },
          {
            "name": "fullScreenButton",
            "align": "tr",
            "x": 10,
            "y": 12
          },
          {
            "name": "subtitle",
            "align": "tr",
            "x": 15,
            "y": 12
          },
          {
            "name": "setting",
            "align": "tr",
            "x": 15,
            "y": 12
          },
          {
            "name": "volume",
            "align": "tr",
            "x": 5,
            "y": 10
          },
          {
            "name": "snapshot",
            "align": "tr",
            "x": 10,
            "y": 12
          }
        ]
      }
    ]
  }, function (player) {
    console.log('Hello, My friend.')
  }
  );
  /* h5截图按钮, 截图成功回调 */
  player.on('snapshoted', function (data) {
    var pictureData = data.paramData.base64
    var downloadElement = document.createElement('a')
    downloadElement.setAttribute('href', pictureData)
    var fileName = 'Aliplayer' + Date.now() + '.png'
    downloadElement.setAttribute('download', fileName)
    downloadElement.click()
    pictureData = null
  });
  player.on('error', function (e) {
    $('.prism-ErrorMessage').hide();
    $('.prism-button.prism-button-orange').hide();
    if (e.paramData.error_code == 4400) {
      $('.prism-error-content p').html("<h4>播放地址失效</h4>");
    } else if (e.paramData.error_code == 4014) {
      $('.prism-error-content p').html("<h4>网络连接失败</h4>");
    }
    $('.prism-ErrorMessage').show();
    });
}

requestPlay()

addWatchHistory();
