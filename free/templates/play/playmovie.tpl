{% extends "play/playbase.tpl" %}
{% load tplfilter %}

{% block breadcrumb %}
<!-- 站点导航 -->
<div class="container">
  <ul class="breadcrumb">
    <li><a href="/">首页</a></li>
    <li><a href="/classify/type/0/time/0/area/0/page/0">电影</a></li>
    <li>
        <a href="/classify/type/{{ info.flag_type|custom_type_to_num }}/time/0/area/0/page/0">{{ info.flag_type}}</a>
    </li>
    <li class="active"><a href="/info/movie/{{ info.id }}">{{ info.name }}</a></li>
  </ul>
</div>
{% endblock %}

{% block play %}
<!-- 播放容器 -->
<div class="container" id="container-play">
  <div class="prism-player" id="player-con"></div>
  <form style="display:none" id="cipher-form">
  {% csrf_token %}
    <input type="hidden" name="cipher" value="{{ url }}">
  </form>
</div>
{% endblock %}

{% block playurl %}
<!-- 播放线路容器 -->
<div class="container" id="container-playurl">
  <h3>播放线路</h3>
  <ul class="itemlist">
    <li><a href="/play/movie/{{ info.id }}">知否线路</a></li>
  </ul>
  </p>
</div>
{% endblock %}
