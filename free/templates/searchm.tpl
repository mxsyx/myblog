{% load tplfilter %}

<!DOCTYPE HTML>
<html lang="zh-CN">

<head>
  {% include 'component/meta.tpl' %}
  <title>搜索视频</title>
  {% include 'component/link.tpl' %}
  <link rel="stylesheet" href="/static/css/index.css">
  <style>
    .form-inline {
      width: 80%;
      margin: auto;
      text-align: center;
    }

    .form-inline button {
      width: 40%;
    }
  </style>
</head>

<body>
  <!-- 页面头部 -->
  <header>
    <div class="container">
      <div class="row">
        <div class="col-md-10">
          <a id="logo" href="/">自在仙</a>
          <small>浮云轻入鹤撩雾，青山深处自在仙</small>
        </div>
      </div><!-- /.row -->
    </div><!-- /.container -->
  </header>
  {% include 'component/navbar.tpl' %}

  <div class="container">
    <form class="form-inline">
      <div class="form-group">
        <input type="text" class="form-control" placeholder="输入影片名" onkeydown="searchKeydown()">
      </div>
      <button type="button" class="btn btn-default" onclick="searchByKeyword()">搜索</button>
    </form>
  </div>
</body>

</html>
